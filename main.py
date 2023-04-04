import cv2
import qrcode
import numpy as np
import os
from pyzbar.pyzbar import decode
from tkinter import filedialog
import tkinter as tk
from tqdm import tqdm

root = tk.Tk()
root.withdraw()

detector = cv2.QRCodeDetector()

def encode_qr():
    # Pre processing
    img_path = filedialog.askopenfilename()
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    img = cv2.imread(img_path)
    img = cv2.resize(img, (width,height), interpolation = cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f"\nArray size: [{img.nbytes}]")
    cv2.imwrite("original.png", img)
    img = np.floor(img / 2.56).astype(np.uint8)
    # Create QR
    y=0
    iterations = int(np.ceil(img.nbytes/700))
    if (iterations < 1):
        iterations=1
    print(f"{width}x{height}")
    print(f"Required QR codes: {iterations}")
    for i in tqdm(range(iterations)):
        data_chunk = img.ravel()[y:y+700].tolist()
        if i == iterations-1:
            data_chunk.extend([0] * (700 - len(data_chunk)))
        qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(data_chunk)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(f"qr_codes/qr{i}.png")
        y=y+700
    print("Done!")

# Detect QR
def decode_qr(iterations, width, height):
    while True:
        anim = input("Animate read? ")
        anim = anim.upper()
        if anim != "Y" and anim != "N":
            print("Invalid choice!")
            continue
        break
    image = []
    preview = np.zeros((height, width), dtype=np.uint8)
    for i in tqdm(range(iterations)):
        decoded_image = cv2.imread(f"qr_codes/qr{i}.png")
        data = decode(decoded_image)
        try:
            image.append(eval(data[0].data.decode()))
        except:
            print("Failed to read data")
            exit()
        if anim == "Y":
            decoded_data = np.hstack(image).astype(np.uint8)
            start_row = i * 700 // width
            end_row = min((i + 1) * 700 // width, height)
            preview[start_row:end_row, :] = decoded_data[start_row*width:end_row*width].reshape(end_row-start_row, width)
            cv2.imshow("image", preview)
            cv2.waitKey(100)

    # Restore the image
    decoded_data = np.hstack(image).astype(np.uint8)
    decoded_data = decoded_data[:width*height].reshape(height, width)
    decoded_data = np.floor(decoded_data * 2.57).astype(np.uint8)

    # Display the decoded image
    cv2.imwrite("decoded_image.png", decoded_data)
    cv2.imshow("image", decoded_data)
    print("Done!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

while True:
    task = input("Encode or Decode? ")
    task = task.upper()
    if task != "ENCODE" and task != "DECODE":
        print("Invalid choice!")
        continue
    break
os.system("cls")
if task == "ENCODE":
    encode_qr()
else:
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    iterations = int(input("Enter QR amount: "))
    decode_qr(iterations, width, height)
