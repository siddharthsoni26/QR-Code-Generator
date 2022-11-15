#importing required lib
import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1, error_correction=qrcode.ERROR_CORRECT_H,
box_size=10, border = 4,)

#URL to QR Generating process
qr_url = input("Enter url to convert: ")
qr.add_data(qr_url)

qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img_savingname = input("Enter file name to save QR Code:")
#QR Code is saved in project file
img.save(f"{img_savingname}.png")
