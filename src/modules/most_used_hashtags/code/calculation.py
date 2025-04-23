import json
import os
from rich import print
from utils.functions.basics import tokenize_hashtags
from collections import Counter, defaultdict

def most_used_hashtags_calculation():
  """
  Retourne les mots les plus utilisés dans les tweets et ainsi qu'un retweet-index pour chacun des mots.
  Traite tous les fichiers JSON dans le répertoire src/dataset/formated.

  Returns:
      dict: Les mots les plus fréquents de chaque fichier avec leur fréquence et index de retweet normalisé.
  """
  
  input_dir = 'src/dataset/formated'
  output_dir = 'src/modules/most_used_hashtags/results/'
  result = {}

  for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
      file_path = os.path.join(input_dir, filename)
      file_name_without_extension = filename.replace('.json', '')
      
      with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

      all_hashtags = []
      tweet_count_with_hashtag = defaultdict(int)
      total_retweets_for_hashtag = defaultdict(int)

      # Mise en forme

      for tweet in data:
        if 'content' not in tweet or 'retweetCount' not in tweet:
          print(f"[red]Error in most_used_hashtags: rows content or retweetCount are missing for: {tweet}[/red]")
          continue

        hashtags = tokenize_hashtags(tweet['content'])
        unique_hashtags = set(hashtags)
        all_hashtags.extend(hashtags)

        # Préparation pour retweet-index

        for hashtag in unique_hashtags:
          tweet_count_with_hashtag[hashtag] += 1
          total_retweets_for_hashtag[hashtag] += tweet['retweetCount']

      # Top des mots

      hashtags_counts = Counter(all_hashtags)
      top_hashtags = hashtags_counts.most_common(15)

      # Calcul du ratio des retweets par tweet

      ratios = [
        total_retweets_for_hashtag[hashtag] / tweet_count_with_hashtag[hashtag]
        for hashtag, _ in top_hashtags
        if tweet_count_with_hashtag[hashtag] > 0
      ]
      if not ratios:
        print(f"[red]Erreur : Aucune donnée de retweet disponible pour normaliser l'index dans le fichier {filename}.[/red]")
        continue

      # Normalisation du ratio entre 0 et 1

      min_ratio = min(ratios)
      max_ratio = max(ratios)

      def normalize_ratio(x):
        if max_ratio == min_ratio:
          return 5.0
        return round((x - min_ratio) / (max_ratio - min_ratio), 4)

      # Mise en forme finale

      result[filename] = {
        hashtag: {
            "count": count,
            "retweet_index": normalize_ratio(total_retweets_for_hashtag[hashtag] / tweet_count_with_hashtag[hashtag])
        }
        for hashtag, count in top_hashtags
        if tweet_count_with_hashtag[hashtag] > 0
      }

    # Écriture du résultat en json

    output_file = os.path.join(output_dir, f"{file_name_without_extension}_most_used_hashtags.json")
    with open(output_file, 'w', encoding='utf-8') as out_file:
      json.dump(result[filename], out_file, indent=2, ensure_ascii=False)
      print(f"💾 [green]{output_file}[/green]")

  return result