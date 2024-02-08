import random 

my_list = [6, 9, 80, 3, 7, 4]
 
print(my_list)
cislo = random.choice(my_list)
print(cislo)
odpoved = input()
if my_list[int(odpoved)] == cislo:
   print("das ist gut")
else:
   print("das ist spate gut")



