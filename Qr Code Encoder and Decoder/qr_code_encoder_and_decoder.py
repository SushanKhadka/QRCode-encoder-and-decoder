import qrcode

qr = qrcode.QRCode(
    version = 15,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 5,
    border = 4
)

data = input("Enter the data to be encoded (eg. URL, texts etc) \n : ")

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "black", back_color="white")
img.save("qrcode_documentation.png")