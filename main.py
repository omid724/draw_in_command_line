# In the name of God


import os
from pack import frame, put_point, what_is_the_os_type

monitor = frame
xp, yp = 5, 5

for y in range(0, 10):
    for x in range(0, 10):
        monitor = put_point(x + xp, y + yp, chr(9608), monitor)


if what_is_the_os_type() == "linux":
    os.system("clear")
else:
    os.system("cls")

print(monitor)
