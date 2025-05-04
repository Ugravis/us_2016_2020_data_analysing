import json
import os
import matplotlib.pyplot as plt
import numpy as np
from rich import print
from matplotlib import cm
from matplotlib.colors import Normalize

plt.rcParams.update({
  'axes.titlesize': 20,
  'axes.labelsize': 20,
  'xtick.labelsize': 20,
  'ytick.labelsize': 20
})

def most_used_words_draw_charts():
  """
  ###
  """

  results_dir = 'src/modules/most_used_words/results/'
  charts_dir = 'src/modules/most_used_words/charts/'

  title_mapping = {
    '2016_trump_most_used_words': 'Pour Donald Trump, 2016',
    '2020_trump_most_used_words': 'Pour Donald Trump, 2020',
    '2016_clinton_most_used_words': 'Pour Hillary Clinton, 2016',
    '2020_biden_most_used_words': 'Pour Joe Biden, 2020'
  }

  os.makedirs(charts_dir, exist_ok=True)

  json_files = [f for f in os.listdir(results_dir) if f.endswith('.json')]

  for json_file in json_files:
    part_name = json_file.replace('.json', '')
    title = title_mapping.get(part_name, f'Données pour {part_name}')  # Titre par défaut si non trouvé

    with open(os.path.join(results_dir, json_file), 'r') as file:
      data = json.load(file)

    words = list(data.keys())
    counts = [data[word]['count'] for word in words]
    retweet_indices = [data[word]['retweet_index'] for word in words]

    if 'trump' in part_name:
      cmap = cm.get_cmap('Reds')  
    else:
      cmap = cm.get_cmap('Blues') 

    width = 0.4
    fig, ax = plt.subplots(figsize=(12, 8))
    y = np.arange(len(words))

    norm = Normalize(vmin=0, vmax=1)
    colors = [cmap(norm(r)) for r in retweet_indices]

    ax.barh(y, counts, width, color=colors)
    ax.set_xlabel('Occurrences')
    ax.set_ylabel('Mots')
    ax.set_title(title)  
    ax.invert_yaxis()
    ax.set_yticks(y)
    ax.set_yticklabels(words)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Retweet Index')

    # Save
    plt.savefig(os.path.join(charts_dir, f'{part_name}.svg'))
    plt.close(fig)  

    print(f"📊 [green]{charts_dir}{part_name}.svg[/green]")

