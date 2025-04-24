from rich import print
from .code.calculation import tweet_quantity_evo_calculation
from .code.draw_charts import tweet_quantity_evo_draw_charts

def make_tweet_quantity_evo():
  print("[bold underline green]Module: tweet quantity evolution[/bold underline green]")
  tweet_quantity_evo_calculation()
  tweet_quantity_evo_draw_charts()