import json
from modules.format_csv_datasets import format_tweets_csv_to_json
from modules.most_used_words import mostUsedWords

with open("src/config/format_config.json", encoding="utf-8") as f:
  formatMetas = json.load(f)

# Format CSV to Json
format_tweets_csv_to_json(formatMetas)

# Get most used words
mostUsedWords()