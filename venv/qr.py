# pip install qrcode
# Importing library
import qrcode
import image

qr = qrcode.QRCode(
     version = 1,
     error_correction = qrcode.constants.ERROR_CORRECT_L,
     box_size = 10,
     border = 4
)

qr.add_data("https://github.com/kallyas/cit-assignment/fork")

img = qr.make_image(fill_color = "black", back_color = "white")
img.save("qrcode.jpg")