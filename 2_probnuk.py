print('x y z w')
for x in range(2):
  for y in range(2):
    for z in range(2):
      for w in range(2):
        if ((not y or x) == (x or w)) and (x or y):
          print(x, y, z, w)