import qrcode

if __name__ == "__main__":
    img = qrcode.make("https://www.youtube.com/watch?v=k9RO-eEF9xo&list=PLhQjrBD2T380Xnv_v683p6UjiKJZe13ki&index=7")
    img.save("qr.png", "PNG")
