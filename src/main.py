import json
from modules.format_csv_datasets import format_tweets_csv_to_json

# Format CSV to Json
with open("src/config/format_config.json", encoding="utf-8") as f:
  formatMetas = json.load(f)
format_tweets_csv_to_json(formatMetas)