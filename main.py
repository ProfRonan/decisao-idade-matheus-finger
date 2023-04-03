numero = int(input())

cond1 = False
cond2 = False
cond3 = False
cond4 = False

if numero < 0:
  print("impossível!")
  cond1 = True
if numero < 18:
  print("não precisa se alistar.")
  cond2 = True
if 18 < numero < 65:
  print("Não esqueça de votar na próxima eleição.")
  cond3 = True
if numero > 65:
  print("Vá descansar.")
  cond4 = True
if not (cond1 or cond2 or cond3 or cond4):
  print("eita!")