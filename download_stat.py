import asyncio
from user import UserInfo
from language import Language
from instance import bot

class DownloadStatus:
    def __init__(self):
        self.event = asyncio.Event()

    async def wait_message(self, message, messaggio_stato, download_status):
        info = UserInfo(message)
        language = Language()
        chat_id = info.chat_id
        language_code = info.language
        status_symbols = ["⏳", "⌛️"]
        i = 0
        while download_status:  # Assumi che video_downloaded diventi True quando il download è completato
            if download_status == False:
                break
            try:
                # Aggiorna il messaggio di stato con i simboli di stato
                await bot.edit_message_text(chat_id=chat_id, message_id=messaggio_stato.message_id,
                                                    text=status_symbols[i])
            except Exception as e:
                break

            i = (i + 1) % 2  # Cambia i simboli di stato tra ⏳ e ⌛️
            await asyncio.sleep(5)  # Attendi 5 secondi
        return