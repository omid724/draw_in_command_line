# In the name of God


width, height, target_char = 100, 40, chr(9608)

line = target_char * width + "\n"
body = target_char + " " * (width - 2) + target_char + "\n"
body = body * (height - 2)

frame = line + body + line


def put_point(x, y, harf, page):
    if 0 >= x or x >= width or 0 >= y or y >= height:
        return page
    
    tedad_char = ((width + 1) * (y + 1)) + (x + 1)
    return page[:tedad_char] + harf + page[tedad_char+1:]
