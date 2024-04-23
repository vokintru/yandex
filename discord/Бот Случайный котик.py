import discord
import logging
import requests

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "" # вставь свой токен


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "кот" in message.content.lower():
            url = 'https://api.thecatapi.com/v1/images/search'
            response = requests.get(url)
            data = response.json()
            image_url = data[0]['url']
            await message.channel.send(image_url)
        elif "собака" in message.content.lower():
            url = "https://dog.ceo/api/breeds/image/random"
            response = requests.get(url)
            data = response.json()
            image_url = data["message"]
            await message.channel.send(image_url)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)