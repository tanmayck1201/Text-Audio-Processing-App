from tkinter import *
from tkinter import ttk
import random
import time
f3=Tk()
f3.geometry("800x600")
f3.title("Audio and Text Processing")
bg= PhotoImage(file="C:\\Users\\Administrator.WHITEHOUSE\\Desktop\\Programming\\MiniPjct Sem4\\Py Mini-Project\\Wall.png")
select_alg = StringVar()
data = []
select_alg1 = StringVar()
data1 = []

def bubble(data, drawData, timer):
    n = len(data)
      
    for i in range(n):
        for j in range(0, n-i-1):
              
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                  
                # if swapped then color becomes Green else stays Red
                drawData(data, ['Green' if x == j +
                                1 else 'Red' for x in range(len(data))])
                time.sleep(timer)
          
    # sorted elements geneated with Green color
    drawData(data, ['Green' for x in range(len(data))])

def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]
  
    drawData(data, getColorArray(len(data), head, 
                                 tail, border, border))
    time.sleep(timeTick)
  
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(
                len(data), head, tail, border, j, True))
            time.sleep(timeTick)
  
            data[border], data[j] = data[j], data[border]
            border += 1
  
        drawData(data, getColorArray(len(data), head, 
                                     tail, border, j))
        time.sleep(timeTick)
  
    # swapping pivot with border value
    drawData(data, getColorArray(len(data), head, 
                                 tail, border, tail, True))
    time.sleep(timeTick)
  
    data[border], data[tail] = data[tail], data[border]
  
    return border
  
  
# head  --> Starting index,
# tail  --> Ending index
def quick_sort(data, head, tail, 
               drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, 
                                 tail, drawData, 
                                 timeTick)
  
        # left partition
        quick_sort(data, head, partitionIdx-1, 
                   drawData, timeTick)
  
        # right partition
        quick_sort(data, partitionIdx+1, 
                   tail, drawData, timeTick)
  
# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - Sfter all elements are sorted
  
# assign color representation to elements
  
  
def getColorArray(dataLen, head, tail, border,
                  currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # base coloring
        if i >= head and i <= tail:
            colorArray.append('Grey')
        else:
            colorArray.append('White')
  
        if i == tail:
            colorArray[i] = 'Blue'
        elif i == border:
            colorArray[i] = 'Red'
        elif i == currIdx:
            colorArray[i] = 'Yellow'
  
        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'Green'
  
    return colorArray

def qui():
    f30=Frame()
    f30.place(x="0",y="0",width="800",height="600")
    Label(f30, image=bg).place(x="0",y="0",relwidth="1",relheight="1")
    def generate1():
      
        global data1
  
        # minval : minimum value of the range
        minval = int(minEntry.get())
  
        # maxval : maximum value of the range
        maxval = int(maxEntry.get())
  
        # sizeval : number of data1 
        # values/bars to be generate1d
        sizeval = int(sizeEntry.get())
  
        # creating a blank data1 list which will 
        # be further filled with random data1 values
        # within the entered range
        data1 = []
        for _ in range(sizeval):
            data1.append(random.randrange(minval, maxval+1))
  
        drawdata12(data1, ['Red' for x in range(len(data1))])
  
# funtion to create the data1 bars 
# by creating a canvas in Tkinter
    def drawdata12(data1, colorlist):
        canvas.delete("all")
        can_height = 380
        can_width = 550
        x_width = can_width/(len(data1) + 1)
        offset = 30
        spacing = 10
        # normalizing data1 for rescaling real-valued 
        # numeric data1 within the
        # given range
        normalized_data1 = [i / max(data1) for i in data1]
      
        for i, height in enumerate(normalized_data1):
            # top left corner
            x0 = i*x_width + offset + spacing
            y0 = can_height - height*340
      
            # bottom right corner
            x1 = ((i+1)*x_width) + offset
            y1 = can_height
      
            # data1 bars are generate1d as Red 
            # colored vertical rectangles
            canvas.create_rectangle(x0, y0, x1, y1, 
                                    fill=colorlist[i])
            canvas.create_text(x0+2, y0, anchor=SE, 
                               text=str(data1[i]))
        f30.update_idletasks()
  
    # function to initiate the sorting 
    # process by calling the extension code    
    
    def start_algorithm1():     
        global data1
  
        if not data1:
            return
  
        if (algmenu.get() == 'Quick Sort'):
            quick_sort(data1, 0, len(data1)-1, drawdata12, speedbar.get())
            drawdata12(data1, ['Green' for x in range(len(data1))])
  
  
         # creating main user interface frame 
         # and basic layout by creating a frame
    Mainframe = Frame(f30, width=600, height=200, bg="Grey")
    Mainframe.grid(row=0, column=0, padx=10, pady=5)
  
    canvas = Canvas(f30, width=600, height=380, bg="Grey")
    canvas.grid(row=1, column=0, padx=10, pady=5)
  
     # creating user interface area in grid manner
     # first row components
    Label(Mainframe, text="ALGORITHM",      
          bg='Grey').grid(row=0, column=0, 
                      padx=5, pady=5, 
                      sticky=W)
  
     # algorithm menu for showing the 
     # name of the sorting algorithm
    algmenu = ttk.Combobox(Mainframe,      
                       textvariable=select_alg1, 
                       values=["Quick Sort"])
    algmenu.grid(row=0, column=1, padx=5, pady=5)
    algmenu.current(0)
  
     # creating Start Button to start 
     # the sorting visualization process
    Button(Mainframe, text="START", 
            bg="Blue", 
            command=start_algorithm1).grid(row=1, 
                                          column=3, 
                                          padx=5, 
                                          pady=5)
  
     # creating Speed Bar using scale in Tkinter
    speedbar = Scale(Mainframe, from_=0.10, 
                 to=2.0, length=100, digits=2,
                 resolution=0.2, orient=HORIZONTAL, 
                 label="Select Speed")
    speedbar.grid(row=0, column=2, 
              padx=5, pady=5)
  
     # second row components
     # sizeEntry : scale to select 
     # the size/number of data1 bars
    sizeEntry = Scale(Mainframe, from_=3, 
                  to=60, resolution=1,
                  orient=HORIZONTAL, 
                  label="Size")
    sizeEntry.grid(row=1, column=0, 
               padx=5, pady=5)
  
     # minEntry : scale to select the 
     # minimum value of data1 bars
    minEntry = Scale(Mainframe, from_=0, 
                 to=10, resolution=1,
                 orient=HORIZONTAL, 
                 label="Minimun Value")
    minEntry.grid(row=1, column=1, 
              padx=5, pady=5)
  
     # maxEntry : scale to select the 
     # maximum value of data1 bars
    maxEntry = Scale(Mainframe, from_=10, 
                 to=100, resolution=1,
                 orient=HORIZONTAL, 
                 label="Maximun Value")
    maxEntry.grid(row=1, column=2, 
              padx=5, pady=5)
  
     # creating generate1 button
    Button(Mainframe, text="generate1", 
       bg="Red", 
       command=generate1).grid(row=0, 
                              column=3, 
                              padx=5, 
                              pady=5)
    bt475=Button(f30,text="Go Back",width=12,command=mainpage)
    bt475.grid()
  
     # to stop automatic window termination

def bub():
    f20=Frame()
    f20.place(x="0",y="0",width="800",height="600")
    Label(f20, image=bg).place(x="0",y="0",relwidth="1",relheight="1")
    def generate():
        global data
 
        # minval : minimum value of the range
        minval = int(minEntry.get())
 
        # maxval : maximum value of the range
        maxval = int(maxEntry.get())
 
        # sizeval : number of data values/bars to be generated
        sizeval = int(sizeEntry.get())
 
        # creating a blank data list which will be further
        # filled with random data values
        # within the entered range
        data = []
        for _ in range(sizeval):
            data.append(random.randrange(minval, maxval+1))
 
        drawData(data, ['Red' for x in range(len(data))])
 
# function to create the data bars by creating a canvas in Tkinter
    def drawData(data, colorlist):
        canvas.delete("all")
        can_height = 380
        can_width = 550
        x_width = can_width/(len(data) + 1)
        offset = 30
        spacing = 10
     
        # normalizing data for rescaling real-valued numeric data within the
        # given range
        normalized_data = [i / max(data) for i in data]
     
        for i, height in enumerate(normalized_data):
            # top left corner
            x0 = i*x_width + offset + spacing
            y0 = can_height - height*340
     
            # bottom right corner
            x1 = ((i+1)*x_width) + offset
            y1 = can_height
     
            # data bars are generated as Red colored vertical rectangles
            canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
            canvas.create_text(x0+2, y0, anchor=SE, text=str(data[i]))
        f20.update_idletasks()
 
    # function to initiate the sorting process by
    # calling the extension code
    def start_algorithm():
        global data
        bubble(data, drawData, speedbar.get())
     
     
    # creating main user interface frame and
    # basic layout by creating a frame
    Mainframe = Frame(f20, width=600, height=200, bg="Grey")
    Mainframe.grid(row=0, column=0, padx=10, pady=5)
 
    canvas = Canvas(f20, width=600, height=380, bg="Grey")
    canvas.grid(row=1, column=0, padx=10, pady=5)
 
    # creating user interface area in grid manner
    # first row components
    Label(Mainframe, text="ALGORITHM", bg='Grey').grid(
        row=0, column=0, padx=5, pady=5, sticky=W)
     
    # algorithm menu for showing the name of the sorting algorithm
    algmenu = ttk.Combobox(
        Mainframe, textvariable=select_alg, values=["Bubble Sort"])
    algmenu.grid(row=0, column=1, padx=5, pady=5)
    algmenu.current(0)
     
    # creating Start Button to start the sorting visualization process
    Button(Mainframe, text="START", bg="Blue", command=start_algorithm).grid(
        row=1, column=3, padx=5, pady=5)
     
    # creating Speed Bar using scale in Tkinter
    speedbar = Scale(Mainframe, from_=0.10, to=2.0, length=100, digits=2,
                     resolution=0.2, orient=HORIZONTAL, label="Select Speed")
    speedbar.grid(row=0, column=2, padx=5, pady=5)
 
 
    # second row components
    # sizeEntry : scale to select the size/number of data bars
    sizeEntry = Scale(Mainframe, from_=3, to=60, resolution=1,
                      orient=HORIZONTAL, label="Size")
    sizeEntry.grid(row=1, column=0, padx=5, pady=5)
 
    # minEntry : scale to select the minimum value of data bars
    minEntry = Scale(Mainframe, from_=0, to=10, resolution=1,
                     orient=HORIZONTAL, label="Minimun Value")
    minEntry.grid(row=1, column=1, padx=5, pady=5)
 
    # maxEntry : scale to select the maximum value of data bars
    maxEntry = Scale(Mainframe, from_=10, to=100, resolution=1,
                     orient=HORIZONTAL, label="Maximun Value")
    maxEntry.grid(row=1, column=2, padx=5, pady=5)
 
    # creating generate button
    Button(Mainframe, text="Generate", bg="Red", command=generate).grid(
        row=0, column=3, padx=5, pady=5)
    bt477=Button(f20,text="Go Back",width=12,command=mainpage)
    bt477.grid()

    


def mainpage():
    f0=Frame()
    f0.place(x="0",y="0",width="800",height="600")
    Label(f0, image=bg).place(x="0",y="0",relwidth="1",relheight="1")
    Label(f0,text="visualization of bubble sort and quicksort",font="comicsansms 30 bold",fg="lightblue").grid()
    Label(f0,text=" GUI Application",font="comicsansms 30 bold",fg="lightblue").grid()
    l1=Label(f0,text="Visualization of Bubble Sort Algorithm",font="Times 20 bold")
    l1.grid(padx=30)
    bt1=Button(f0,text="View",command=bub,font=("comicsansms","10"))
    bt1.grid(pady="50")
    l2=Label(f0,text="Visualization Of Quick Sort Algorithm",font="Times 20 bold")
    l2.grid(padx=30)
    bt2=Button(f0,text="View",command=qui,font=("comicsansms","10"))
    bt2.grid(pady="50")
    bt3=Button(f0,text="Exit",command=exit,font=("comicsansms","10"))
    bt3.grid(pady="10")
mainpage()
f3.mainloop()