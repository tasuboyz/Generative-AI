from PIL import Image, ImageColor, ImageOps ,ImageDraw, ImageFont, ImageFilter
import io
import os
import time
import random
import uuid
import glob
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, ReplyKeyboardRemove
from user import UserInfo
from logger_config import logger
import instance
import config
import instance

class FileManager: # crea una classe per gestire i colori e le impostazioni del QR
    def __init__(self):
        self.bot = instance.bot
        self.admin_id = config.admin_id

    def check_file_exists(self, file_path):
        while os.path.exists(file_path):
            file_path = self.generate_random_filename(file_path)
        return file_path

    async def recive_image(self, message):
        chat_id = message.chat.id
        try:
            if message.document or message.photo or message.animation:
                file = message.document or message.photo[-1] or message.animation
                file_info = await self.bot.get_file(file.file_id)
                file_path = file_info.file_path                

                uid = uuid.uuid4()   # Genera un identificatore univoco                
                file_extension = file_path.split(".")[-1]# Ottieni l'estensione del file originale                
                file_name = f"{uid}.{file_extension}"  # Crea il nuovo nome del file con l'identificatore e l'estensione    

                # Specifica il percorso della directory in cui desideri salvare l'immagine
                directory_path = f"UserImage"
                if not os.path.exists(directory_path):
                    os.makedirs(directory_path)

                # Combina il percorso della directory con il nome del file
                download_path = os.path.join(directory_path, file_name)
                file_path = self.check_file_exists(file_path) # Aggiungi questa riga

                await self.bot.download_file(file_path, download_path)
                #await self.bot.download_file(file_path, download_path)

                return download_path, file_name
            return None
        except Exception as ex:
            logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
            await self.bot.send_message(self.admin_id, f"{chat_id}:{ex}")           
            
    def remove_file_if_exists(self, file):    
        for file in glob.glob(file + ".*"):
                if os.path.exists(file):
                    os.remove(file)                                
            
class FileInfo: # crea una classe per gestire i colori e le impostazioni del QR
    def __init__(self, file_name):
        self.nome_completo = os.path.basename(file_name).split(".")[0]
        self.percorso = os.path.dirname(os.path.abspath(file_name)) #visualizza percorso file
        self.file = file_name.split(".")[0]
        self.extention = file_name.split(".")[-1]
            
