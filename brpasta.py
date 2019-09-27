###         Inicio Idioma
print("Choose your language: pt or en")
var_idioma = input("Language: ")
var_idiomack = False
if var_idioma.lower() == "en":
  var_idiomack = True
  # print("English")
elif var_idioma.lower() == "pt":
  var_idiomack = True
  # print("Português")
elif var_idiomack == False:
  print("This language is not valid")
  exit()

print("Language chosen: " + var_idioma.lower())
###         Fim Idioma

###         Inicio Categoria
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
elif var_categoria_ck == False:
  print("This category does not exists")
  exit()

print("Category chosen: " + var_categoria.lower())
###         Fim Categoria

###         Inicio tamanho copypasta
cp_lenght: int
cp_size = input("Choose your copypasta lenght. It can be short, medium or large!")
cp_size_ck = False

if cp_size == "short":
  cp_lenght = 1000
  cp_min = 0
  cp_size_ck = True
elif cp_size == "medium":
  cp_lenght = 3000
  cp_min = 1200
  cp_size_ck = True
elif cp_size == "large":
  cp_lenght = 50000
  cp_min = 3500
  cp_size_ck = True
elif cp_size_ck == False:
  cp_lenght = 1000
  cp_min = 0
  print("Pequeno")
###         Fim tamanho copypasta


###         Inicio Busca o copypasta do reddit
import praw
import random

def busca_copy_pasta():
  reddit = praw.Reddit('brpasta')
  max_length = cp_lenght  # Maior que isso
  min_lenght = cp_min # Menor que isso
  copypasta_ck = False
  try:
    post = random.choice([x for x in reddit.subreddit('PastaPortuguesa').top("all", limit=None)])
    if len((post.selftext)) <= max_length and len((post.selftext)) > min_lenght: # Trata o tamanho do texto
      copypasta_ck = True
    if copypasta_ck:
      print((post.selftext))
      print(len((post.selftext)))
    elif not copypasta_ck:
      # Se não encontra, repete até encontrar
      busca_copy_pasta()

  except Exception as err:
    print(err)


busca_copy_pasta()

###         Fim Busca o copypasta do reddit
