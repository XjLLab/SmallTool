from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Tk 
from tkinter import messagebox
from tkinter import StringVar
from PIL import Image, ImageTk

def fun_1(x):
    return (0.4749) + 0.1017*x

def fun_2(x):
    return 1.15805 + 0.07672*x - 0.00103*x**2 + 5.90803E-6*x**3


root = Tk()

root.title('I-U Conversion Tool')

length = 300

root.geometry('%dx%d+%d+%d'%(length, int(length*0.618), (root.winfo_screenwidth() - length)/2.0, (root.winfo_screenheight() - length*0.618)/2.0))

# root.maxsize(width=length, height=int(length*0.618))
# root.minsize(width=length, height=int(length*0.618))
root.resizable(width=False, height=False)

u_value = StringVar()
u_tb = Entry(root, text=u_value)
i_tb = Entry(root)
i_tb.place(x=60, y=40, width=50)
u_tb.place(x=60, y=120, width=50)

img_path = 'D:\\Code\\Python\\Demo\\arrow_small.png'
img = Image.open(img_path)
photo = ImageTk.PhotoImage(img)
img_lb = Label(root, image=photo)
img_lb.place(x=75, y=80)

# arrow = tk.Canvas(root, width=75, height=35)
# arrow.create_text(120, 60, fill="#afeeee", text='Convert I/uA into U/V')
# arrow.place(x=120, y=60)


def convert():
    try:
        if i_tb.get() == '':
            messagebox.showerror("Input Error", "Please input I value in the top textbox") 
            return 
        x = float(i_tb.get())
        if x < 3.1 or x > 112:
            messagebox.showerror("Scale Error", "Please ensure the input number less than 112.0 and big than 3.1")
            return
        
        if 3 < x < 15.3:
            u_value.set(str(fun_1(x)))
        elif x <= 112:
            u_value.set(str(fun_2(x)))
        else:
            return
    except Exception:
        messagebox.showerror(title="Convert Error", message=Exception.__str__)


convert_bt = Button(root, text='Convert', command=convert)
convert_bt.place(x=160, y=80, width=90)

root.mainloop()


