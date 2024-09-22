# In the name of God


import os
import platform


def what_is_the_os_type():
    os_type = platform.system()

    if os_type.lower() == "darwin":
        # it returns 'mac'
        return "mac"
    else:
        # it returns 'windows' or 'linux'
        return os_type.lower()


def clear_screen():
    if what_is_the_os_type() == "linux":
        clear_cmd = "clear"
    else:
        clear_cmd = "cls"
    os.system(clear_cmd)


class CliRobot:
    def __init__(self, width=80, height=50, target_char=chr(9608)):
        self.width, self.height, target_char = width, height, target_char

        line = target_char * self.width + "\n"
        body = target_char + " " * (self.width - 2) + target_char + "\n"
        body = body * (self.height - 2)

        frame = line + body + line

        self.x, self.y = 0, 0
        self.page = frame
    

    def put_point(self, x, y, harf=chr(9608)):
        if 0 <= x < (self.width - 1) and 0 <= y < (self.height - 1):
            tedad_char = ((self.width + 1) * (y + 1)) + (x + 1)
            self.page = self.page[:tedad_char] + harf + self.page[tedad_char + 1 :]
    