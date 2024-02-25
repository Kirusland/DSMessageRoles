# Discord Role Bot

## Описание

Этот проект представляет собой бота для Discord, написанного на Python с использованием библиотеки discord.py. Бот предназначен для управления ролями участников на сервере с помощью реакций на сообщения.

## Установка

1. Установите Python 3.6 или выше.
2. Установите библиотеку discord.py с помощью pip: `pip install discord.py`.
3. Клонируйте этот репозиторий на свой компьютер.
4. Заполните необходимые переменные окружения, такие как `ROLE_MESSAGE_ID`, `RED_ROLE_ID`, `YELLOW_ROLE_ID`, `GREEN_EMOJI_ID`, `GREEN_ROLE_ID` и `DISCORD_TOKEN`.

## Использование

Запустите бота, используя команду `python bot.py` (или `python3 bot.py`, в зависимости от вашей системы). Бот начнет слушать реакции на сообщение с ID `ROLE_MESSAGE_ID` и добавлять или удалять соответствующие роли.

## Лицензия

Все права защищены. Использование, копирование, изменение или распространение этого программного обеспечения в коммерческих целях запрещено без получения письменного разрешения от владельца авторских прав.