a, b, c = map(float, input().split())
D = b ** 2 - 4 * a * c
if D > 0:
  x1 =  (-b + D ** 0.5) / (2*a)
  x2 =  (-b - D ** 0.5) / (2*a)
  print(x1, x2)
if D == 0:
  print(-b / (2 * a))
if D < 0:
  print('Нет корней')