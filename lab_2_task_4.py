f1 = 1
f2 = 1
n  = int(input())
i = 0
print(1, 1,  sep = ' ', end=' ' )
while i < n-2:
  f = f1 + f2
  print(f)
  f1 = f2
  f2 = f
  i += 1