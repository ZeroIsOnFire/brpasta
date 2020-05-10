import os
import io
import praw
import random
import discord
import aiohttp
from dotenv import load_dotenv
from discord.ext import commands
from textwrap import wrap

MAX_CHARACTERS = 2000
MAX_PASTAS = 100

SUBREDDITS = {
  "pt": "PastaPortuguesa",
  "en": "copypasta",
  "emoji": "emojipasta"
}

AI_SOURCES = {
  "waifu": "https://www.thiswaifudoesnotexist.net"
}

PASTA_HELP_MESSAGE='''
  Responds with a copypasta from reddit.
  Receives language as parameters, with 'en', 'pt' and 'emoji' as options, default as 'en' and
  if you type anything, it changes to 'emoji'
'''.strip()

# Configurações de ambiente
load_dotenv()

# Configurações do discord
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'))

# Configurações do Reddit
reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent=os.getenv('REDDIT_AGENT'))

# Filtra os posts de acordo com o necessário
def filtrar_posts(post):
  return post.selftext.strip()

# Busca uma copypasta no reddit
def busca_copy_pasta(var_idioma):
  if not var_idioma in SUBREDDITS:
    var_idioma = "emoji"

  # Busca os 100 primeiros posts do Hot do subreddit selecionado
  posts = reddit.subreddit(SUBREDDITS[var_idioma]).hot(limit=MAX_PASTAS)

  # Filtra todos os posts que não tem texto vazio
  filtered_posts = list(filter(filtrar_posts, list(posts)))

  if len(filtered_posts) == 0:
    return 'No pasta found'
  else:
    # Retorna post aleatório
    return random.choice(filtered_posts).selftext

# Busca a foto de AI em uma source
async def buscar_ai(source):
  if not source in AI_SOURCES:
    source = "artwork"

  async with aiohttp.ClientSession() as session:
    if source == 'waifu':
      id = random.randint(0,100000)
      url = f'https://www.thiswaifudoesnotexist.net/example-{id}.jpg'

      async with session.get(url) as resp:
        if resp.status != 200:
          raise Exception('Request Failed', f'Request failed for {source}')
        else:
          return {
            "raw": io.BytesIO(await resp.read()),
            "name": "waifu.jpg"
          }
    else:
      return { "raw": '', "name": ''}

# Ao conectar no discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready to shitpost!')

# Recebe comando de busca de pasta
@bot.command(name='pasta', help=PASTA_HELP_MESSAGE)
async def summon_pasta(message, language='en'):
  try:
    pasta = busca_copy_pasta(language)
    chunks = wrap(pasta, MAX_CHARACTERS)
    # Imprime as mensagens em chunks de 2000, por causa de limitações do discord
    for chunk in chunks:
      await message.send(chunk)
  except Exception as err:
    print(err)
id
# Recebe comando de foto de item não existente aleatorio
@bot.command(name='ai', help=PASTA_HELP_MESSAGE)
async def summon_ai_picture(message, source='artwork'):
  try:
    data = await buscar_ai(source)
    picture = discord.File(data["raw"], data["name"])
    await message.send(file=picture)
  except Exception as err:
    print(err)
    await message.send('Sorry, I failed :(')

bot.run(token)
