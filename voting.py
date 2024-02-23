from db import Database
from aiogram import types
from user import UserInfo
import re
from chat_keyboards import Keyboard_Manager
import instance
from aiogram.enums import ParseMode
from language import Language
from logger_config import logger
from config import admin_id, image_vote

class Voting():
    def __init__(self):
        self.bot = instance.bot
        pass

    async def give_star(self, callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        old_text = info.caption_text
        message_id = info.message_id
        user_id = info.user_id
        language_code = info.language
        try:
            user_vote_count = Database().get_vote_count(user_id)
            new_text = self.update_text(callback_query)
            if new_text == old_text:
                you_already_voted = Language().you_already_voted(language_code)
                await callback_query.answer(you_already_voted)
                return
            if user_vote_count % image_vote == 0:
                    Database().update_user_token(1, user_id)
                    await self.bot.send_message(user_id, "+1 🪙")
                    pass
            keyboard = Keyboard_Manager().star_keyboard()
            await self.bot.edit_message_caption(chat_id=info.chat_id, message_id=message_id, caption=new_text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        except Exception as ex:
            logger.error(ex)
            await self.bot.send_message(admin_id, f"{ex}")

    def update_text(self, callback_query):
        info = UserInfo(callback_query)
        original = info.caption_text
        post_id = info.message_id
        user_id = info.user_id       
        vote = info.user_data
        text = original.split('\n')[0]
        info_star = original.split('\n')[1]
        split_stars = info_star.split()
        matches = re.findall(r'\d+', info_star)
        if len(matches) >= 2:
            total_votes = split_stars[-1][1:-1]  # Rimuovi le parentesi
            score = split_stars[-2]
        else:
            score = 0
            total_votes = info_star
        user_vote = Database().get_vote(user_id, post_id)    
        total_votes = total_votes.replace('(', '').replace(')', '')
        total_votes = int(total_votes)  
        score = float(score)  
        vote = float(vote)       
        if user_vote:
            user_vote = float(user_vote)
            if vote == user_vote:
                return original
            else:
                Database().update_vote(user_id, post_id, vote)
                prompt = text
                text = self.update_average(score, total_votes, user_vote, vote, prompt)
                return text
        else:                       
            
            if total_votes > 0:
                average_vote = self.nuova_media(score, total_votes, vote)
                new_score = round(average_vote)
                stars_text = '⭐' * int(new_score)  # Crea una stringa di stelle
                text = f"`{text}`\n{stars_text} {average_vote} ({total_votes + 1})"
            else:
                new_score = vote  # Se non ci sono voti, nessuna stella
                stars_text = '⭐' * int(new_score)  # Crea una stringa di stelle
                text = f"`{text}`\n{stars_text} {new_score} ({total_votes + 1})"       

            Database().save_vote(user_id, post_id, vote)           
            return text
        
    def nuova_media(self, score, total_votes, vote):
        new_score = ((score * total_votes) + vote) / (total_votes + 1)
        return new_score
    
    def update_average(self, score, total_votes, user_vote, vote, prompt):
        sum_votes = (total_votes * score) - user_vote

        sum_votes += vote

        average_vote = sum_votes / total_votes

        new_score = round(average_vote)

        stars_text = '⭐' * new_score
        text = f"`{prompt}`\n{stars_text} {average_vote} ({total_votes})"
        return text
    
    def competition(self):
        
        return