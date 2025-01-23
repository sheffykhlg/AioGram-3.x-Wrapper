# ---------------------------------------------------
# File Name: __init__.py
# Description: A Aiogram Wrapper for Save Restricted Content Bot
# Copyright: devgagan
# GitHub: https://github.com/devgaganin/
# Telegram: https://t.me/team_spy_pro
# YouTube: https://youtube.com/@dev_gagan
# Version: 1.0.0
# ---------------------------------------------------


from .start import router as start_router
from .help import router as help_router
from .echo import router as echo_router

routers = [start_router, help_router]
