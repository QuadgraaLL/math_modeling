a, b, c = map(float, input().split())
if a < b + c and b < a + c and c < a + b:
  print('треугольник существует') 
  if a == b and b == c:
    print('треугольник равносторонний')
  elif a==b or b==c or a==c:
    print('равнобедренный')
  else:
    print('разносторонний')
else:
  print('треугольника нет')
  
