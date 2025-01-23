# Telegram Bot with Aiogram 3.x

This repository provides a modular structure for creating a Telegram bot using the **Aiogram 3.x** framework. It allows you to easily add new features and manage bot functionality in separate files for better scalability and maintainability.

---

## Features

- Modular design using **routers** for better code organization.
- Simple and clear structure to add new features (e.g., commands like `/start`, `/help`, or handling contacts).
- Ready-to-use bot instance for seamless integration.
- Scalable for small bots or large projects with multiple functionalities.

---

## Project Structure

```plaintext
.
├── handlers/               # Folder for all feature-specific logic
│   ├── __init__.py         # Router aggregation for all handlers
│   ├── start.py            # /start command handler
│   ├── help.py             # /help command handler
│   └── add more .py        # Custom handler for contacts
├── starter.py              # starter for bot
├── main.py                 # Entry point for the bot
└── README.md               # This file
```

---

## Installation

1. **fork, start and Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install dependencies:**

   Use Python 3.10 or higher and install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure `requirements.txt` includes:

   ```plaintext
   aiogram>=3.0.0b7
   python-dotenv
   ```

3. **Set up your bot token:**

   Create a `.env` file in the root directory:

   ```env
   BOT_TOKEN=your_bot_token_here
   ```

---

## How It Works

### Main File: `main.py`

The `main.py` file is the entry point of the bot. It initializes the bot, loads all handlers from the `handlers` directory, and starts polling.

### Handlers: `handlers/`

Each feature or command is written as a separate Python file in the `handlers` directory. For example:
- `start.py` handles the `/start` command.
- `help.py` handles the `/help` command.
- `contacts.py` handles contact-related commands or events.

The `handlers/__init__.py` file aggregates all handlers into a single list of routers.

### Router Aggregation: `starter.py`

This file starts the bot.

---

## How to Add a New Feature

Follow these steps to add a new feature, such as handling contacts:

1. **Create a new file in the `handlers` directory:**

   Create a file named `contacts.py`:

   ```bash
   touch handlers/contacts.py
   ```

2. **Define a router and add the handler:**

   Example content for `contacts.py`:

   ```python
   from aiogram import types
   from aiogram.dispatcher.router import Router

   router = Router()

   @router.message(types.ContentType.CONTACT)
   async def handle_contact(message: types.Message):
       contact = message.contact
       await message.answer(f"Received contact:\nName: {contact.first_name}\nPhone: {contact.phone_number}")
   ```

3. **Include the router in `handlers/__init__.py`:**

   Add your new router to the `routers` list:

   ```python
   from .start import router as start_router
   from .help import router as help_router
   from .contacts import router as contacts_router

   routers = [start_router, help_router, contacts_router]
   ```

4. **Run the bot:**

   Start your bot with:

   ```bash
   python main.py
   ```
---

## Adding More Commands

To add a new command (e.g., `/about`), repeat the process:

1. Create `handlers/about.py`:

   ```python
   from aiogram.types import Message
   from aiogram.filters import Command
   from aiogram.dispatcher.router import Router

   router = Router()

   @router.message(Command("about"))
   async def about_handler(message: Message):
       await message.answer("This is the About command.")
   ```

2. Add the router to `handlers/__init__.py`:
    add router name in `[ ]`

---

## License

This repository is open source under the MIT license. Feel free to use and modify it as needed!
