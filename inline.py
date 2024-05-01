
import instance
from logger_config import logger
from db import Database, Result
from leonardo import LeonardoAI
from aiogram import types

class InlineCommand():
    def __init__(self):
         self.bot = instance.bot
         self.leonardo = LeonardoAI()
         pass
    
    def choose_photoreal_model(self, user_id):            
        inline_results = []
        db = Database()
        try:
            results = self.leonardo.get_model() 
            result = Result(user_id) 
            photoreal_current = result.photoreal_current
            allowed_models = ["Leonardo Kino XL", "Leonardo Vision XL", "Leonardo Diffusion XL"]
            for result in results['custom_models']:
                Title = result['name']
                if photoreal_current and Title not in allowed_models:
                    continue

                model_id = result['id']
                if result['generated_image'] != None:
                    thumbnail_url = result['generated_image']
                    thumbnail_url = thumbnail_url['url']
                else:
                    thumbnail_url = ''
                
                desciption = result['description']
                db.insert_model(model_id, Title)

                inline_result = types.InlineQueryResultArticle(
                    id=model_id,
                    title=Title,
                    thumbnail_url=thumbnail_url,                   
                    description=desciption,
                    input_message_content=types.InputTextMessageContent(
                        message_text=Title
                    )
                )
                inline_results.append(inline_result)
            return inline_results
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)

    def choose_all_model(self, user_id):            
        inline_results = []
        db = Database()
        try:
            results = self.leonardo.get_model() 
            result = Result(user_id) 
            photoreal_current = result.photoreal_current
            for result in results['custom_models']:
                Title = result['name']

                model_id = result['id']
                if result['generated_image'] != None:
                    thumbnail_url = result['generated_image']
                    thumbnail_url = thumbnail_url['url']
                else:
                    thumbnail_url = ''
                
                desciption = result['description']
                db.insert_model(model_id, Title)

                inline_result = types.InlineQueryResultArticle(
                    id=model_id,
                    title=Title,
                    thumbnail_url=thumbnail_url,                   
                    description=desciption,
                    input_message_content=types.InputTextMessageContent(
                        message_text=Title
                    )
                )
                inline_results.append(inline_result)
            return inline_results
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)

    def choose_element_a(self, user_id):
        inline_results = []
        results = self.leonardo.get_element()  
        result = Result(user_id)
        photoreal_current = result.photoreal_current
        db = Database()
        model_name = db.get_model_name_by_user_id(user_id)

        for result in results['loras']:
            creatorName = result['creatorName']

            if creatorName == 'konyconi':
                element_id = result['akUUID']
                thumbnail_url = result['urlImage']
                Title = result['name']
                desciption = result['description']
                db.insert_elements_id(element_id, Title)

                inline_result = types.InlineQueryResultArticle(
                    id=element_id,
                    title=Title,
                    thumbnail_url=thumbnail_url,                   
                    description=desciption,
                    input_message_content=types.InputTextMessageContent(
                        message_text = f"{Title}: 1"
                    ),
                )
                inline_results.append(inline_result)
        return inline_results
    
    def choose_element_b(self, user_id):
        inline_results = []
        results = self.leonardo.get_element()  
        result = Result(user_id)
        photoreal_current = result.photoreal_current
        db = Database()
        model_name = db.get_model_name_by_user_id(user_id)
        for result in results['loras']:
            creatorName = result['creatorName']

            if creatorName == "Leonardo":
                element_id = result['akUUID']
                thumbnail_url = result['urlImage']
                Title = result['name']
                desciption = result['description']
                db.insert_elements_id(element_id, Title)

                inline_result = types.InlineQueryResultArticle(
                    id=element_id,
                    title=Title,
                    thumbnail_url=thumbnail_url,                   
                    description=desciption,
                    input_message_content=types.InputTextMessageContent(
                        message_text = f"{Title}: 1"
                    ),
                )
                inline_results.append(inline_result)
        return inline_results