from aiogram import types
from user import UserInfo
from db import Database, Result
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from logger_config import logger
from chat_keyboards import Keyboard_Manager
import instance
from config import admin_id
from aiogram.enums import ParseMode
from state import Form
import re
import time
from leonardo import LeonardoAI
from language import Language
from download_stat import DownloadStatus
import asyncio
from inline import InlineCommand

class LeonardoCommand():
    def __init__(self):
         self.keyboards = Keyboard_Manager()
         self.bot = instance.bot
         self.leonardo = LeonardoAI()
         self.inline = InlineCommand()
         pass
    
    async def cancel_operation(self, callback_query: types.CallbackQuery, state: FSMContext):
            await state.clear()
            info = UserInfo(callback_query)
            chat_id = info.chat_id
            message_id = info.message_id
            user_id = info.user_id
            db = Database()
            db.delate_image(user_id)
            db.delate_option(user_id)
            db.delate_elements(user_id)
            await self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Operation delated")

    async def cancel_element(self,  callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        chat_id = info.chat_id
        user_id = info.user_id
        a = callback_query.message.md_text
        try:
            selected_element = a.split(':')[0].strip()
            
            message_id = info.message_id
            user_id = info.user_id
            db = Database()
            model_name = db.get_model_name_by_user_id(user_id)
            element_id = db.get_element_id(selected_element)
            db.delate_selected_element(user_id=user_id, element_id=element_id[0])
            result = Result(user_id)
            prompt = result.prompt
            post_id = result.post_id
            alchemy_current = result.alchemy_current
            photoreal_current = result.photoreal_current
            if alchemy_current:
                Alchemy_V2 = "Alchemy V2 🧪"
            else:
                Alchemy_V2 = ""
            if photoreal_current:
                PhotoReal_V2 = "PhotoReal V2 📸"
            else:
                PhotoReal_V2 = ""
            elements = db.get_element_name(user_id)  # recupera tutti gli element_id per l'utente
            elements_string = "\n".join(elements)
            keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name)
            await self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="Element delated")
            await self.bot.edit_message_text(chat_id=user_id, message_id=post_id, text = f'"`{prompt}`"\nElements ⚡️:\n{elements_string} \n{Alchemy_V2}\n{PhotoReal_V2}\nModel🤖:\n{model_name}', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True) 

    async def inline_query_handler(self, query: types.InlineQuery):
        await asyncio.sleep(2)
        inline_results = []
        user_id = query.from_user.id
        result = query.query
        try:
            if result == "element a":
                inline_results = self.inline.choose_element_a(user_id)
                await query.answer(inline_results)
            elif result == "element b":
                inline_results = self.inline.choose_element_b(user_id)
                await query.answer(inline_results)
            elif result == "all_model":
                inline_results = self.inline.choose_all_model(user_id)
                await query.answer(inline_results)
            elif result == "photoreal_model":
                inline_results = self.inline.choose_photoreal_model(user_id)
                await query.answer(inline_results)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)

    async def set_alchemy_photoreal(self, callback_query: types.CallbackQuery, state: FSMContext):
        info = UserInfo(callback_query)
        db = Database()
        user_id = info.user_id
        message_id = info.message_id
        caption = callback_query.message.text
        data = info.user_data
        try:
            model_name = db.get_model_name_by_user_id(user_id)
            option = db.get_option(user_id)
            result = Result(user_id)

            photoreal_current = result.photoreal_current 
            alchemy_current = result.alchemy_current
            prompt = result.prompt
            elements = db.get_element_name(user_id)  # recupera tutti gli element_id per l'utente
            elements_string = "\n".join(elements)
            size = db.get_image_size(user_id)

            if option is None:
                if data.startswith('alchemy'):
                    db.insert_option(user_id=user_id, alchemy=True, photoreal=False)
                    alchemy_current = not alchemy_current
                    keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name, size=size)
                    if alchemy_current:
                        Alchemy_V2 = "Alchemy V2 🧪"
                    else:
                        Alchemy_V2 = ""
                    if photoreal_current:
                        PhotoReal_V2 = "PhotoReal V2 📸"
                    else:
                        PhotoReal_V2 = ""
                if data.startswith('photoreal'):
                    db.insert_option(user_id=user_id, alchemy=False, photoreal=True)
                    photoreal_current = not photoreal_current
                    keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name, size=size)
                    if photoreal_current:
                        PhotoReal_V2 = "PhotoReal V2 📸"
                    else:
                        PhotoReal_V2 = ""
                    if alchemy_current:
                        Alchemy_V2 = "Alchemy V2 🧪"
                    else:
                        Alchemy_V2 = ""

                #db.insert_option(user_id=user_id, alchemy=not alchemy_current, photoreal=photoreal_current)
                
                await self.bot.edit_message_text(chat_id=user_id, message_id=message_id, text = f'"`{prompt}`"\nElements ⚡️:\n{elements_string} \n{Alchemy_V2}\n{PhotoReal_V2}\nModel🤖:\n{model_name}', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
            else:         
                if data.startswith('alchemy'):
                    alchemy_current = not alchemy_current
                    db.insert_option(user_id=user_id, alchemy=alchemy_current, photoreal=photoreal_current)
                    
                    keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name, size=size)
                    if photoreal_current:
                        PhotoReal_V2 = "PhotoReal V2 📸"
                    else:
                        PhotoReal_V2 = ""
                    if alchemy_current:
                        Alchemy_V2 = "Alchemy V2 🧪"
                    else:
                        Alchemy_V2 = ""
                if data.startswith('photoreal'):
                    photoreal_current = not photoreal_current
                    db.insert_option(user_id=user_id, alchemy=alchemy_current, photoreal=photoreal_current)
                    keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name, size=size)
                    if photoreal_current:
                        PhotoReal_V2 = "PhotoReal V2 📸"
                    else:
                        PhotoReal_V2 = ""
                    if alchemy_current:
                        Alchemy_V2 = "Alchemy V2 🧪"
                    else:
                        Alchemy_V2 = ""
                    db.delate_elements(user_id)
                    model_name = "Leonardo Vision XL"                    
                    model_id = db.get_model_id(model_name)
                    db.insert_user_model(user_id, model_id)
                    elements = db.get_element_name(user_id)  # recupera tutti gli element_id per l'utente
                    elements_string = "\n".join(elements)
                
                await self.bot.edit_message_text(chat_id=user_id, message_id=message_id, text = f'"`{prompt}`"\nElements ⚡️:\n{elements_string} \n{Alchemy_V2}\n{PhotoReal_V2}\nModel🤖:\n{model_name}', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        except Exception as ex:
            await self.bot.send_message(admin_id, f"{ex}")
            logger.error(ex, exc_info=True)

    async def recive_prompt(self, message: types.Message, state: FSMContext):
        info = UserInfo(message)
        db = Database()
        user_id = info.user_id
        text = message.text
        try:
            model_name = db.get_model_name_by_user_id(user_id)
            size = db.get_image_size(user_id)
            keyboard = self.keyboards.custom_keyboard(model_name=model_name, size=size)
            prompt = await message.answer(text=f'"`{text}`"', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
            await state.set_state(Form.set_selement)  
            post_id = prompt.message_id
            db.insert_prompt(user_id, post_id, text)
        except Exception as ex:
            await self.bot.send_message(admin_id, f"{ex}")
            logger.error(ex)

    async def confirm_prompt(self, Callback: types.CallbackQuery, state: FSMContext):
        info = UserInfo(Callback)
        db = Database()
        user_id = info.user_id
        message_id = info.message_id
        text = Callback.message.text
        language_code = info.language
        await state.clear()             
        try:
            waiting_message = await self.bot.edit_message_text(chat_id=user_id, message_id=message_id,text=Language().waiting(language_code))
            download_status = DownloadStatus()
            asyncio.create_task(download_status.wait_message(Callback, waiting_message, True))
            prompt = text.split('\n')[0].strip('"')
            other = re.sub(r'"[^"]*"', '', text) 
            match = re.search('Model🤖:\s*(.*)', other)
            if match:
                model = match.group(1)
                model_id = db.get_model_id(model)
            else:
                model_name = db.get_model_name_by_user_id(user_id)
                model_id = db.get_model_id(model_name)
                
            element_pattern = r'([\w\s&]+):\s*(-?[\d.]+)'
            #elements = dict(re.findall(element_pattern, text))
            elements = dict((key.strip(), value) for key, value in re.findall(element_pattern, other))
            if len(elements) > 0:
                keys = elements.keys()
                chiavi_stringhe = [str(chiave) for chiave in keys]
                ids = []
                for key in chiavi_stringhe:
                    element_id = db.get_element_id(key)
                    ids.append(element_id[0])
                corrispondenze = {chiave: id for chiave, id in zip(elements.keys(), ids)}

                elementi_con_id = {corrispondenze[chiave]: valore for chiave, valore in elements.items()}
            else:
                elementi_con_id = None

            alchemy = 'Alchemy V2' in text
            photo_real = 'PhotoReal V2' in text
            
            await self.handle_set_threshold(Callback, prompt, elementi_con_id, alchemy, photo_real, waiting_message, model_id)
            db.insert_vip_member(user_id, True)
            db.delate_image(user_id)
            db.delate_option(user_id)
            db.delate_elements(user_id)
        except Exception as ex:
            await self.bot.send_message(admin_id, f"{ex}")
            logger.error(ex, exc_info=True)          

    async def set_element(self, message: types.Message):
        info = UserInfo(message)
        user_id = info.user_id
        message_id = info.message_id
        element = message.text
        db = Database()
        try:
            size = db.get_image_size(user_id)
            keyboard = self.keyboards.custom_elements()

            
            selected_element = element.split(':')[0].strip()
            model_id = db.get_model_id(element)
            if model_id:                
                db.insert_user_model(user_id, model_id)
                db.delate_elements(user_id)
                model_name = db.get_model_name_by_user_id(user_id)
            else:
                model_name = db.get_model_name_by_user_id(user_id)
            
            element_id = db.get_element_id(selected_element)
            elements = db.get_element_name(user_id)
            
            for element in elements:
                if element.startswith(selected_element):
                    return
            if len(elements) < 4:
                if element_id != None:
                    element_id = element_id[0]
                    await message.send_copy(user_id, reply_markup=keyboard)
                    db.insert_element(user_id, element_id)  
                elements_id = db.get_elements(user_id)  # recupera tutti gli element_id per l'utente
                elements = db.get_element_name(user_id)

                result = Result(user_id)
                prompt = result.prompt
                post_id = result.post_id
                alchemy_current = result.alchemy_current
                photoreal_current = result.photoreal_current

                elements_string = "\n".join(elements)

                if photoreal_current:
                    PhotoReal_V2 = "PhotoReal V2 📸"
                else:
                    PhotoReal_V2 = ""
                if alchemy_current:
                    Alchemy_V2 = "Alchemy V2 🧪"
                else:
                    Alchemy_V2 = ""
                db.insert_prompt(user_id, post_id, prompt)
                keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name, size=size)
                await self.bot.edit_message_text(chat_id=user_id, message_id=post_id, text = f'"`{prompt}`"\nElements ⚡️: \n{elements_string} \n{Alchemy_V2}\n{PhotoReal_V2}\nModel🤖:\n{model_name}', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
            else:
                return
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(admin_id, f"{ex}")   
        finally:
            await self.bot.delete_message(chat_id=user_id, message_id=message_id)

    async def handle_set_threshold(self, Callback, prompt, elements, alchemy, photo_real, waiting_message, model_id):
        info = UserInfo(Callback)
        chat_id = info.chat_id
        user_id = info.user_id
        db = Database()
        language_code = info.language
        #await state.finish()
        try:
            if photo_real:
                allowed_models = ["aa77f04e-3eec-4034-9c07-d0f619684628", "5c232a9e-9061-4777-980a-ddc8e65647c6", "1e60896f-3c26-4296-8ecc-53e2afecc132"]
                if model_id not in allowed_models:
                    model_id = "aa77f04e-3eec-4034-9c07-d0f619684628"               
            total_token = db.user_token(user_id)
            if total_token > 1:            
                size = db.get_image_size(user_id)
                result = self.leonardo.generation(prompt=prompt, alchemy=alchemy, photoReal=photo_real, elements=elements, model_id=model_id, size=size)
                if isinstance(result, str):
                    await self.bot.send_message(chat_id=chat_id, text=result)
                    return
                generationId = result['sdGenerationJob']['generationId']
                apiCreditCost = result['sdGenerationJob']['apiCreditCost']
                
                # db.image_id(user_id, generationId)
                # image_id =db.get_image_ids(user_id)
                download_status = DownloadStatus()
                await asyncio.sleep(45)
                image_url = self.leonardo.get_image(generationId, prompt)
                if image_url is None:
                    await asyncio.sleep(30)
                    image_url = self.leonardo.get_image(generationId, prompt)
                keyboard = self.keyboards.send_keyboard(language_code)
                await download_status.wait_message(Callback, waiting_message, False)
                await self.bot.delete_message(chat_id, waiting_message.message_id)
                if apiCreditCost < 20:
                    await self.bot.send_photo(chat_id, photo=f"{image_url}", caption=f'"`{prompt}`"\n(0)', parse_mode=ParseMode.MARKDOWN)
                else:
                    await self.bot.send_photo(chat_id, photo=f"{image_url}", caption=f'"`{prompt}`"\n(0)', parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)
                if alchemy or photo_real:
                    total_token -= 2
                else:
                    total_token -= 1
                db.update_user_token(total_token, user_id)
                user_image = f'<a href="{image_url}">{apiCreditCost}"</a>'
                await self.bot.send_message(chat_id=admin_id, text=f"{user_image}")
            else:
                keyboard = Keyboard_Manager().buy_inline_keyboard()
                not_token = Language().have_not_token(language_code)
                await Callback.message.reply(not_token, reply_markup=keyboard)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}, url={image_url}", exc_info=True)
            await self.bot.send_message(admin_id, f"{ex}, url={image_url}")   
            await self.bot.send_message(user_id, "Ops... Error has occurred, this mode is in testing phase, thaks for your patience!")

    async def set_element_point(self, callback: types.CallbackQuery):
        info = UserInfo(callback)
        db = Database()
        chat_id = info.chat_id
        user_id = info.user_id
        message_id = info.message_id
        data = callback.data
        a = callback.message.md_text
        try:
            size = db.get_image_size(user_id)
            model_name = db.get_model_name_by_user_id(user_id)
            
            selected_element = a.split(':')[0].strip()
            value = a.split(':')[1].strip()
            value = value.replace("\\", "")
            if data == value:
                await callback.answer("It's same")
                return
            result = Result(user_id)
            prompt = result.prompt
            post_id = result.post_id
            alchemy_current = result.alchemy_current
            photoreal_current = result.photoreal_current
            if photoreal_current:
                PhotoReal_V2 = "PhotoReal V2 📸"
            else:
                PhotoReal_V2 = ""
            if alchemy_current:
                Alchemy_V2 = "Alchemy V2 🧪"
            else:
                Alchemy_V2 = ""
            elements = db.get_element_name(user_id)

            new_value = f"{selected_element}:{data}"
            elements_id = db.get_element_id(selected_element)
            db.update_gradation(gradation=float(data), element_id=elements_id[0])
            db.insert_element(user_id, f"{selected_element}:{data}")
            new_elements_list = [new_value if s.startswith(selected_element) else s for s in elements]
            new_elements_string = '\n'.join(new_elements_list)

            db.insert_prompt(user_id, post_id, prompt)
            keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name, size=size)
            keyboard_elements = self.keyboards.custom_elements()
            await self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"{selected_element}:{data}", reply_markup=keyboard_elements)
            await self.bot.edit_message_text(chat_id=user_id, message_id=post_id, text = f'"`{prompt}`"\nElements ⚡️: \n{new_elements_string} \n{Alchemy_V2}\n{PhotoReal_V2}\nModel🤖:\n{model_name}', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(admin_id, ex)

    async def choose_size(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        keyboard = self.keyboards.image_size()
        await callback_query.message.reply("Choose size:", reply_markup=keyboard)

    async def recive_choosed_size(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        db = Database()
        user_id = info.user_id
        data = info.user_data
        message_id = info.message_id
        try:
            saved_size = db.get_image_size(user_id)
            
            size = data.split("size:")[1]
            if size == saved_size:
                await callback_query.answer("You already choosed")
                return
            db.insert_image_size(user_id=user_id, size=size)
            
            result = Result(user_id)
            prompt = result.prompt
            post_id = result.post_id
            alchemy_current = result.alchemy_current
            photoreal_current = result.photoreal_current
            model_name = db.get_model_name_by_user_id(user_id)
            keyboard = self.keyboards.custom_keyboard(alchemy=alchemy_current, photoreal=photoreal_current, model_name=model_name, size=size)
            await self.bot.edit_message_reply_markup(chat_id=user_id, message_id=post_id, reply_markup=keyboard)          
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(admin_id, ex)
        finally:
            try:
                await self.bot.edit_message_text(text=f"{size}", chat_id=user_id, message_id=message_id)
            except Exception as ex:
                logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)