# ---------------------------------------------------
# File Name: main.py
# Description: A Aiogram Wrapper for Save Restricted Content Bot
# Copyright: devgagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Version: 1.0.0
# ---------------------------------------------------

import asyncio
from aiogram import Bot
from starter import bot, dp
from handlers import routers

async def main():
    # Include all routers
    for router in routers:
        dp.include_router(router)

    # Start polling
    async with bot:
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
