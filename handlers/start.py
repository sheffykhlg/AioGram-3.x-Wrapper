# ---------------------------------------------------
# File Name: start.py
# Description: A Aiogram Wrapper for Save Restricted Content Bot
# Copyright: devgagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Version: 1.0.0
# ---------------------------------------------------

from aiogram.types import Message
from aiogram.dispatcher.router import Router
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Hello! 👋 there this side Gagan... ")
