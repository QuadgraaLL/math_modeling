b1 = float(input())
q = float(input())
n = int(input())
for i in range(1, n + 1):
  print(b1*q**(i - 1), end=' ')
  i += 1