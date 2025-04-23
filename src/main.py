import json
from modules.format_csv_datasets.format_csv_datasets import format_tweets_csv_to_json
from modules.most_used_words.most_used_words import make_most_used_words

with open("src/config/format_config.json", encoding="utf-8") as f:
  formatMetas = json.load(f)

# Format CSV to Json
format_tweets_csv_to_json(formatMetas)

# Get most used words
make_most_used_words()