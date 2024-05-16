from pyzbar.pyzbar import decode
from PIL import Image

def decodeQRCode(img):
    image = Image.open(img)
    decoded_message = decode(image)[0].data.decode('utf-8')
    print (decoded_message)

    return decoded_message

