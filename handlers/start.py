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

router = Router()

@router.message(commands=["start"])
async def start_command(message: Message):
    await message.answer("Hello! 👋 I'm Save Restricted just send me post link for public or private channel I will download / formward that to you.")
