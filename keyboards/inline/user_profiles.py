# - *- coding: utf- 8 - *-
from utils.db_api.sqlite import get_userx, get_purchasesx


def get_user_profile(user_id):
    get_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = f"<b>Доборо пожаловать в hydra:</b>\n\n" \
          f"" \
          f"""<b>🔷 Привет</b>: <code>{get_user[1]}</code> вижу что ты решил пополнить свой баланс, нажми на кнопки чтобы пополнять свой баланс так же не забудь что у нас есть свой <a href="https://hydra-review.ru/">сайт</a>\n\n""" \
          f"<b>🔷 Это единственный бот Hydra! Остерегайтесь фейков, официальный линк бота - @hydra_fakebot</b> \n\n" \
          f"<b>🔷 Дней с нами</b>: <code>{get_user[6]}</code>\n\n" \
          f"" \
          f"<b>🔷 Ваш баланс</b>: <code>{get_user[4]}руб</code>\n\n🧸 На данный момент пополнить можно только через оператора - @yacud3a" \

    return msg


def search_user_profile(user_id):
    get_status_user = get_userx(user_id=user_id)
    get_purchases = get_purchasesx("*", user_id=user_id)
    count_items = 0
    if len(get_purchases) >= 1:
        for items in get_purchases:
            count_items += int(items[5])
    msg = f"<b>📱 Профиль пользователя:</b> <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"🔑 ID: <code>{get_status_user[1]}</code>\n" \
          f"👤 Логин: <b>@{get_status_user[2]}</b>\n" \
          f"Ⓜ Имя: <a href='tg://user?id={get_status_user[1]}'>{get_status_user[3]}</a>\n" \
          f"🕜 Регистрация: <code>{get_status_user[6]}</code>\n" \
          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
          f"💳 Баланс: <code>{get_status_user[4]}руб</code>\n" \
          f"💵 Всего пополнено: <code>{get_status_user[5]}руб</code>\n" \
          f"🎁 Куплено товаров: <code>{count_items}шт</code>\n"
    return msg
