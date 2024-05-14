from tkinter import *
from tkinter import filedialog
from encode import encode
from decode import decode_qrcode


message = ""
def decodeQRCode():
    filePath = filedialog.askopenfilename(initialdir='"C:\Projects\Python Projects\Qr Code Encoder and Decoder"',
                                          title="Select a file",
                                          filetypes=[("PNG file", ".png"), ("JPEG file", ".jpg")])
    

    decodedMessage = decode_qrcode(filePath)
    

    message = Label(window,
                    font=("Arial", 12, "italic"),
                    text=decodedMessage)
    message.pack()

# This code generates a GUI for the QR Code encoder once "Encode a QR Code" is pressed
def encodeQRCode():
    global message

    # Below is the text area where user can enter their message
    userMessage = Text(window, height=10, width=50)
    userMessage.pack()

    message = userMessage.get(1.0, END)

    #Below is the button that generates the QR Code, it calls the function "generateQrCode" when pressed
    generateQrCodeButton = Button(window, 
                            text="Generate Qr Code",
                            command=generateQrCode,
                            font=("Arial", 12),
                            activebackground="lightgray",
                            relief=SOLID,
                            bd=1)

    generateQrCodeButton.pack()

    return message
def generateQrCode():
    global message

    # This function generates a QR code image based on the message entered by the user in the GUI text area.
    # It uses the `encode()` function from the `encode` library to encode the message into a QR code image.
    
    qrcodeImage = encode(message)


    #The code below generates a fath where the image will be saved. The path is chosen by the user.
    file = filedialog.asksaveasfile(defaultextension=".png",
                                filetypes=(("PNG file", ".png"), ("JPEG file", ".jpg")))
    
    #The code below saves the image in the path generated above (file) 
    if file:
        try:
            qrcodeImage.save(file.name)
        except Exception as e:
            print("There was an error while saving the file.")   

    file.close()

window = Tk()
window.geometry("600x400")
window.title("Qr Code Encoder and Decoder")

greeting= Label(window, 
               text="Hello There!",
               font= ("Arial", 16, "bold"))
greeting.pack()

instruction= Label(window, 
               text="Enter the message or link that you want to encode.",
               font= ("Arial", 16, "bold"))
instruction.pack()



generateQrCodeButton = Button(window, 
                              text="Encode a QR Code",
                              command=encodeQRCode,
                              font=("Arial", 12),
                              activebackground="lightgray",
                              relief=SOLID,
                              bd=1)

generateQrCodeButton.pack()


decodingQrCodeButton = Button(window, 
                              text="Decode a QR Code",
                              command=decodeQRCode,
                              font=("Arial", 12),
                              activebackground="lightgray",
                              relief=SOLID,
                              bd=1)

decodingQrCodeButton.pack()

window.mainloop()