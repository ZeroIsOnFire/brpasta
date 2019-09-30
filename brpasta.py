import os
import praw
import random
import discord
from dotenv import load_dotenv

# Caso seja necessário adicionar um novo idioma ou subreddit, adicionar aqui
SUBREDDITS = {
  "pt": "PastaPortuguesa",
  "en": "copypasta",
  "emoji": "emojipasta"
}

# Retorna uma instancia do reddit
def fetch_reddit_instance():
  return praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent=os.getenv('REDDIT_AGENT'))

# Filtra os posts de acordo com o necessário
def filtrar_posts(post):
  return post.selftext.strip()

# Busca uma copypasta no reddit
def busca_copy_pasta(var_idioma):
  # Busca os 100 primeiros posts do Hot do subreddit selecionado
  reddit = fetch_reddit_instance()
  posts = reddit.subreddit(SUBREDDITS[var_idioma]).top(limit=100)

  # Filtra todos os posts que não tem texto vazio
  filtered_posts = list(filter(filtrar_posts, list(posts)))

  if len(filtered_posts) == 0:
    return 'No pasta found'
  else:
    # Retorna post aleatório
    return random.choice(filtered_posts).selftext

try:
  load_dotenv()

  # Input de idioma
  print("Choose your language: pt (portuguese) or en (english) or type anything for a surprise!")
  var_idioma = input("Language: ").lower().strip()

  # Caso não encontre o idioma na constante de subreddits, força usar emoji
  if not var_idioma in SUBREDDITS:
    var_idioma = "emoji"

  print(busca_copy_pasta(var_idioma))

except Exception as err:
  print(err)
