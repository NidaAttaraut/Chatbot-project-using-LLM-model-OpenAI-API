import logging
from aiogram import Bot, Dispatcher, excecutor,types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
print(API_TOKEN)

#configure logging
logging.basicConfig(Level=logging.INFO)

#Intitialize bot and dispatcher
bot =Bot(token=API_TOKEN)
dp =Dispatcher(bot)

