x = int(input())
y = int(input())
if x % y == 0:
  print('делится')
  print(x / y)
else:
  print('Не делится')
  print(x % y)
  print(x // y)