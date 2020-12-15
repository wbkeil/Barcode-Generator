import barcode
from barcode import Code128
from barcode.writer import ImageWriter
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

pathToFile = ''
saveDirectory = ''

def __main__():
    pathToFile = getFilePath()
    generateBarcodes()


def getFilePath():
    global pathToFile, saveDirectory
    print("Please choose the file...")
    Tk().withdraw()
    pathToFile = askopenfilename()
    print("Choose where to save images...")
    saveDirectory = askdirectory()


def generateBarcodes():
    global pathToFile, saveDirectory
    errorList = []
    with open(pathToFile) as csv:
       for item in csv:
           record = item.split(',')
           barcodeNumber = record[1].rstrip().zfill(15) #for a nice chunky barcode
           fileName = record[1].rstrip() + ' ' + record[0]
           barcodeText = record[0] + '\n' + record[1].rstrip()
           try:
               with open(saveDirectory + '/' + fileName + '.png', 'wb') as barcodeFile:
                   Code128(barcodeNumber, writer=ImageWriter()).write(barcodeFile, text=barcodeText)                   
           except:
               print('Error processing ' + fileName)
               errorList.append(record)
    with open(saveDirectory + '/errors.txt', 'a') as errorLog:
        for record in errorList:
            for part in record:
                errorLog.write(part)
            errorLog.write('\n')


__main__()