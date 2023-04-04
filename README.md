# Image-to-QR
Turn images into QR codes!

## About
This program takes an image input, rescales it to your desired resolution and turns it into grayscale. After that the pixel values are split up into different QR codes.
 
It can also decode the QR codes back into the image!
 
## Note
Should work fine with any resolution. 200x200 = 67 QR codes. 100x50 = 9 QR codes.

The "animation" feature looks weird while it's decoding but after it's fully read the QR codes it will look fine.
## Requirements

- Python 3.9
- cv2
- qrcode
- numpy
- pyzbar
- tkinter
- tqdm
