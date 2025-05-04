import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
from rich import print

def tweet_length_draw_charts():
  folder_path = "src/dataset/formated"
  output_path = "src/modules/tweet_length/charts/tweet_length_boxplot.svg"

  data = []
  for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
      candidate = filename.replace(".json", "")
      with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
        tweets = json.load(f)
        for tweet in tweets:
          data.append({
            "candidate": candidate,
            "length": len(tweet["content"])
          })

  df = pd.DataFrame(data)
  df_sample = df.sample(frac=0.1, random_state=42)

  custom_palette = {
    '2016_clinton': '#ACCBFF',
    '2016_trump': '#FF9797',
    '2020_trump': '#FF5733',
    '2020_biden': '#3380FF'
  }
  order = ['2020_biden', '2020_trump', '2016_clinton', '2016_trump']
  pretty_labels = ['J. Biden 2020', 'D. Trump 2020', 'H. Clinton 2016', 'D. Trump 2016']

  plt.figure(figsize=(12, 8))
  ax = sns.boxplot(
    hue="candidate",
    legend=False,
    x="candidate",
    y="length",
    data=df_sample,
    palette=custom_palette,
    width=0.4,
    showfliers=False,
    order=order
  )

  ax.set_xticks(ax.get_xticks())
  ax.set_xticklabels(pretty_labels)

  handles = []
  for candidate_key, label in zip(order, pretty_labels):
    patch = mpatches.Patch(color=custom_palette[candidate_key], label=label)
    handles.append(patch)
  ax.legend(handles=handles, title="Candidat", loc='upper right')

  plt.ylim(df_sample["length"].min() - 10, df_sample["length"].max() + 10)

  plt.ylabel("Longueur du tweet (en caractères)")
  plt.xlabel("Candidat")

  plt.tight_layout()
  os.makedirs(os.path.dirname(output_path), exist_ok=True)
  plt.savefig(output_path, format='svg')
  plt.close()

  print(f"📊 [green]{output_path} généré avec succès ![/green] ")
