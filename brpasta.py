# print("Bem vindo ao CopyPasta Finder Simulator 3001!"
#       + "\nAqui você escolhe a resposta pronta para as perguntas ou discussões chatas pakarai!")
# catg = ["0", "Drogas", "Política", "Jogos", "Foda-se"]
# selcat = int(input("Por favor, escolha sua categoria abaixo:"
#                    + "\n 1 - Drogas\n 2 - Política\n 3 - Jogos\n 4 - Foda-se\n"))

# if selcat == 0:
#     print("Oi zero")
# elif selcat != 0:
#     print("Muito bem! Você selecionou: " + catg[1])

# Busca o copypasta do reddit
import praw
import random
from six.moves import urllib

def busca_copy_pasta():
  reddit = praw.Reddit('brpasta')

  try:
    post = random.choice([x for x in reddit.subreddit('PastaPortuguesa').top("all", limit=1)])
    print(post.selftext)
  except Exception as err:
    print(err)

busca_copy_pasta()
