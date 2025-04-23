from rich import print
from pathlib import Path
import csv
import json
from datetime import datetime, timezone
from utils.functions.basics import clean_string, parse_iso8601

def format_tweets_csv_to_json(formatMetas):
  """
  Formate les data CSV selon les paramètres fournis dans le fichier de configuration (formatMetas)
  """

  print("[bold underline green]Modules: format csv datasets[/bold underline green]")

  for formatMeta in formatMetas:
    filtered_data = []

    csv_file_path = formatMeta["csv_file_path"]
    json_file_path = formatMeta["json_file_path"]
    date_row = formatMeta["date_row"]
    date_format = formatMeta["date_format"]
    start_range_date = parse_iso8601(formatMeta["start_date"])
    end_range_date = parse_iso8601(formatMeta["end_date"])
    filters = formatMeta.get("filters", [])

    # Suppression des rows inutiles et standardisation des noms de row
    row_mappings = {r["name"]: r["rename"] for r in formatMeta["rows"]}

    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
      reader = csv.DictReader(csv_file)

      for row in reader:
        try:
          # Filtre date
          raw_date_str = row[date_row]
          tweet_date = datetime.strptime(raw_date_str, date_format).replace(tzinfo=timezone.utc)
          if not (start_range_date <= tweet_date <= end_range_date):
            continue
          normalized_date_str = tweet_date.isoformat().replace("+00:00", "Z")

          # Filtres conditionnels
          should_include = True
          for f in filters:
            if row.get(f["row"]) != f["mustBe"]:
              should_include = False
              break
          if not should_include:
            continue
          
          # Formatage des str
          cleaned_row = {}
          for initial_key, new_key in row_mappings.items():
            value = row.get(initial_key)
            if isinstance(value, str):
              value = clean_string(value)
            
            # Conversion de retweetCount en int
            if new_key == "retweetCount":
              try:
                  value = int(value)
              except:
                  value = 0

            if new_key == "date": 
              value = normalized_date_str

            cleaned_row[new_key] = value

          filtered_data.append(cleaned_row)

        except Exception as e:
          print(f"[red]Error on row:[/red] {e}")
          continue

    Path(json_file_path).parent.mkdir(parents=True, exist_ok=True)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
      json.dump(filtered_data, json_file, indent=2, ensure_ascii=False)

    print(f"📂 [green]{json_file_path}[/green] [bold cyan][{len(filtered_data)} tweets][/bold cyan]")