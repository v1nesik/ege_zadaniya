import qrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()

root.geometry('500x400')
root.title('QRCode generation')
root.resizable(False, False)


label = ttk.Label(root, text='Enter URL')
label.pack()

entry = ttk.Entry(root, text='Enter URL')
entry.pack()

label_file = ttk.Label(root, text='Enter File Name(.png)')
label_file.pack()

entry_file = ttk.Entry(root, text='Enter File Name')
entry_file.pack()


def generate():
    img = qrcode.make(entry.get())
    type(img)
    img.save(entry_file.get())
    img = ImageTk.PhotoImage(Image.open(entry_file.get()))
    panel = Label(image=img)
    panel.image = img
    panel.pack(side='bottom')


button = ttk.Button(root, text='Generate QR Code', command=generate)
button.pack(side='bottom')

label_help = ttk.Label(
    root, text='The file is saved in the directory where you ran the code')
label_help.pack()

root.mainloop()
