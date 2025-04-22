from datetime import datetime, timezone
from modules.stopwords_en import STOP_WORDS
from modules.names_mapping import NAMES_MAPPING
import re
import html

def clean_string(string):
  """
  Nettoyage des textes: suppression des sauts de ligne, remplacement de " par '.

  Args:
    string (str): texte à nettoyer.

  Returns:
    string: texte nettoyé.
  """

  string = re.sub(r"&amp[, ]", "&", string) 
  string = re.sub(r"https://t\.co/\S+", "", string)
  string = html.unescape(string) 
  clean_string = string.replace('"', "'")
  clean_string = clean_string.replace('\n', ' ').replace('\r', '').strip()
  return clean_string

def parse_iso8601(date_str):
  """
  Conversion d'une date ISO 8601 en datetime UTC.

  Args:
    date_str (str): date iso à parser

  Returns:
    new_date: date UTC.
  """

  dt = datetime.strptime(date_str[:-6], "%Y-%m-%dT%H:%M:%S")
  return dt.replace(tzinfo=timezone.utc)

def tokenize_text(text):
  """
  Retourne une version tokenisée d'un texte: minuscules, plus de ponctuation. 

  Args: 
    text (str): texte à tokeniser.
  
  Returns: 
    list: tableau avec tous les mots normalisés du text. 
  """

  text = text.lower()

  for expression, replacement in NAMES_MAPPING.items():
    text = re.sub(r'\b' + re.escape(expression) + r'\b', replacement, text, flags=re.IGNORECASE)

  text = re.sub(r'http\S+|@\S+|#\S+|[^a-zàâçéèêëîïôûùüÿñæœ_]', ' ', text)  
  words = text.split()
  words = [word for word in words if word not in STOP_WORDS]

  return words