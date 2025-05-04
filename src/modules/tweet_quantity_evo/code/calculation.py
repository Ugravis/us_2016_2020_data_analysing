import json
import os
from rich import print
from dateutil import parser
from collections import defaultdict

def tweet_quantity_evo_calculation():
  input_dir = "src/dataset/formated"
  output_base = "src/modules/tweet_quantity_evo/results"
  result_2016 = {}
  result_2020 = {}

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

    data = {
      "time_amplitude": {
        "start": start,
        "end": end
      },
      "tweet_counts": {
        k: tweet_counts[k]
        for k in sorted(tweet_counts.keys())
      }
    }

    if "2016" in candidate:
      result_2016[candidate] = data
    elif "2020" in candidate:
      result_2020[candidate] = data

  # Écriture des résultats dans deux fichiers distincts
  output_2016 = os.path.join(output_base, "tweet_quantity_evolution_2016.json")
  output_2020 = os.path.join(output_base, "tweet_quantity_evolution_2020.json")

  with open(output_2016, 'w', encoding='utf-8') as f_2016:
    json.dump(result_2016, f_2016, indent=2, ensure_ascii=False)
    print(f"💾 [green]{output_2016}[/green]")

  with open(output_2020, 'w', encoding='utf-8') as f_2020:
    json.dump(result_2020, f_2020, indent=2, ensure_ascii=False)
    print(f"💾 [green]{output_2020}[/green]")
