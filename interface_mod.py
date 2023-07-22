#https://pythonru.com/uroki/obuchenie-python-gui-uroki-po-tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog

def click1():
    lbl.configure(text='button1_pressed')
    files = filedialog.askopenfilenames()
#file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

def click2():
    lbl.configure(text='button2_pressed')
    messagebox.showinfo('Заголовок', 'Текст')
    messagebox.showwarning('Заголовок', 'Текст')  # показывает предупреждающее сообщение
    messagebox.showerror('Заголовок', 'Текст')  # показывает сообщение об ошибке

def click3():
    res=txt.get()
    window.title(res)

def click4():
    if txt2['state'] == 'disabled':
       txt2.configure(state='normal')
    else:
        txt2.configure(state='disabled')

def click5():
    lbl.configure(text='radioBTN_pressed')

window = Tk()
window.title('tkinter test')
#window.geometry('800x600')

lbl = Label(window, text='это label', font=("Arial Bold", 20))
lbl.grid(column=0, row=0)

btn = Button(window, text='buttonFile', command=click1)
btn.grid(column=1, row=0)

btn2 = Button(window, text="button2", bg="black", fg="red", command=click2)
btn2.grid(column=3, row=0)

txt = Entry(window, width=50)
txt.insert(0,'ввод с фокусировкой',)
txt.focus()
txt.grid(column=0, row=1)

btn3 = Button(window, text='set page name', comman=click3)
btn3.grid(column=1,row=1)

txt2 = Entry(window, width=50, state='disabled')
txt2.grid(column=0, row=2)

btn4 = Button(window, text='enable/disable', command=click4)
btn4.grid(column=1, row=2)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 'text')
combo.current(4)
combo.grid(column=0, row=3)

chk_state = BooleanVar()  
chk_state.set(True)  # задайте проверку состояния чекбокса  
chk = Checkbutton(window, text='Выбрать', var=chk_state)  
chk.grid(column=1, row=3)

rad1 = Radiobutton(window, text='Первый', value=1, command=click5)
rad1.grid(column=2, row=3)

txtField = scrolledtext.ScrolledText(window, width=40, height=10)
txtField.insert(INSERT, 'Текстовое поле')
txtField.grid(column=0, row=4)

spin = Spinbox(window, from_=0, to=100, width=10)
spin.grid(column=1,row=4)

bar = Progressbar(window, length=100, orient='vertical')
bar['value'] = 70
bar.grid(column=2, row=4)


window.mainloop()
