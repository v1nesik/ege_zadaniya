print('w x y z')
for w in range(2):
  for x in range(2):
    for y in range(2):
      for z in range(2):
        if (((not(x) or z) == (y and not(w))) <= (z and y)) == False:
          print(w, x, y, z)