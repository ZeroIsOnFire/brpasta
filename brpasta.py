import praw
import random

subreddit_map = {
  "pt": "PastaPortuguesa",
  "en": "copypasta",
  "emoji": "emojipasta"
}

# Busca uma copypasta no reddit
def busca_copy_pasta(var_idioma):
  reddit = praw.Reddit('brpasta')

  try:
    # Procura de qualquer jeito (mais rapido)
    posts = reddit.subreddit(subreddit_map[var_idioma]).hot()
    postlist = list(posts)
    post = random.choice(postlist)
    text = post.selftext

    if not text.strip():
      busca_copy_pasta(var_idioma)
    else:
      print(text)

  except Exception as err:
    print("Erro: " + err)

# Input de lingua
print("Choose your language: pt (portuguese) or en (english) or type anything for a surprise!")
var_idioma = input("Language: ").lower().strip()
if var_idioma.lower() != "en" and var_idioma.lower() != "pt":
  var_idioma = "emoji"

busca_copy_pasta(var_idioma)

# dump
"""
###     Inicio Categoria
if var_idioma_ck:
  var_categoria = input("Choose category: drugs, politics, memes, random, mock, compliment, menace, sorry: ")
  var_categoria_ck = False
  var_categoria_cod: int

  if var_categoria.lower() == "drugs":
    var_categoria_ck = True
    var_categoria_cod = 1
  elif var_categoria.lower() == "politics":
    var_categoria_ck = True
    var_categoria_cod = 2
  elif var_categoria.lower() == "memes":
    var_categoria_ck = True
    var_categoria_cod = 3
  elif var_categoria.lower() == "random":
    var_categoria_ck = True
    var_categoria_cod = 4
  elif var_categoria.lower() == "mock":
    var_categoria_ck = True
    var_categoria_cod = 5
  elif var_categoria.lower() == "compliment":
    var_categoria_ck = True
    var_categoria_cod = 6
  elif var_categoria.lower() == "menace":
    var_categoria_ck = True
    var_categoria_cod = 7
  elif var_categoria.lower() == "sorry":
    var_categoria_ck = True
    var_categoria_cod = 8
  elif not var_categoria_ck:
    print("This category does not exists")
    exit()

  print("Category chosen: " + var_categoria.lower())
###     Fim Categoria
"""

"""
# insere SQL
pw = 1 #Senha do Banco
import pyodbc
conn = pyodbc.connect(
 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=BD_TESTE;UID=SA;PWD='+pw+';')
cursor = conn.cursor()
cursor.execute('INSERT INTO BD_TESTE.dbo.PASTAS (TEXTO) VALUES (' + "'" + (post.selftext).replace("'", "") + "'" + ')')
conn.commit()
"""
