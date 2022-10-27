import qrcode
import os

data = 'www.google.com'

img = qrcode.make(data)

img.save(os.path.expanduser("~/Desktop/myqrcode.png"))