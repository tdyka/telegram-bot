import telebot
import webbrowser
from telebot import types
import pizza

bot = telebot.TeleBot('8317999106:AAE5Y1STOCj_zyPrBFtINj-c_vMIa66aEhw')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Вітаю, {message.from_user.first_name}")

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://classroom.google.com/u/1/c/ODAwNjM0NDczNDk0?hl=ru')

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🍕 Піца", callback_data="cat_Піца"),
        types.InlineKeyboardButton("🍣 Суші", callback_data="cat_Суші"),
        types.InlineKeyboardButton("🍔 Бургер", callback_data="cat_Бургер"),
        types.InlineKeyboardButton("🥔 Картопля", callback_data="cat_Картопля"),
        types.InlineKeyboardButton("🍝 Паста", callback_data="cat_Паста"),
        types.InlineKeyboardButton("🥤 Напої", callback_data="cat_Напої"),
        types.InlineKeyboardButton("🍰 Десерти", callback_data="cat_Десерти"),
    )

    markup.add(types.InlineKeyboardButton("🔥 Акція «Середа»", callback_data="promo_wed"))
    bot.send_message(
        message.chat.id,
        f"{message.from_user.first_name}, оберіть категорію або акцію 👇",
        reply_markup=markup
    )

@bot.message_handler(commands=['sale'])
def sale(message):
    bot.send_message(
        message.chat.id,
        "🔥 Акція «Середа»!\nКожна друга піцца зі знижкою 50% у середу!"
    )

# --- обробка натискань усіх кнопок ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # якщо натиснули категорію
    if call.data.startswith("cat_"):
        category = call.data.split("_", 1)[1]

        if category == "Піца":
            bot.answer_callback_query(call.id)
            pizza.show_pizza_list(bot, call.message.chat.id)
        else:
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id,
                             f"Поки немає товарів у категорії {category}")

    # якщо вибрано конкретну піцу
    elif call.data.startswith("pizza_"):
        pizza_name = call.data.split("_", 1)[1]
        pizza.handle_pizza_callback(bot, call, pizza_name)


    elif call.data == "promo_wed":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id,
                         "🔥 Акція «Середа»!\nКожна друга піцца зі знижкою 50% у середу!")

    elif call.data == "back_pizza":
        bot.answer_callback_query(call.id)
        pizza.show_pizza_list(bot, call.message.chat.id)

    elif call.data == "back_main":
        bot.answer_callback_query(call.id)
        menu(call.message)


bot.polling(non_stop=True)
