import random 

class Animal:
   def __init__(self, name, color):
      self.name = name
      self.color = color

   def animals_namecolor(self):
      print("ja jsem " + self.name + " a moje barva je " + self.color)

koza = Animal("koza", "bila")
ryba = Animal("ryba", "ruzova")
zirafa = Animal("zirafa", "hnedo zluta")

random_kotrmelce = random.choice([koza, ryba, zirafa])
random_kotrmelce.animals_namecolor() 
 