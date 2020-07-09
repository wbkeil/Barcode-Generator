import barcode
from barcode import Code128
from barcode.writer import ImageWriter
import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askdirectory

prefix = 0
start = 0
end = 0
pathToFile = ''

def __main__():
    getRangeInfo()
    getFilePath()
    generateBarcodes()

def getRangeInfo():
    global prefix, start, end
    done = False
    while not done:
        prefix = int(input("Enter desired prefix: "))
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))
        if(start < end):
            done = True
        else:
            print("ERROR: Starting number must be higher than ending number.\n")

def getFilePath():
    global pathToFile
    print("Please choose the location you would like the files saved to...")
    Tk().withdraw()
    pathToFile = askdirectory()

def generateBarcodes():
    for barcodes in range (start, end):
        fileName = str(prefix) + str(barcodes).zfill(4) #zfill(4) guarantees that if start or end are < 1000, we have padded 0s
        with open(pathToFile + '/' + fileName + '.png', 'wb') as barcodeFile:
            print('Writing barcode #' + str(fileName) + '.....')
            Code128(fileName, writer=ImageWriter()).write(barcodeFile)

__main__()