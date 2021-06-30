import os

i = 1
c = 27533208
b = 27533208
while (i):
    os.system(f"curl https://stickershop.line-scdn.net/stickershop/v1/sticker/{c}/android/sticker.png -o {i}.png")
    i += 1
    c += 1
    os.system("wait")
    if (c == b):
        break