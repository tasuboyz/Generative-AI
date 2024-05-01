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
import asyncio
from limiter import RateLimiter

class Voting():
    def __init__(self):
        self.bot = instance.bot
        self.semaphore = asyncio.Semaphore(1)
        self.rate_limiter = RateLimiter()
        pass

    async def give_star(self, callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        old_text = info.caption_text
        message_id = info.message_id
        user_id = info.user_id
        post_id = info.message_id
        language_code = info.language
        vote = info.user_data
        vote_float = float(vote)
        vote_int = int(vote_float)
        try:           
            if self.rate_limiter.is_limited(user_id, post_id, max_actions=1, period=10):
                wait_to_vote = Language().wait_to_vote(language_code)
                await callback_query.answer(wait_to_vote)
                return 
            user_vote = Database().get_vote(user_id, post_id)
            if user_vote == None:
                user_vote = 0
            if vote_int == int(user_vote):
                you_already_voted = Language().you_already_voted(language_code)
                await callback_query.answer(you_already_voted)
                return    
            user_vote_count = Database().get_vote_count(user_id)            
            vote_changed = Language().vote_changed(language_code)
            await callback_query.answer(vote_changed)
            async with self.semaphore:     
                new_text = self.update_text(callback_query)      
                if user_vote_count[0] % 10 == 0 and user_vote_count[0] != 0:
                        total_token = Database().user_token(user_id)
                        total_token += 1
                        await self.bot.send_message(user_id, "You Win +1 🪙")
                        Database().update_user_token(total_token, user_id)                        
                        pass
                keyboard = Keyboard_Manager().star_keyboard()
                await asyncio.sleep(0.1)                

                await self.bot.edit_message_caption(chat_id=info.chat_id, message_id=post_id, caption=new_text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
                Database().save_vote(user_id, post_id, vote_int)  
        except Exception as ex:
            logger.error(ex, exc_info=True)
            await self.bot.send_message(admin_id, f"{ex}")

    def update_text(self, callback_query):
        info = UserInfo(callback_query)
        original_caption = info.caption_text
        post_id = info.message_id
        user_id = info.user_id       
        vote = info.user_data
        vote = float(vote)
        
        text, score, total_votes = self.extract_caption_info(original_caption)
        user_vote = Database().get_vote(user_id, post_id)
        
        if user_vote:
            user_vote = float(user_vote)
            if vote == user_vote:
                return original_caption
            else:
                text = self.update_average(text, score, total_votes, user_vote, vote)
        else:
            text = self.update_new_vote(text, score, total_votes, vote)
        
        return text

    def extract_caption_info(self, original_caption):
        match_prompt = re.search(r'"(.*?)"', original_caption)
        if match_prompt:
            prompt = match_prompt.group(1)
            rest = original_caption.replace('"' + prompt + '"', '').strip()
        else:
            prompt = original_caption.split('\n')[0]
            rest = original_caption

        match_score = re.search(r'(\d+(\.\d+)?)\s*\(', rest)
        if match_score:
            score = match_score.group(1)
            score = float(score)
        else:
            score = 0

        match_votes = re.search(r'\(\d+\)', rest)
        if match_votes:
            total_votes = int(match_votes.group().strip('()'))
        else:
            total_votes = 0

        return prompt, score, total_votes
        
    def update_new_vote(self, text, score, total_votes, vote):
        if total_votes > 0:
            average_vote = self.calculate_new_average(score, total_votes, vote)
            new_score = round(average_vote)

            stars_text = '⭐' * new_score
            text = f'"`{text}`"\n{stars_text} {round(average_vote, 2)} ({total_votes + 1})'
        else:
            new_score = int(vote)
            stars_text = '⭐' * new_score
            text = f'"`{text}`"\n{stars_text} {new_score}.0 ({total_votes + 1})'             
        return text
    
    def update_average(self, text, score, total_votes, user_vote, vote):
        sum_votes = (total_votes * score) - user_vote
        sum_votes += vote
        average_vote = sum_votes / total_votes
        new_score = round(average_vote)
        stars_text = '⭐' * int(new_score)
        text = f'"`{text}`"\n{stars_text} {round(average_vote, 2)} ({total_votes})'
        return text
    
    def calculate_new_average(self, score, total_votes, vote):
        new_score = ((score * total_votes) + vote) / (total_votes + 1)
        return new_score