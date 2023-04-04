# Image-to-QR
Turn images into QR codes!

## About
This program takes an image input, rescales it to your desired resolution and turns it into grayscale. After that the pixel values are split up into different QR codes.
 
It can also decode the QR codes back into the image!
 
## Note
Should work fine with any resolution. 200x200 = 58 QR codes. 100x50 = 8 QR codes. 1920x1080 = 2963 QR codes.

While decoding you might get warnings. You can ignore them because it will work anyway.
## Requirements

- Python 3.9
- cv2
- qrcode
- numpy
- pyzbar
- tkinter
- tqdm
