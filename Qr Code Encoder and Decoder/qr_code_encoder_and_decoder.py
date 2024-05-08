import qrcode

qr = qrcode.QRCode(
    version = 15,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 5,
    border = 4
)

def encode(data):
    qr.add_data(data)
    qr.make(fit=True)

    return qr.make_image(fill_color = "black", back_color="white")

encode("Hello").save("qrcode.png")