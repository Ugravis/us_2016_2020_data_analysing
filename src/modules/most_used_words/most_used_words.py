from rich import print
from .code.calculation import most_used_words_calculation
from .code.draw_charts import most_used_words_draw_charts

def make_most_used_words():
  print("[bold underline green]Module: most used words[/bold underline green]")
  most_used_words_calculation()
  most_used_words_draw_charts()