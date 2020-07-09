import barcode
from barcode import Code128
from barcode.writer import ImageWriter
from tkinter import Tk
from tkinter.filedialog import askdirectory


Tk().withdraw()
pathToFile = askdirectory()

prefix = '987650'
for barcodes in range (0, 10000):
    fileName = str(prefix) + str(barcodes).zfill(4)
    with open(pathToFile + '/' + fileName + '.png', 'wb') as barcodeFile:
        print('Writing barcode #' + str(fileName) + '.....')
        Code128(fileName, writer=ImageWriter()).write(barcodeFile)

