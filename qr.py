import qrcode
img = qrcode.make('https://www.youtube.com/')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")