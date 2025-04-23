import json
import os
import matplotlib.pyplot as plt
import numpy as np
from rich import print
from matplotlib import cm
from matplotlib.colors import Normalize

def most_used_words_draw_charts():
  results_dir = 'src/modules/most_used_words/results/'
  charts_dir = 'src/modules/most_used_words/charts/'

  # S'assurer que le dossier charts existe
  os.makedirs(charts_dir, exist_ok=True)

  # Lister tous les fichiers JSON dans le dossier results
  json_files = [f for f in os.listdir(results_dir) if f.endswith('.json')]

  for json_file in json_files:
    part_name = json_file.replace('.json', '')

    with open(os.path.join(results_dir, json_file), 'r') as file:
      data = json.load(file)

    words = list(data.keys())
    counts = [data[word]['count'] for word in words]
    retweet_indices = [data[word]['retweet_index'] for word in words]

    width = 0.4
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(words))

    norm = Normalize(vmin=0, vmax=1)
    cmap = cm.get_cmap('Reds')
    colors = [cmap(norm(r)) for r in retweet_indices]

    ax.barh(y, counts, width, color=colors)
    ax.set_xlabel('Occurrences')
    ax.set_ylabel('Mots')
    ax.set_title(f'Données pour {part_name}')
    ax.invert_yaxis()
    ax.set_yticks(y)
    ax.set_yticklabels(words)

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Retweet Index')

    plt.savefig(os.path.join(charts_dir, f'{part_name}.svg'))
    plt.close(fig)  # Fermer pour économiser la mémoire

    print(f"📊 [green]{charts_dir}{part_name}.svg[/green]")