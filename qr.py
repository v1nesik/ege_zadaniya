import qrcode
# img = qrcode.make(input('Enter URL:'))
# type(img)  # qrcode.image.pil.PilImage
# img.save(input('Saving name(end .png): '))
from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry('200x250')
root.title('QRCode generation')
root.resizable(False, False)


def generate():
    img = qrcode.make(entry.get())
    type(img)
    img.save('LLLLLde.png')


button = ttk.Button(root, text='Generate QR Code', command=generate)
button.pack(side='bottom')

entry = ttk.Entry(root, text='Enter URL')
entry.pack()

qrcode = PhotoImage(file='LLLLLde')

if generate == True:
    label = ttk.Label(root, image=qrcode)
    label.pack()

root.mainloop()
