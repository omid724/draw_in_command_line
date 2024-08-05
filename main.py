# In the name of God


import os
from time import sleep
from pack import frame, put_point, clear_screen

monitor = frame
xp, yp = 5, 5

for y in range(0, 10):
    for x in range(0, 10):
        monitor = put_point(x + xp, y + yp, chr(9608), monitor)
        clear_screen()
        print(monitor)
        sleep(0.2)
