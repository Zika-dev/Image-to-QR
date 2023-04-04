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
    width_height = int(input("Enter resolution (1:1): "))
    img = cv2.imread(img_path)
    img = cv2.resize(img, (width_height,width_height), interpolation = cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = np.floor(img / 2.56).astype(np.uint8)
    print(f"Array size: [{img.nbytes}]")
    cv2.imwrite("original.png", img)

    # Create QR
    element_count = 10
    x = 0
    y = element_count
    while True:
        if (img[x:y].nbytes > 500):
            print(f"QR_SIZE: {img[0:element_count].nbytes}")
            print("Too large!")
            element_count = element_count-1
            y=element_count
            continue
        break

    iterations = int(width_height/element_count)
    os.system("cls")
    print(f"{width_height}x{width_height}")
    print(f"Required QR codes: {iterations}")
    for i in tqdm(range(iterations)):
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(img[x:y].tolist())
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(f"qr{i}.png")
        x = x+element_count
        y = y+element_count
    print("Done!")

# Detect QR
def decode_qr(iterations):
    while True:
        anim = input("Animate read? ")
        anim = anim.upper()
        if anim != "Y" and anim != "N":
            print("Invalid choice!")
            continue
        break
    image = []
    for i in tqdm(range(iterations)):
        decoded_image = cv2.imread(f"qr{i}.png")
        data = decode(decoded_image)
        try:
            image.append(eval(data[0].data.decode()))
        except:
            print("Failed to read data")
            exit()
        if anim == "Y":
            decoded_data = np.vstack(image).astype(np.uint8)
            cv2.imshow("image", decoded_data)
            cv2.waitKey(100)

    # Vertically concatenate the decoded arrays
    decoded_data = np.vstack(image).astype(np.uint8)

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
    iterations = int(input("Enter QR amount: "))
    decode_qr(iterations)
