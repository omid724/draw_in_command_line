# In the name of God

from time import sleep

from pack import clear_screen, CliRobot


robot = CliRobot()

xp, yp = 40, 0
m = 50

for y in range(0, m):
    for x in range(0, y):
        robot.put_point(x + xp, y + yp)
        clear_screen()
        print(robot.page)
        sleep(0.01)

for y in range(0, m):
    for x in range(-1, -y - 1, -1):
        robot.put_point(x + xp, y + yp)
        clear_screen()
        print(robot.page)
        sleep(0.01)

for y in range(0, m):
    for x in range(-1, +y - 1 - m, -1):
        robot.put_point(x + xp, y + yp + m)
        clear_screen()
        print(robot.page)
        sleep(0.01)

for y in range(0, m):
    for x in range(0, m - y):
        robot.put_point(x + xp, y + yp + m)
        clear_screen()
        print(robot.page)
        sleep(0.01)
