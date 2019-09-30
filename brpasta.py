import praw
import random

# Caso seja necessário adicionar um novo idioma ou subreddit, adicionar aqui
SUBREDDITS = {
  "pt": "PastaPortuguesa",
  "en": "copypasta",
  "emoji": "emojipasta"
}

# Filtra os posts de acordo com o necessário
def filtrar_posts(post):
  return post.selftext.strip()

# Busca uma copypasta no reddit
def busca_copy_pasta(var_idioma):
  # Busca os 100 primeiros posts do Hot do subreddit selecionado
  reddit = praw.Reddit('brpasta')
  posts = reddit.subreddit(SUBREDDITS[var_idioma]).top(limit=100)

  # Filtra todos os posts que não tem texto vazio
  filtered_posts = list(filter(filtrar_posts, list(posts)))

  if len(filtered_posts) == 0:
    return 'No pasta found'
  else:
    # Retorna post aleatório
    return random.choice(filtered_posts).selftext

try:
  # Input de idioma
  print("Choose your language: pt (portuguese) or en (english) or type anything for a surprise!")
  var_idioma = input("Language: ").lower().strip()

  # Caso não encontre o idioma na constante de subreddits, força usar emoji
  if not var_idioma in SUBREDDITS:
    var_idioma = "emoji"

  print(busca_copy_pasta(var_idioma))

except Exception as err:
  print(err)
