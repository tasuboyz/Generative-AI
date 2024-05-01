from aiogram.utils.markdown import hbold
from aiogram import types
from db import Database

class UserInfo:
    def __init__(self, data):
        if isinstance(data, types.Message):
            user = data.from_user
            self.chat_id = data.chat.id
            self.message_id = data.message_id
            self.text= data.text
            self.caption_text = data.caption
        elif isinstance(data, types.CallbackQuery):
            user = data.from_user
            self.chat_id = data.message.chat.id
            self.message_id = data.message.message_id
            self.user_data = data.data
            self.text= data.message.caption
            self.caption_text = data.message.caption
        else:
            return None

        self.user_id = user.id
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.username = user.username
        self.setting = Database().get_language_code(self.user_id)
        if self.setting == None:
            self.language = user.language_code
        else:
            self.language = self.setting
        
    async def get_user_member(self, user_id, bot):
        chat_id= -1001966478916
        user_count = await bot.get_chat_member(chat_id, user_id)
        return user_count.status
    
    async def get_vip_member(self, user_id, bot):
        private_channel = -1002100731393
        user_count = await bot.get_chat_member(private_channel, user_id)
        return user_count.status