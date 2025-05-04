import json
import os
from rich import print
from utils.functions.basics import tokenize_text
from collections import Counter, defaultdict

def most_used_words_calculation():
  """
  ###
  """
  
  input_dir = 'src/dataset/formated'
  output_dir = 'src/modules/most_used_words/results/'
  result = {}

  for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
      file_path = os.path.join(input_dir, filename)
      file_name_without_extension = filename.replace('.json', '')
      
      with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

      all_words = []
      tweet_count_with_word = defaultdict(int)
      total_retweets_for_word = defaultdict(int)

      # Mise en forme

      for tweet in data:
        if 'content' not in tweet or 'retweetCount' not in tweet:
          print(f"[red]Error in most_used_words: rows content or retweetCount are missing for: {tweet}[/red]")
          continue

        words = tokenize_text(tweet['content'])
        unique_words = set(words)
        all_words.extend(words)

        # Préparation pour retweet-index

        for word in unique_words:
          tweet_count_with_word[word] += 1
          total_retweets_for_word[word] += tweet['retweetCount']

      # Top des mots

      words_counts = Counter(all_words)
      top_words = words_counts.most_common(15)

      # Calcul du ratio des retweets par tweet

      ratios = [
        total_retweets_for_word[word] / tweet_count_with_word[word]
        for word, _ in top_words
        if tweet_count_with_word[word] > 0
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
        word: {
            "count": count,
            "retweet_index": normalize_ratio(total_retweets_for_word[word] / tweet_count_with_word[word])
        }
        for word, count in top_words
        if tweet_count_with_word[word] > 0
      }

    # Écriture du résultat en json

    output_file = os.path.join(output_dir, f"{file_name_without_extension}_most_used_words.json")
    with open(output_file, 'w', encoding='utf-8') as out_file:
      json.dump(result[filename], out_file, indent=2, ensure_ascii=False)
      print(f"💾 [green]{output_file}[/green]")

  return result