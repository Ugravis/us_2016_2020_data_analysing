from datetime import datetime, timezone

def clean_string(string):
  """
  Nettoyage des textes
  """

  clean_string = string.replace('"', "'")
  clean_string = clean_string.replace('\n', ' ').replace('\r', '').strip()
  return clean_string

def parse_iso8601(date_str):
  """
  Conversion date ISO 8601 en datetime UTC
  """

  dt = datetime.strptime(date_str[:-6], "%Y-%m-%dT%H:%M:%S")
  return dt.replace(tzinfo=timezone.utc)