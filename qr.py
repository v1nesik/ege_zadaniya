import qrcode
img = qrcode.make(input('Enter URL:'))
type(img)  # qrcode.image.pil.PilImage
img.save(input('Saving name(end .png): '))
