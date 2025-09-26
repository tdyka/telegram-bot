from telebot import types

def show_pizza_list(bot: object, chat_id: object) -> None:
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton("Гавайська", callback_data="pizza_Гавайська"),
               types.InlineKeyboardButton("Маргарита", callback_data="pizza_Маргарита"),
               types.InlineKeyboardButton("Пепероні", callback_data="pizza_Пепероні"),
               types.InlineKeyboardButton("4 сири", callback_data="pizza_4_сири"))
    markup.add(types.InlineKeyboardButton("⬅️ Головне меню", callback_data="back_main"))
    bot.send_message(chat_id, "Оберіть піцу 🍕:", reply_markup=markup)

def send_hawaiian_pizza(bot, call):
    bot.answer_callback_query(call.id)
    photo_url = "https://tb-static.uber.com/prod/image-proc/processed_images/06465f935e66cfa20230e9c5a49d919f/4218ca1d09174218364162cd0b1a8cc1.jpeg"
    caption = "Гавайська піцца – 179 грн\nТоматний соус, сир моцарела, шинка, ананас."
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🟢 Купити на сайті 🟢",
                                   url="https://example.com/product/hawaiian-pizza"),
        types.InlineKeyboardButton("⬅️ Назад до піц", callback_data="back_pizza")
    )
    markup.add(
        types.InlineKeyboardButton("🏠 Головне меню", callback_data="back_main")
    )
    bot.send_photo(call.message.chat.id, photo_url, caption=caption, reply_markup=markup)

def send_pepperoni_pizza(bot, call):
    bot.answer_callback_query(call.id)
    photo_url = "https://i.pinimg.com/736x/5c/83/52/5c8352581812d088b92349a56e2cfe90.jpg"
    caption = "Пепероні – 189 грн\nТоматний соус, сир моцарела, ковбаса пепероні."
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🟢 Купити на сайті 🟢",
                                   url="https://example.com/product/pepperoni-pizza"),
        types.InlineKeyboardButton("⬅️ Назад до піц", callback_data="back_pizza")
    )
    markup.add(
        types.InlineKeyboardButton("🏠 Головне меню", callback_data="back_main")
    )
    bot.send_photo(call.message.chat.id, photo_url, caption=caption, reply_markup=markup)

def send_margarita_pizza(bot, call):
    bot.answer_callback_query(call.id)
    photo_url = "https://i.pinimg.com/736x/37/36/fd/3736fd91ce58c7ea10ac449bf3cc7718.jpg"
    caption = "Маргарита - 189 грн\nТоматний соус, сир моцарела, свіжий базилік, оливкова олія."
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🟢 Купити на сайті 🟢",
                                   url="https://example.com/product/margarita-pizza"),
        types.InlineKeyboardButton("⬅️ Назад до піц", callback_data="back_pizza")
    )
    markup.add(
        types.InlineKeyboardButton("🏠 Головне меню", callback_data="back_main")
    )
    bot.send_photo(call.message.chat.id, photo_url, caption=caption, reply_markup=markup)

def send_4cheese_pizza(bot, call):
    bot.answer_callback_query(call.id)
    photo_url = "https://i.pinimg.com/736x/ed/71/24/ed7124aa0c4616269bd88bb6410a5dde.jpg"
    caption = "4 сири - 199 грн\nСоус бешамель, моцарелла, сир дорблю, пармезан, твердий сир, орегано."
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("🟢 Купити на сайті 🟢",
                                   url="https://example.com/product/4cheese-pizza"),
        types.InlineKeyboardButton("⬅️ Назад до піц", callback_data="back_pizza")
    )
    markup.add(
        types.InlineKeyboardButton("🏠 Головне меню", callback_data="back_main")
    )
    bot.send_photo(call.message.chat.id, photo_url, caption=caption, reply_markup=markup)

def handle_pizza_callback(bot, call, pizza_name):
    if pizza_name == "Гавайська":
        send_hawaiian_pizza(bot, call)
    elif pizza_name == "Пепероні":
        send_pepperoni_pizza(bot, call)
    elif pizza_name == "Маргарита":
        send_margarita_pizza(bot, call)
    elif pizza_name == "4_сири":
        send_4cheese_pizza(bot, call)
    else:
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"Піца {pizza_name} поки недоступна")