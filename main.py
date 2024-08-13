# In the name of God


from time import sleep
from pack import frame, put_point, clear_screen

monitor = frame
xp, yp = 40, 5

for y in range(0, 20):
    for x in range(0, y):
        monitor = put_point(x + xp, y + yp, chr(9608), monitor)
        clear_screen()
        print(monitor)
        sleep(0.02)
