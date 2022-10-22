x = int(input())
r = int(x ** 0.5)
for d in range(2, r + 1):
  while x % d == 0:
    print(d, end=' ')
    x //= d
if x != 1:
  print(x)
  