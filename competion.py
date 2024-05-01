import asyncio
from datetime import datetime, timedelta
from db import Database
import instance
from aiogram.types import FSInputFile, Message
from logger_config import logger
import config
from language import Language
from user import UserInfo

class Win_Check:
    def __init__(self):
        self.bot = instance.bot
        self.admin_id = config.admin_id
        self.channel_username = config.channel_username
        self.contest_time = config.contest_time
        self.is_running = instance.is_running
        pass

    async def win_check(self):
        db = Database()
        average_votes = db.calculate_average_votes()

        max_score = max(average_votes, key=lambda x: x[1])[1]

        winning_posts = [post for post in average_votes if post[1] == max_score]

        if len(winning_posts) > 1:
            winning_image_id = max(winning_posts, key=lambda x: x[2])[0]
        else:
            winning_image_id = winning_posts[0][0]

        user_id = db.get_user_id_by_post(winning_image_id)
        input_file = FSInputFile("elmo-elmos-fire.gif")
        post_link = f'<a href="https://t.me/{self.channel_username}/{winning_image_id}">🎉</a>'
        await self.bot.send_animation(chat_id=user_id, animation=input_file, caption="🥇🥳🍾🎉🥂 Token: +20")
        await self.bot.send_message(user_id, post_link)
        await self.bot.send_message(f"@{self.channel_username}", f"{post_link} Winner!")
        total_token = db.user_token(user_id)
        total_token = total_token + 20
        db.update_user_token(total_token, user_id)
        db.reset_competition()

    async def win_check_scheduler(self):
        try:
            while self.is_running:
                submission_time = Database().get_first_submission_of_month()
                if submission_time:

                    submission_time = datetime.strptime(submission_time, '%Y-%m-%d %H:%M:%S')
                    end_time = submission_time + timedelta(hours=self.contest_time)
                
                    current_time = datetime.now()
                    if current_time >= end_time:
                        await self.win_check()

                await asyncio.sleep(10)
        except Exception as ex:
            logger.error(ex)
            await self.bot.send_message(self.admin_id, f"{ex}")
    