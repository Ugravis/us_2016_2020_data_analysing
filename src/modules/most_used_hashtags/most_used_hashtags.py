from rich import print
from .code.calculation import most_used_hashtags_calculation
from .code.draw_charts import most_used_hashtags_draw_charts

def make_most_used_hashtags():
  print("[bold underline green]Module: most used hashtags[/bold underline green]")
  most_used_hashtags_calculation()
  most_used_hashtags_draw_charts()