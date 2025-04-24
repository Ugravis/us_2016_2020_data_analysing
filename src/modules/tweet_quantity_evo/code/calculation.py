import json
import os
from rich import print
from dateutil import parser
from collections import defaultdict

def tweet_quantity_evo_calculation():
  input_dir = "src/dataset/formated"
  output_path = "src/modules/tweet_quantity_evo/results/tweet_quantity_evolution.json"
  result = { }

  for file_name in os.listdir(input_dir):
    if not file_name.endswith('.json'):
      continue

    candidate = file_name.replace('.json', '')
    filepath = os.path.join(input_dir, file_name)

    with open(filepath, 'r', encoding='utf-8') as f:
      try:
        tweets = json.load(f)
      except json.JSONDecodeError as e:
        print(f"[red]Erreur dans le fichier {file_name} : {e}[/red]")
        continue

    tweet_counts = defaultdict(int)
    dates = []

    for tweet in tweets:
      try:
        tweet_date = parser.isoparse(tweet["date"])
      except Exception as e:
        print(f"[yellow]Date invalide dans {file_name} : {e}[/yellow]")
        continue

      if tweet_date.month == 11:
        continue

      period_key = tweet_date.strftime("%Y-%m")
      tweet_counts[period_key] += 1
      dates.append(tweet_date)

    valid_dates = [d for d in dates if d.month != 10]

    if valid_dates:
      start = min(valid_dates).strftime('%Y-%m-%d')
      end = max(valid_dates).strftime('%Y-%m-%d')
    else:
      start = end = None

  # Ecriture du resultat

    result[candidate] = {
      "time_amplitude": {
        "start": start,
        "end": end
      },
      "tweet_counts": {
        k: tweet_counts[k]
        for k in sorted(tweet_counts.keys())
      }
    }

  with open(output_path, 'w', encoding='utf-8') as out_file:
    json.dump(result, out_file, indent=2, ensure_ascii=False)

  print(f"💾 [green]{output_path}[/green]")