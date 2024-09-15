prime = []
prime.append(1)

for i in range(2, 51):
  count = 0
  for j in range(2, 51):
    if i%j==0:
      count += 1
  if count == 1:
    prime.append(i)

stop = " "
for elem in prime:
  print(elem, end = stop)