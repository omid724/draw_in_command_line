# In the name of God


width, height, neviseh_safheh = 100, 40, chr(9608)

line = neviseh_safheh * width + "\n"
body = neviseh_safheh + " " * (width - 2) + neviseh_safheh + "\n"
body = body * (height - 2)

frame = line + body + line


def put_point(x, y, harf, page):
    tedad_char = ((width + 1) * (y + 1)) + (x + 1)
    return page[:tedad_char] + harf + page[tedad_char+1:]
