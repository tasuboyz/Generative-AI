from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
import os
from user import UserInfo
from language import Language

class Keyboard_Manager:
    def __init__(self):
        self.url = 'https://t.me/TasuPremiumBot'
        self.model_list_konyconi = ['Anime Pastel Dream', 'DreamSharper v7', 'Absolute Reality v1.6', '3D Animation Style', 'Stable Diffusion 1.5', 'Stable Diffusion 2.1']
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
    
    def reply_add_token(self, leonardo=False):
        on = '✅'
        off = '🚫'
        on_off_leonardo = on if leonardo else off
        keyboard = []
        keyboard.append([InlineKeyboardButton(text="About Token 🪙", callback_data="token")])
        keyboard.append([InlineKeyboardButton(text="Language Setting ⚙️", callback_data="setting")])
        keyboard.append([InlineKeyboardButton(text="Buy Premium Pack ⭐️", url=self.url)])
        keyboard.append([InlineKeyboardButton(text=f"Leonardo AI (Vip💎) {on_off_leonardo}",  callback_data="leonardo")])
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
    
    def admin_keyboard(self, enable=False):
        on_off_enable = "✅" if enable else "🚫"
        keyboard = []
        keyboard.append([InlineKeyboardButton(text="number user", callback_data="user_number"),
                         InlineKeyboardButton(text="give to user", callback_data="give_to_user")])
        keyboard.append([InlineKeyboardButton(text="Reset competition", callback_data="reset_competition"),
                         InlineKeyboardButton(text="Send Ads", callback_data="ads")])
        keyboard.append([InlineKeyboardButton(text=f"Enabled {on_off_enable}", callback_data="enable")])
        keyboard.append([InlineKeyboardButton(text="Cancel ❌", callback_data="cancel")])    
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard)
        return keyboard
    
    def custom_keyboard(self, alchemy=None, photoreal=None, model_name=None, size=None):
        on_alchemy = 'Alchemy V2 🧪✅'
        off_alchemy = 'Alchemy V2 🧪🚫(2🪙)'
        on_photoreal = 'PhotoReal V2 📸✅'
        off_photoreal = 'PhotoReal V2 📸🚫(2🪙)'
        on_off_alchemy = on_alchemy if alchemy else off_alchemy
        on_off_photoreal = on_photoreal if photoreal else off_photoreal
        keyboard_buttons = []
        keyboard_buttons.append([InlineKeyboardButton(text=on_off_alchemy, callback_data="alchemy"),
                                 InlineKeyboardButton(text=on_off_photoreal, callback_data="photoreal")])
        if model_name in self.model_list_konyconi:
            keyboard_buttons.append([InlineKeyboardButton(text="Element ⚡️", switch_inline_query_current_chat='element a'),
                                     InlineKeyboardButton(text="Model 🤖", switch_inline_query_current_chat='model')])
        elif photoreal:
            keyboard_buttons.append([InlineKeyboardButton(text="Element ⚡️", switch_inline_query_current_chat='element b'),
                                     InlineKeyboardButton(text="Model 🤖", switch_inline_query_current_chat='photoreal_model')])
        else:
            keyboard_buttons.append([InlineKeyboardButton(text="Element ⚡️", switch_inline_query_current_chat='element b'),
                                     InlineKeyboardButton(text="Model 🤖", switch_inline_query_current_chat='all_model')])
        keyboard_buttons.append([InlineKeyboardButton(text=f"Size {size}", callback_data="size")])
        keyboard_buttons.append([InlineKeyboardButton(text="Confirm ✅", callback_data="confirm")])
        keyboard_buttons.append([InlineKeyboardButton(text="Cancel ❌", callback_data="cancel_leonardo")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
        return keyboard
    
    def custom_elements(self):
        keyboard_buttons = []
        keyboard_buttons.append([InlineKeyboardButton(text="0.1", callback_data="0.1"),
                                 InlineKeyboardButton(text="0.2", callback_data="0.2"),
                                 InlineKeyboardButton(text="0.3", callback_data="0.3"),
                                 InlineKeyboardButton(text="0.4", callback_data="0.4"),
                                 InlineKeyboardButton(text="0.5", callback_data="0.5")])
        keyboard_buttons.append([InlineKeyboardButton(text="0.6", callback_data="0.6"),
                                 InlineKeyboardButton(text="0.7", callback_data="0.7"),
                                 InlineKeyboardButton(text="0.8", callback_data="0.8"),
                                 InlineKeyboardButton(text="0.9", callback_data="0.9"),
                                 InlineKeyboardButton(text="1", callback_data="1")])
        keyboard_buttons.append([InlineKeyboardButton(text="-0.1", callback_data="-0.1"),
                                 InlineKeyboardButton(text="-0.2", callback_data="-0.2"),
                                 InlineKeyboardButton(text="-0.3", callback_data="-0.3"),
                                 InlineKeyboardButton(text="-0.4", callback_data="-0.4"),
                                 InlineKeyboardButton(text="-0.5", callback_data="-0.5")])
        keyboard_buttons.append([InlineKeyboardButton(text="-0.6", callback_data="-0.6"),
                                 InlineKeyboardButton(text="-0.7", callback_data="-0.7"),
                                 InlineKeyboardButton(text="-0.8", callback_data="-0.8"),
                                 InlineKeyboardButton(text="-0.9", callback_data="-0.9"),
                                 InlineKeyboardButton(text="-1", callback_data="-1")])
        keyboard_buttons.append([InlineKeyboardButton(text="Cancel ❌", callback_data="cancel_element")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
        return keyboard
    
    def language_setting(self):
        keyboard_buttons = []
        keyboard_buttons.append([InlineKeyboardButton(text="Italiano 🇮🇹", callback_data="code:it"),
                                 InlineKeyboardButton(text="Spanish 🇪🇦", callback_data="code:es"),
                                 InlineKeyboardButton(text="भारतीय 🇮🇳", callback_data="code:hi")])
        keyboard_buttons.append([InlineKeyboardButton(text="English 🇬🇧", callback_data="code:en"),
                                 InlineKeyboardButton(text="Français 🇫🇷", callback_data="code:fr"),
                                 InlineKeyboardButton(text="Deutsch 🇩🇪", callback_data="code:de")])
        keyboard_buttons.append([InlineKeyboardButton(text="Русский 🇷🇺", callback_data="code:ru"),
                                 InlineKeyboardButton(text="Українська 🇺🇦", callback_data="code:uk"),
                                 InlineKeyboardButton(text="中文 🇨🇳", callback_data="code:zh")])
        keyboard_buttons.append([InlineKeyboardButton(text="العربية🇸🇦", callback_data="code:ar")])
        keyboard_buttons.append([InlineKeyboardButton(text="Cancel ❌", callback_data="cancel")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
        return keyboard
    
    def image_size(self):
        keyboard_buttons = []
        keyboard_buttons.append([InlineKeyboardButton(text="512 × 768", callback_data="size:512x768"),
                                 InlineKeyboardButton(text="768 × 512", callback_data="size:768x512"),
                                 InlineKeyboardButton(text="1024 × 768", callback_data="size:1024x768")])
        keyboard_buttons.append([InlineKeyboardButton(text="1360 × 768", callback_data="size:1360x768"),
                                 InlineKeyboardButton(text="768 × 1360", callback_data="size:768x1360"),
                                 InlineKeyboardButton(text="512 × 512", callback_data="size:512x512")])
        keyboard_buttons.append([InlineKeyboardButton(text="Cancel ❌", callback_data="cancel")])
        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
        return keyboard
    
    