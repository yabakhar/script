import os
import urllib.request
j = "/watch?v=LgB3j2y1b-4&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=1,/watch?v=nfNBdD85ouQ&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=2,/watch?v=M2OyRnysdKs&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=3,/watch?v=F2fep13NHrM&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=4,/watch?v=JpRrX8JqJts&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=5,/watch?v=qgvIXnxef1o&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=6,/watch?v=o9sMJo0f5Us&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=7,/watch?v=IQ3JiRnrz_0&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=8,/watch?v=lP9ViELPevQ&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=9,/watch?v=YKBaqjOkXQY&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=10,/watch?v=mQAtChtLVw4&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=11,/watch?v=e8KH_KSZgpE&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=12,/watch?v=QNcZzVlwud0&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=13,/watch?v=D0uPMSKSDLs&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=14,/watch?v=NSjwNRG7HXY&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=15,/watch?v=gKys2o1E03w&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=16,/watch?v=rsdAetH-qIU&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=17,/watch?v=gMgOvDDfpDo&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=18,/watch?v=7La_xIFiLUc&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=19,/watch?v=Od120Wf-xoI&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=20,/watch?v=Zl2SuItvGmM&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=21,/watch?v=v1p_ILHiZ1E&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=22,/watch?v=rfJ4kbZ8-gM&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=23,/watch?v=4HxdSe6IEpk&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=24,/watch?v=XnK4Fb2T1PY&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=25,/watch?v=v1YR-yPWl28&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=26,/watch?v=aIx8Ll3HM5A&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=27,/watch?v=0-QOXHXnqfQ&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=28,/watch?v=wV3ERspLo9U&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=29,/watch?v=uhTwmDRbRTo&list=PLtFbQRDJ11kEjXWZmwkOV-vfXmrEEsuEW&index=30"

l = j.split(",")
youtube = "https://www.youtube.com"
d = []
i = 0

while (i < len(l)):
    d.append(youtube+l[i])
    i = i + 1

i = 27

while (i < len(l)):
    youtube = pytube.YouTube(d[i])
    video = youtube.streams.get_highest_resolution()
    video.download('.')
    i = i + 1