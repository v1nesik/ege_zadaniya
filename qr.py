import qrcode
from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry('300x250')
root.title('QRCode generation')
root.resizable(False, False)


def generate():
    img = qrcode.make(entry.get())
    type(img)
    img.save(entry_file.get())


button = ttk.Button(root, text='Generate QR Code', command=generate)
button.pack(side='bottom')

label = ttk.Label(root, text='Enter URL')
label.pack()

entry = ttk.Entry(root, text='Enter URL')
entry.pack()

label_file = ttk.Label(root, text='Enter File Name(.png)')
label_file.pack()

entry_file = ttk.Entry(root, text='Enter File Name')
entry_file.pack()

label_help = ttk.Label(root, text='The file is saved in the directory where you ran the code')
label_help.pack()

root.mainloop()
