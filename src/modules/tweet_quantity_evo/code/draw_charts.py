import json
import os
import matplotlib.pyplot as plt
from rich import print

def draw_chart(input_path, output_path, title, colors):
  
  with open(input_path, "r", encoding="utf-8") as file:
    data = json.load(file)

  months = ['05', '06', '07', '08', '09', '10']
  month_labels = ['Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct']

  plt.figure(figsize=(12, 8))

  for candidate, values in data.items():
    monthly_counts = { month: 0 for month in months }

    for period, count in values["tweet_counts"].items():
      month = period.split('-')[1]
      if month in monthly_counts:
        monthly_counts[month] += count

    filtered_months = [month for month in months if monthly_counts[month] > 0]
    filtered_counts = [monthly_counts[m] for m in filtered_months]

    candidate_color = colors.get(candidate, 'grey')

    if filtered_counts:
      filtered_labels = [month_labels[months.index(m)] for m in filtered_months]
      
      pretty_labels = {
        '2016_clinton': 'H. Clinton 2016',
        '2016_trump': 'D. Trump 2016',
        '2020_trump': 'D. Trump 2020',
        '2020_biden': 'J. Biden 2020'
      }

      plt.plot(
        filtered_labels,
        filtered_counts,
        marker='o',
        label=pretty_labels.get(candidate, candidate),
        color=candidate_color,
        linewidth=2
      )

  plt.xlabel("Mois")
  plt.ylabel("Nombre de tweets")
  plt.title(title)
  plt.legend()
  plt.tight_layout()
  plt.savefig(output_path)
  plt.close()

  print(f"📊 [green]{output_path}[/green]")

def tweet_quantity_evo_draw_charts():
  base_path = "src/modules/tweet_quantity_evo"
  results_dir = os.path.join(base_path, "results")
  charts_dir = os.path.join(base_path, "charts")
  os.makedirs(charts_dir, exist_ok=True)

  configs = [
    {
      "input": os.path.join(results_dir, "tweet_quantity_evolution_2016.json"),
      "output": os.path.join(charts_dir, "tweet_quantity_evolution_2016.svg"),
      "title": "Pour la campagne de 2016",
      "colors": {
        '2016_clinton': '#3380FF',
        '2016_trump': '#FF5733'
      }
    },
    {
      "input": os.path.join(results_dir, "tweet_quantity_evolution_2020.json"),
      "output": os.path.join(charts_dir, "tweet_quantity_evolution_2020.svg"),
      "title": "Pour la campagne de 2020",
      "colors": {
        '2020_biden': '#3380FF',
        '2020_trump': '#FF5733'
      }
    }
  ]

  for config in configs:
    draw_chart(
      input_path=config["input"],
      output_path=config["output"],
      title=config["title"],
      colors=config["colors"]
    )
