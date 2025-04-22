import json
from modules.format_csv_datasets.format_csv_datasets import format_tweets_csv_to_json
from modules.most_used_words.most_used_words import mostUsedWords

with open("src/config/format_config.json", encoding="utf-8") as f:
  formatMetas = json.load(f)

# Format CSV to Json
format_tweets_csv_to_json(formatMetas)

# Get most used words
mostUsedWords()


################ Graph test ################ Graph test ################


import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

with open('src/dataset/results/most_used_words.json', 'r') as file:
    data = json.load(file)

part_names = [name.replace('.json', '') for name in data.keys()]

# 1 graph pour chaque partie du json

for part_name in part_names:
    words = list(data[f"{part_name}.json"].keys())
    counts = [data[f"{part_name}.json"][word]['count'] for word in words]
    retweet_indices = [data[f"{part_name}.json"][word]['retweet_index'] for word in words]
    
    width = 0.4 # width barres
    
    # Creation graph
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(words)) # Position barres sur axe y

    # Index de retweet
    norm = Normalize(vmin=0, vmax=1)
    cmap = cm.get_cmap('Reds')
    colors = [cmap(norm(retweet)) for retweet in retweet_indices]
    
    # Affichage des barres
    ax.barh(y, counts, width, label='Occurrences', color=colors)

    # Labels / titres
    ax.set_xlabel('Occurrences')
    ax.set_ylabel('Mots')
    ax.set_title(f'Données pour {part_name}')

    # Ordre décroissant des occurences
    ax.invert_yaxis()
    
    ax.set_yticks(y)
    ax.set_yticklabels(words)
    
    # Légende pour la colorimétrie du retweet-index
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Retweet Index')
    
    # Sauvegarde finale en .svg
    plt.savefig(f"src/dataset/results/graphs/{part_name}.svg")
