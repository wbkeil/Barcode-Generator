import barcode
from barcode import Code128
from barcode.writer import ImageWriter
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
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
    def getInfo():
        global prefix, start, end
        prefix = int(prefixEntry.get())
        start = int(startEntry.get())
        end = int(endEntry.get()) + 1 #To include entire range

    window = tk.Tk()

    prefixLabel = tk.Label(window, text="Prefix").grid(row=0)
    startLabel = tk.Label(window, text="Start Range").grid(row=1)
    endLabel = tk.Label(window, text="End Range").grid(row=2)

    prefixEntry = tk.Entry(window)
    startEntry = tk.Entry(window)
    endEntry = tk.Entry(window)

    prefixEntry.grid(row=0, column=1)
    startEntry.grid(row=1, column=1)
    endEntry.grid(row=2, column=1)

    button = tk.Button(window,text = "Generate", command=lambda:[getInfo(), window.quit()]).grid(row=3)

    

    window.mainloop()

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