# In the name of God


import os
from pack import frame, put_point

monitor = frame
xp, yp = 20, 5

for y in range(10):
    for x in range(y):
        monitor = put_point(x + xp, y + yp, chr(9608), monitor)


os.system("cls")
print(monitor)
