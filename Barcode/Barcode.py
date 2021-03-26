import barcode
import datetime
from barcode import Code128
from barcode.writer import ImageWriter
import os.path
from os import path
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

pathToFile = ''
saveDirectory = ''

def __main__():
    pathToFile = getFilePath()
    print('Beginning processing...')
    generateBarcodes()
    print('Program complete"')


def getFilePath():
    global pathToFile, saveDirectory
    print("Please choose the file...")
    Tk().withdraw()
    pathToFile = askopenfilename()
    print("Choose where to save images...")
    saveDirectory = askdirectory()


def generateBarcodes():
    processed = 0
    global pathToFile, saveDirectory
    errorList = []
    with open(pathToFile) as csv:
        #record[0] = name
        #record[1] = store
        #record[2] = region
       for item in csv:
           record = item.split(',')
           barcodeNumber = record[0].strip() + record[2].zfill(15) + '-' + record[1].strip()
           barcodeText = record[0].strip() + ' ' + record[2].strip() + '-' + record[1].strip()
           fileName = record[2].strip() + '-' + record[1].strip() + ' ' + record[0].strip()
           try:
               #If the barcode already exists in the folder, we won't waste time reprocessing it
               if(path.exists(saveDirectory + '/' + fileName + '.png')):
                   print('Barcode already generated for ' + fileName)
               else:
                   with open(saveDirectory + '/' + fileName + '.png', 'wb') as barcodeFile:
                       Code128(barcodeNumber, writer=ImageWriter()).write(barcodeFile, text=barcodeText) 
                       processed = processed + 1
           except:
               print('Error processing ' + fileName)
               errorList.append(record)
       print('Processing complete. Processed ' + str(processed))
    if errorList:
        print('Writing error log...')
        with open(saveDirectory + '/errors.txt', 'a') as errorLog:
            errorLog.write('-----ERROR LOG-----\n' + str(datetime.datetime.now()) + '\n--------------\n')
            for record in errorList:
                for part in record:
                    errorLog.write(part)
                errorLog.write('\n')


__main__()