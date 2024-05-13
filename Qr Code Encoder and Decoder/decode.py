from pyzbar.pyzbar import decode
from PIL import Image

def decode_qrcode(img):
    image = Image.open(img)
    decoded_message = decode(image)[0].data.decode('utf-8')

    return decoded_message