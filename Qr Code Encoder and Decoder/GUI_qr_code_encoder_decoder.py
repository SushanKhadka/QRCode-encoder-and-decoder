from tkinter import *
from tkinter import filedialog
from qr_code_encoder_and_decoder import encode

def generateQrCode():
    message = userMessage.get(1.0, END)
    qrcodeImage = encode(message)

    file = filedialog.asksaveasfile(defaultextension=".png",
                                filetypes=(("PNG file", ".png"), ("JPEG file", ".jpg")))
    
    if file is None:
        return
    
    qrcodeImage.save(file)

    
    file.close()

window = Tk()
window.geometry("600x400")
window.title("Qr Code Encoder and Decoder")

greeting= Label(window, 
               text="Hello There!",
               font= ("Arial", 16, "bold"))
greeting.pack()

instruction= Label(window, 
               text="Entet the message or link that you want to encode.",
               font= ("Arial", 16, "bold"))
instruction.pack()

userMessage = Text(window, height=10, width=50)
userMessage.pack()

generateQrCodeButton = Button(window, 
                              text="Generate Qr Code",
                              command=generateQrCode,
                              font=("Arial", 12),
                              activebackground="lightgray",
                              relief=SOLID,
                              bd=1)

generateQrCodeButton.pack()

window.mainloop()