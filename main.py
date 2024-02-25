import discord
import os
import logging

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ID сообщения, на которое можно реагировать, чтобы добавить/удалить роль.
        self.role_message_id = int(os.getenv('ROLE_MESSAGE_ID'))
        # Каждый эмодзи связан с определенной ролью на сервере.
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): int(os.getenv('RED_ROLE_ID')),  # ID роли, связанной с эмодзи '🔴'.
            discord.PartialEmoji(name='🟡'): int(os.getenv('YELLOW_ROLE_ID')),  # ID роли, связанной с эмодзи '🟡'.
            discord.PartialEmoji(name='green', id=int(os.getenv('GREEN_EMOJI_ID'))): int(os.getenv('GREEN_ROLE_ID')),  # ID роли, связанной с эмодзи 'green'.
        }

        # Настройка системы логирования
        logging.basicConfig(level=logging.INFO)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        # Проверяем, что реакция добавлена к сообщению, которое мы отслеживаем.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Проверяем, что мы все еще находимся на сервере и он кэширован.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # Если эмодзи не та, которую мы отслеживаем, то выходим.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Проверяем, что роль все еще существует и действительна.
            return

        try:
            # Наконец, добавляем роль.
            await payload.member.add_roles(role)
        except discord.HTTPException as e:
            # Если мы хотим что-то сделать в случае ошибок, мы сделаем это здесь.
            logging.error(f"Не удалось добавить роль: {e}")

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        # Проверяем, что реакция удалена с сообщения, которое мы отслеживаем.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Проверяем, что мы все еще находимся на сервере и он кэширован.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # Если эмодзи не та, которую мы отслеживаем, то выходим.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Проверяем, что роль все еще существует и действительна.
            return

        # Для `on_raw_reaction_remove` полезная нагрузка не предоставляет `.member`,
        # поэтому мы должны получить участника сами из `.user_id` полезной нагрузки.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Проверяем, что участник все еще существует и действителен.
            return

        try:
            # Наконец, удаляем роль.
            await member.remove_roles(role)
        except discord.HTTPException as e:
            # Если мы хотим что-то сделать в случае ошибок, мы сделаем это здесь.
            logging.error(f"Не удалось удалить роль: {e}")


# Устанавливаем намерения по умолчанию и добавляем привилегированные намерения 'members'.
intents = discord.Intents.default()
intents.members = True

# Создаем экземпляр клиента с заданными намерениями.
client = MyClient(intents=intents)
# Запускаем бота с токеном, полученным из переменных окружения.
client.run(os.getenv('TOKEN'))
