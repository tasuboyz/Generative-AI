from bot import BOT
from ascii import art
import asyncio
from logger_config import logger
from db import Database
from competion import Win_Check
import sys
import instance

async def on_start():    
    print(art)
    Database().create_table()

async def on_stop():
    instance.is_running = False
    print("Bot fermato")

async def main():
    try:       
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop) 
        my_bot = BOT()
        await on_start()

        your_instance = Win_Check()
       
        asyncio.create_task(your_instance.win_check_scheduler())
        await my_bot.dp.start_polling(my_bot.bot)

    except KeyboardInterrupt:
        print("Interrotto dall'utente")
        
    except Exception as ex:
        logger.error(f"Errore durante l'esecuzione di handle_set_state: {ex}", exc_info=True)
    finally:
        await on_stop()
        
if __name__ == '__main__':   
    asyncio.run(main())