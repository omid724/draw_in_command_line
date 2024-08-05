# In the name of God


import os
import platform


width, height, target_char = 100, 40, chr(9608)

line = target_char * width + "\n"
body = target_char + " " * (width - 2) + target_char + "\n"
body = body * (height - 2)

frame = line + body + line


def put_point(x, y, harf, page):
    if 0 > x or x >= width - 1 or 0 > y or y >= height - 1:
        return page

    tedad_char = ((width + 1) * (y + 1)) + (x + 1)
    return page[:tedad_char] + harf + page[tedad_char + 1 :]


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
