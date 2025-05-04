# 🇺🇸 2016 and 2020 US Presidential Elections - Data Analysing

Analysis of **tweets from candidates** in the 2016 and 2020 US presidential elections. Original dataset from [Kaggle.com]([frfr](https://www.kaggle.com)). Make with **`Python`**, **`CSV`** files and **`JSON`** files. 

This work is part of a research project on the polarization of political discourse during presidential campaigns since the rise of social media in the 2010s ([Pennetier, U. 2025. *D'un espace public à un espace polarisé ; les réseaux sociaux comme arène politique*](https://github.com/Ugravis/us_2016_2020_data_analysing)). 

> [!NOTE]
> **The reshearch is focused on:**  
> 
> \- *H. Clinton* tweets from 2016.  
> \- *D. Trump* tweets from 2016.  
> \- *J. Biden* tweets from 2020.  
> \- *D. Trump* tweets from 2020.

### Here are some examples of the results provided:
 
**Figure 1\.** Distribution of the length of each candidate's tweets:

![Aperçu](https://zupimages.net/up/25/18/dgh1.png)

**Figure 2\.** Donald Trump's most used words during the 2016 campaign: 

![Aperçu](https://zupimages.net/up/25/18/5ejj.png)

### Tree result:
```
usa_2012_2016_data_analysing
├─ Makefile
├─ requirements.txt
└─ src
   ├─ config
   │  └─ format_config.json
   ├─ dataset
   │  └─ original
   │     ├─ biden_tweets.csv
   │     ├─ clinton_trump_2016_tweets.csv
   │     └─ trump_tweets.csv
   ├─ main.py
   ├─ modules
   │  ├─ format_csv_datasets
   │  │  ├─ __init__.py
   │  │  └─ format_csv_datasets.py
   │  ├─ most_used_hashtags
   │  │  ├─ __init__.py
   │  │  ├─ charts
   │  │  │  ├─ 2016_clinton_most_used_hashtags.svg
   │  │  │  ├─ 2016_trump_most_used_hashtags.svg
   │  │  │  ├─ 2020_biden_most_used_hashtags.svg
   │  │  │  └─ 2020_trump_most_used_hashtags.svg
   │  │  ├─ code
   │  │  │  ├─ __init__.py
   │  │  │  ├─ calculation.py
   │  │  │  └─ draw_charts.py
   │  │  ├─ most_used_hashtags.py
   │  │  └─ results
   │  │     ├─ 2016_clinton_most_used_hashtags.json
   │  │     ├─ 2016_trump_most_used_hashtags.json
   │  │     ├─ 2020_biden_most_used_hashtags.json
   │  │     └─ 2020_trump_most_used_hashtags.json
   │  ├─ most_used_words
   │  │  ├─ __init__.py
   │  │  ├─ charts
   │  │  │  ├─ 2016_clinton_most_used_words.svg
   │  │  │  ├─ 2016_trump_most_used_words.svg
   │  │  │  ├─ 2020_biden_most_used_words.svg
   │  │  │  └─ 2020_trump_most_used_words.svg
   │  │  ├─ code
   │  │  │  ├─ __init__.py
   │  │  │  ├─ calculation.py
   │  │  │  └─ draw_charts.py
   │  │  ├─ most_used_words.py
   │  │  └─ results
   │  │     ├─ 2016_clinton_most_used_words.json
   │  │     ├─ 2016_trump_most_used_words.json
   │  │     ├─ 2020_biden_most_used_words.json
   │  │     └─ 2020_trump_most_used_words.json
   │  ├─ tweet_length
   │  │  ├─ __init__.py
   │  │  ├─ charts
   │  │  │  └─ tweet_length_boxplot.svg
   │  │  ├─ code
   │  │  │  ├─ __init__.py
   │  │  │  └─ draw_charts.py
   │  │  ├─ results
   │  │  └─ tweet_length.py
   │  └─ tweet_quantity_evo
   │     ├─ __init__.py
   │     ├─ charts
   │     ├─ code
   │     │  ├─ __init__.py
   │     │  ├─ calculation.py
   │     │  └─ draw_charts.py
   │     ├─ results
   │     │  ├─ tweet_quantity_evolution_2016.json
   │     │  └─ tweet_quantity_evolution_2020.json
   │     └─ tweet_quantity_evo.py
   └─ utils
      ├─ functions
      │  ├─ __init__.py
      │  └─ basics.py
      └─ resources
         ├─ __init__.py
         ├─ names_mapping.py
         └─ stopwords_en.py

```

*This work is carried out as part of a research project at **ESPOL, Université Catholique de Lille***. 

![Aperçu](https://zupimages.net/up/25/17/9zzo.jpg)

*Ulysse Pennetier*