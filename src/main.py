import json
from modules.format_csv_datasets.format_csv_datasets import format_tweets_csv_to_json
from modules.most_used_words.most_used_words import make_most_used_words
from modules.most_used_hashtags.most_used_hashtags import make_most_used_hashtags
from modules.tweet_quantity_evo.tweet_quantity_evo import make_tweet_quantity_evo

with open("src/config/format_config.json", encoding="utf-8") as f:
  formatMetas = json.load(f)

# Format CSV to Json
format_tweets_csv_to_json(formatMetas)

# Make most used words
make_most_used_words()

# Make most used hashtags
make_most_used_hashtags()

# Tweet quantity evolution
make_tweet_quantity_evo()