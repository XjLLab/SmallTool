import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import tkinter.messagebox as messagebox
import threading as Thread
import os

"""
    generate the main window and set the necessary parameters
"""
# find the center position of the window
def getCenterPos(win, width, height):
    x_pos = win.winfo_screenwidth()  
    y_pos = win.winfo_screenheight()
    return width, height, (x_pos-width)/2, (y_pos-height)/2

root = tkinter.Tk()
root.title('Izhikevich Neural Model Simulation Tool')
center_pos = getCenterPos(root, 500, 618) 
root.geometry('%dx%d+%d+%d'%(center_pos[0], center_pos[1], center_pos[2], center_pos[3]))
# root.minsize(center_pos[0], center_pos[1])
# root.maxsize(center_pos[0], center_pos[1])
root.resizable(0, 0)

"""
    generate the widgets
"""
neuron = {
    'LTS':(0.02, 0.25, -65, 2),
    'TC':(0.02, 0.25, -65, 0.05),
    'RS':(0.02, 0.2, -65, 8),
    'IB':(0.02, 0.2, -55, 4),
    'CH':(0.02, 0.2, -50, 2),
    'RZ':(0.1, 0.26, -65, 2),
    'FS':(0.1, 0.2, -65, 2),
}
cmb = ttk.Combobox(root)

'''
LTS:(0.02, 0.25, -65, 2)
TC:(0.02, 0.25, -65, 0.05)
RS:(0.02, 0.2, -65, 8)
IB:(0.02, 0.2, -55, 4)
CH:(0.02, 0.2, -50, 2)
RZ:(0.1, 0.26, -65, 2)
FS:(0.1, 0.2, -65, 2)
'''

type_lb = tkinter.Label(root, text='Neuron Type:')
# type_lb.place(x=60, y=20)
type_lb.place(x=40, y=40)
cmb['value'] = ('LTS', 'TC', 'RS', 'IB', 'CH', 'RZ', 'FS')
cmb.current(1)
cmb.place(x=140, y=40)

v_lb = tkinter.Label(root, text='V:')
v_lb.place(x=40, y=80)
v = tkinter.StringVar()
v_in = tkinter.Entry(root, textvariable=v)
v_in.place(x=60, y=80, width=30)

u_lb = tkinter.Label(root, text='U:')
u_lb.place(x=40, y=120)
u = tkinter.StringVar()
u_in = tkinter.Entry(root, textvariable=u)
u_in.place(x=60, y=120, width=30)

I_lb = tkinter.Label(root, text='I:')
I_lb.place(x=40, y=160)
I = tkinter.StringVar()
I_in = tkinter.Entry(root, textvariable=I)
I_in.place(x=60, y=160, width=30)

if not os.path.exists('test.png'):
    parameters = neuron.get(cmb.get())

    a = parameters[0]
    b = parameters[1]
    c = parameters[2]
    d = parameters[3]

    h = 0.1

    v_ = 63
    u_ = -20
    I_ = 0.15

    data_v = list()
    data_u = list()
    scale = 1000

    for i in range(scale):
        u_ += a*(b*v_ - u_)*h
        v_ += (0.04*v_**2 + 5*v_ + 140 - u_ + I_)*h
        if v_ >= 30:
            v_ = c
            u_ += d 
        data_v.append(v_)
        data_u.append(u_)

    data_x = np.arange(0, scale/10, 0.1)
    plt.title("%s Neuron Simulation Demo"%cmb.get())
    plt.xlabel("t/ms")
    plt.plot(data_x, data_v)
    plt.plot(data_x, data_u)
    save_name = 'test.png'
    plt.savefig(save_name, dpi=(plt.rcParams['figure.dpi']/2))
    plt.clf()

load = Image.open('test.png')
img = ImageTk.PhotoImage(load)
image_lb = tkinter.Label(root, image=img)
image_lb.place(x=100, y=220)

run_bt = tkinter.Button(text='Run')
run_bt.place(x=100, y=540, width=50)

show_bt = tkinter.Button(text='Show')
show_bt.place(x=180, y=540, width=50)

save_bt = tkinter.Button(text='Save')
save_bt.place(x=260, y=540, width=50)

re_bt = tkinter.Button(text='Reset')
re_bt.place(x=340, y=540, width=50)

figure_name = tkinter.StringVar()
figure_name.set('Figure: %s Neuron Wave'%cmb.get())
figure_lb = tkinter.Label(root, textvariable=figure_name)
figure_lb.place(x=200, y=480)

tip = tkinter.StringVar()
tip_lb = tkinter.Label(root, textvariable=tip, fg='red')
tip_lb.place(x=135, y=200)

"""
    write functions for widgets  
"""
save_img = None

def run(event):
    parameters = neuron.get(cmb.get())

    a = parameters[0]
    b = parameters[1]
    c = parameters[2]
    d = parameters[3]

    h = 0.1

    v_ = 63
    if v.get() != '':
        v_ = float(v.get())
    u_ = -20
    if u.get() != '':
        u_= float(u.get())
    I_ = 0.15
    if I.get() != '':
        I_ = float(I.get())

    data_v = list()
    data_u = list()
    scale = 1000

    for i in range(scale):
        u_ += a*(b*v_ - u_)*h
        v_ += (0.04*v_**2 + 5*v_ + 140 - u_ + I_)*h
        if v_ >= 30:
            v_ = c
            u_ += d 
        data_v.append(v_)
        data_u.append(u_)

    data_x = np.arange(0, scale/10, 0.1)
    plt.title("%s Neuron Simulation Demo"%cmb.get())
    plt.xlabel("t/ms")
    plt.plot(data_x, data_v)
    plt.plot(data_x, data_u)
    save_name = 'show.png'
    plt.savefig(save_name, dpi=(plt.rcParams['figure.dpi']/2))
    plt.clf()
    load = Image.open(save_name)
    global save_img
    save_img = load
    img = ImageTk.PhotoImage(load)
    image_lb.configure(image=img)
    image_lb.image = img

def show(event):
    parameters = neuron.get(cmb.get())

    a = parameters[0]
    b = parameters[1]
    c = parameters[2]
    d = parameters[3]

    h = 0.1

    v_ = 63
    if v.get() != '':
        v_ = float(v.get())
    u_ = -20
    if u.get() != '':
        u_= float(u.get())
    I_ = 0.15
    if I.get() != '':
        I_ = float(I.get())

    data_v = list()
    data_u = list()
    scale = 1000

    for i in range(scale):
        u_ += a*(b*v_ - u_)*h
        v_ += (0.04*v_**2 + 5*v_ + 140 - u_ + I_)*h
        if v_ >= 30:
            v_ = c
            u_ += d 
        data_v.append(v_)
        data_u.append(u_)

    data_x = np.arange(0, scale/10, 0.1)
    plt.title("%s Neuron Simulation Demo"%cmb.get())
    plt.xlabel("t/ms")
    plt.plot(data_x, data_v)
    plt.plot(data_x, data_u)
    plt.show()

def save(event):
    global save_img
    if save_img:
        save_img.save('%s.png'%cmb.get())
        tip_lb.configure(fg='blue')
        tip.set('The figure have saved into %s.png'%cmb.get())
    else:
        tip_lb.configure(fg='red')
        tip.set('You must click \'Run\' and generate a figure')

def reset(event):
    v.set('')
    u.set('')
    I.set('')
    tip.set('')


def callback():
    if messagebox.askokcancel('Quit', 'Do you really wish to quit?'):
        plt.close(1)
        root.destroy()


"""
    bind the functions with the widgets
"""
re_bt.bind('<Button-1>' , reset)
run_bt.bind('<Button-1>', run)
save_bt.bind('<Button-1>', save)
show_bt.bind('<Button-1>', show)

root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()
