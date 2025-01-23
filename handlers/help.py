# ---------------------------------------------------
# File Name: help.py
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

@router.message(commands=["help"])
async def help_command(message: Message):
    await message.answer("No help yet...")
