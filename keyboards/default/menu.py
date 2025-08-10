# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup
from admin_panel.entities.admin import Admin


def check_user_out_func(user_id):
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("🔶 Товары")

    menu_default.row("ℹ️ Информация", "↗️ Перейти на сайт")
    menu_default.row("💵 Пополнить")
    if int(user_id) in Admin.admins():
        menu_default.row("🎁 Управление товарами 🖍", "📰 Информация о боте")
        menu_default.row("👑 Админ-панель", "🔑 Платежные системы")
    return menu_default


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")
