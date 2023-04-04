# Image-to-QR
Turn images into QR codes!

## About
This program takes an image input, rescales it to your desired resolution (1:1) and turns it into grayscale. After that the pixel values are split up into different QR codes.
 
It can also decode the QR codes back into the image!
 
## Note
I have only tested this up to 200x200 pixels which worked fine.

## Requirements

- Python 3.9
- cv2
- qrcode
- numpy
- pyzbar
- tkinter
- tqdm
