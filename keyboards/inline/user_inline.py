# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


popolnit_kb = InlineKeyboardButton(text="💵 Пополнить", callback_data="user_input")
input_kb = InlineKeyboardButton(text="🛒 Мои покупки", callback_data="my_buy")
open_profile_inl = InlineKeyboardMarkup()
open_profile_inl.add(popolnit_kb)





# Кнопка с возвратом к профилю
to_ref_kb = InlineKeyboardMarkup()
to_ref_kb.add(InlineKeyboardButton(text="Назад", callback_data="ref_sistem"))
