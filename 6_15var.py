from turtle import *
k = 10000
color('black', 'red')
speed(1000)
lt(90)
pendown()
begin_fill()
for count in range(12):
    right(60)
    forward(2*k)
    right(60)
    forward(2*k)
    right(270)
end_fill()
cnt = 0
canvas = getcanvas()
for x in range(-k*k, k*k, k):
    for y in range(-k*k, k*k, k):
        s = canvas.find_overlapping(x, y, x, y)
        if len(s) == 1 and s[0] == 5:
            cnt += 1
print(cnt)
done()
exit()
