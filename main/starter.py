# ---------------------------------------------------
# File Name: starter.py
# Description: A Aiogram Wrapper for Save Restricted Content Bot
# Copyright: devgagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Version: 2.0.5
# ---------------------------------------------------

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN

# Shared bot and dispatcher instances
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
