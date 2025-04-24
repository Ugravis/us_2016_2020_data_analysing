import json
import os
import matplotlib.pyplot as plt
from rich import print

def tweet_quantity_evo_draw_charts():
  input_path = "src/modules/tweet_quantity_evo/results/tweet_quantity_evolution.json"
  output_path = "src/modules/tweet_quantity_evo/charts/tweet_quantity_evolution_may_oct.svg"

  with open(input_path, "r", encoding="utf-8") as file:
    data = json.load(file)

  months = ['05', '06', '07', '08', '09', '10']
  month_labels = ['Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct']
  colors = {
    '2016_clinton': '#ACCBFF',
    '2016_trump': '#FF9797',
    '2020_trump': '#FF5733',
    '2020_biden': '#3380FF'
  }

  plt.figure(figsize=(12, 6))

  for candidate, values in data.items():
    monthly_counts = { month: 0 for month in months }

    for period, count in values["tweet_counts"].items():
      month = period.split('-')[1]

      if month in monthly_counts:
        monthly_counts[month] += count
    
    # Ignorer les mois avec 0 tweets
    filtered_months = [month for month in months if monthly_counts[month] > 0]
    filtered_counts = [monthly_counts[month] for month in months if monthly_counts[month] > 0]

    candidate_color = colors.get(candidate, 'grey')  # Gris par défaut, si aucune couleur n'est indiquée

    if filtered_counts: 
      filtered_labels = [month_labels[months.index(m)] for m in filtered_months]
      plt.plot(filtered_labels, filtered_counts, marker='o', label=candidate, color=candidate_color, linewidth=2)

  plt.xlabel("Mois (toutes années confondues)")
  plt.ylabel("Nombre de tweets")
  plt.title("Quantité de tweets par mois pour chacun des candidats")
  plt.legend()
  plt.tight_layout()

  plt.savefig(output_path)
  plt.close()
  print(f"📊 [green]{output_path}[/green]")