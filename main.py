import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import math

import numpy
import matplotlib.pyplot as plt
import random

def fileinfo(path_file):
    zeros=0
    ones=0
    lenf=0
    with open(''.join(path_file), "rb") as f:
        try:
            byte=f.read(1)
            while byte!=b"":
                byte=bin(int(byte.hex(), base=16))[2:].zfill(8)
                zeros+=byte.count('0')
                ones+=byte.count('1')
                lenf+=8
                byte=f.read(1)
            entropy =(-zeros/lenf*math.log2(zeros/lenf)-ones/lenf*math.log2(ones/lenf))
##            counters = {byte: 0 for byte in range(2 ** 8)}
##            for byte in file.read():
##                counters[byte] += 1
##            filesize = file.tell()
##            probabilities = [counter / filesize for counter in counters.values()]
##            entropy = -sum(probability * math.log2(probability) for probability in probabilities if probability > 0)
            print(entropy)
            messagebox.showinfo(message="Entropy is  %s " %(entropy))
        except ZeroDivisionError:
            messagebox.showwarning(message="Filesize = 0, can't count entropy ")
def first(path_file):
    print(path_file)
    with open (''.join(path_file), "rb") as f1:
        Bytes=numpy.fromfile(f1,dtype="uint8")
        print(Bytes)
        Bits = numpy.unpackbits(Bytes)
        print(Bits)
        q_bits=len(Bits)
        bt=[0,0]
        i=0
        while i<q_bits:
            if Bits[i]==0:
                bt[0]+=1
            elif Bits[i]==1:
                bt[1]+=1
            i+=1
        print(bt)
        plt.plot(Bits)
        plt.show()
        plt.hist(Bits)
        plt.show()
        q_bits=len(Bits)

def paint(x,y):
    python_green="#476042"
    x1,y1 = (x-1), (y-1)
    x2, y2= (x+1), (y+1)
    w.create_oval(x1,y1, x2, y2, fill=python_green)
def second(path_file):
    print("Iam")
    window2=Toplevel(root)
    global w
    w = Canvas(window2,
           width=256,
           height=256)
    w.pack(expand=YES, fill=BOTH)
    y=''
    with open(''.join(path_file), "rb") as f:
        byte = f.read(1)
        while byte != b"":
            byte=bin(int(byte.hex(),base=16))[2:].zfill(8)
            y=y+byte
            byte = f.read(1)
    len_y=len(y)
    y1=[]
    for i in range(0,len_y,8):
        y1.append(int('0b'+''.join(y[i:i+8]),2))
    for i in range(0,256,2):
        paint(y1[i], y1[i+1])
def third(path_file):
    print(path_file)
    with open(''.join(path_file), "rb") as f3:
        Bytes=numpy.fromfile(f3,dtype="uint8")
        print(Bytes)
        Bits = numpy.unpackbits(Bytes)
        q_bits=len(Bits)
        i=0
        array1=[0,0]
        while i<q_bits:
            if Bits[i]==0:
                array1[0]+=1
            elif Bits[i]==1:
                array1[1]+=1
            i+=1
        print(array1)
        index = ["0", "1" ]
        plt.bar(index, array1)
        plt.show()
        array2=[0,0,0,0] #00, 01 , 10 , 11
        i=0
        while i<q_bits-1:
            if Bits[i]==0 and Bits[i+1]==0:
                array2[0]+=1
            elif Bits[i]==0 and Bits[i+1]==1:
                array2[1]+=1
            elif Bits[i]==1 and Bits[i+1]==0:
                array2[2]+=1
            elif Bits[i]==1 and Bits[i+1]==1:
                array2[3]+=1
        ##    print(i, '  ', bit, '  ', array01[0], '  ', array01[1])
            i+=1
        print(array2)
        index = ["00", "01" , "10", "11"]
        plt.bar(index, array2)
        plt.show()
        array3=[0,0,0,0,0,0,0,0] #000, 001 , 010 , 011, 100, 101 , 110 , 111
        i=0
        while i<q_bits-2:
            if Bits[i]==0 and Bits[i+1]==0 and Bits[i+2]==0:
                array3[0]+=1
            elif Bits[i]==0 and Bits[i+1]==0 and Bits[i+2]==1:
                array3[1]+=1
            elif Bits[i]==0 and Bits[i+1]==1 and Bits[i+2]==0:
                array3[2]+=1
            elif Bits[i]==0 and Bits[i+1]==1 and Bits[i+2]==1:
                array3[3]+=1
            elif Bits[i]==1 and Bits[i+1]==0 and Bits[i+2]==0:
                array3[4]+=1
            elif Bits[i]==1 and Bits[i+1]==0 and Bits[i+2]==1:
                array3[5]+=1
            elif Bits[i]==1 and Bits[i+1]==1 and Bits[i+2]==0:
                array3[6]+=1
            elif Bits[i]==1 and Bits[i+1]==1 and Bits[i+2]==1:
                array3[7]+=1
            i+=1
        print(array3)
        index = ["000", "001" , "010", "011", "100", "101", "110", "111"]
        plt.bar(index, array3)
        #plt.hist(array3 )
        plt.show()
        array4=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #0000, 0001 , 0010 ,  ... , 1111
        i=0
        while i<q_bits-3:
            if Bits[i]==0 and Bits[i+1]==0 and Bits[i+2]==0 and Bits[i+3]==0:
                array4[0]+=1
            elif Bits[i]==0 and Bits[i+1]==0 and Bits[i+2]==0 and Bits[i+3]==1:
                array4[1]+=1
            elif Bits[i]==0 and Bits[i+1]==0 and Bits[i+2]==1 and Bits[i+3]==0:
                array4[2]+=1
            elif Bits[i]==0 and Bits[i+1]==0 and Bits[i+2]==1 and Bits[i+3]==1:
                array4[3]+=1
            elif Bits[i]==0 and Bits[i+1]==1 and Bits[i+2]==0 and Bits[i+3]==0:
                array4[4]+=1
            elif Bits[i]==0 and Bits[i+1]==1 and Bits[i+2]==0 and Bits[i+3]==1:
                array4[5]+=1
            elif Bits[i]==0 and Bits[i+1]==1 and Bits[i+2]==1 and Bits[i+3]==0:
                array4[6]+=1
            elif Bits[i]==0 and Bits[i+1]==1 and Bits[i+2]==1 and Bits[i+3]==1:
                array4[7]+=1
            elif Bits[i]==1 and Bits[i+1]==0 and Bits[i+2]==0 and Bits[i+3]==0:
                array4[8]+=1
            elif Bits[i]==1 and Bits[i+1]==0 and Bits[i+2]==0 and Bits[i+3]==1:
                array4[9]+=1
            elif Bits[i]==1 and Bits[i+1]==0 and Bits[i+2]==1 and Bits[i+3]==0:
                array4[10]+=1
            elif Bits[i]==1 and Bits[i+1]==0 and Bits[i+2]==1 and Bits[i+3]==1:
                array4[11]+=1
            elif Bits[i]==1 and Bits[i+1]==1 and Bits[i+2]==0 and Bits[i+3]==0:
                array4[12]+=1
            elif Bits[i]==1 and Bits[i+1]==1 and Bits[i+2]==0 and Bits[i+3]==1:
                array4[13]+=1
            elif Bits[i]==1 and Bits[i+1]==1 and Bits[i+2]==1 and Bits[i+3]==0:
                array4[14]+=1
            elif Bits[i]==1 and Bits[i+1]==1 and Bits[i+2]==1 and Bits[i+3]==1:
                array4[15]+=1
            i+=1
        print(array4)
        index = ["0000", "0001" , "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
        plt.bar(index, array4)
        plt.show()


class FileAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x300")
        self.root.title("File Info")

        self.canvas = tk.Canvas(self.root)
        self.frame = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.frame.bind("<Configure>", lambda event: self.on_frame_configure())

        self.path_file = ""
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Choose file for analysis").grid(row=2, column=1)

        self.label_dir_path = tk.Label(self.frame, width=25, bg='white', fg='black')
        self.label_dir_path.grid(row=3, column=1)

        tk.Button(self.frame, text="Choose file for analysis", command=self.enter_directory).grid(row=3, column=2)
        tk.Button(self.frame, text="Information entropy", command=self.fileinfo).grid(row=10, column=1)
        tk.Button(self.frame, text="Random appearance", command=self.first).grid(row=16, column=0)
        tk.Button(self.frame, text="Random square", command=self.second).grid(row=16, column=1)
        tk.Button(self.frame, text="Random series", command=self.third).grid(row=16, column=2)

    def on_frame_configure(self):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def enter_directory(self):
        self.path_file = fd.askopenfilenames(title="Open", initialdir='/',
                                             filetypes=[("TXT file", "*.txt"),
                                                        ("Doc", "*.doc *.docx"),
                                                        ("Temp file", "*.tmp"),
                                                        ("Other files", "*")])
        self.label_dir_path.config(text=''.join(self.path_file))

    def fileinfo(self):
        fileinfo(self.path_file)

    def first(self):
        first(self.path_file)

    def second(self):
        second(self.path_file)

    def third(self):
        third(self.path_file)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileAnalysisApp(root)
    root.mainloop()