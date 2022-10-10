f1 = 1
f2 = 1
n  = int(input())
i = 0
x = [1, 1]
while i < n-2:
  f = f1 + f2
  x.append(f)
  f1 = f2
  f2 = f
  i += 1
print(' '.join([str(i) for i in x]))