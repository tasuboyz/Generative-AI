from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import os
from user import UserInfo
from language import Language

class Keyboard_Manager:
    def __init__(self):
        self.url = 'https://t.me/TasuPremiumBot'
        self.language = Language()

    def buy_inline_keyboard(self, message=None):
        keyboard = []
        text = "Buy Token"
        keyboard.append([InlineKeyboardButton(text=text, url=self.url)])

        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    # def create_start_reply_keyboard(self, message=None):
    #     keyboard = []
    #     text = "Buy Token"
    #     keyboard.append([KeyboardButton(text=text, web_app=WebAppInfo(url=self.example_url))])

    #     keyboard = ReplyKeyboardMarkup(inline_keyboard=keyboard)
    #     return keyboard
    
    def star_keyboard(self):
        keyboard = []
        keyboard.append([InlineKeyboardButton(text="1⭐️", callback_data="1.0"),
                        InlineKeyboardButton(text="2⭐️", callback_data="2.0"),
                        InlineKeyboardButton(text="3⭐️", callback_data="3.0")])
        keyboard.append([InlineKeyboardButton(text="4⭐️", callback_data="4.0"),
                         InlineKeyboardButton(text="5⭐️", callback_data="5.0")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def vote_keyboard(self, score):
        keyboard = []
        keyboard.append([InlineKeyboardButton(text=f"U1 {score}⭐️", callback_data="U1"),
                        InlineKeyboardButton(text=f"U2 {score}⭐️", callback_data="U2")])
        keyboard.append([InlineKeyboardButton(text=f"U3 {score}⭐️", callback_data="U3"),
                         InlineKeyboardButton(text=f"U4 {score}⭐️", callback_data="U4")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def send_keyboard(self, language_code):
        send_to_channel = self.language.send_to_channel(language_code)
        keyboard = []
        keyboard.append([InlineKeyboardButton(text=send_to_channel, callback_data="send")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def inline_keyboard_for_admin(self):
        keyboard = []
        keyboard.append([InlineKeyboardButton(text="Modifica 🛠", callback_data="modify")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def send_to_channel_keyboard(self):
        keyboard = []
        keyboard.append([InlineKeyboardButton(text="Invia al canale 🎁", callback_data="send_to_leonardo")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def reply_add_token(self):
        keyboard = []
        keyboard.append([InlineKeyboardButton(text="About Token 💎", callback_data="token")])
        keyboard.append([InlineKeyboardButton(text="Buy Premium Pack ⭐️", url=self.url)])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def yes_or_no(self, language_code):
        yes = self.language.yes(language_code)
        no = self.language.no(language_code)
        keyboard = []
        keyboard.append([InlineKeyboardButton(text=yes, callback_data="yes"),
                         InlineKeyboardButton(text=no, callback_data="cancel")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def admin_keyboard(self):
        keyboard = []
        keyboard.append([InlineKeyboardButton(text="number user", callback_data="user_number"),
                         InlineKeyboardButton(text="give to user", callback_data="give_to_user")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
