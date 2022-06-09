from tkinter import *
import os


root = Tk()
root.title('CookieClicker by eyesss.py')
root.geometry('600x600')
root.resizable(width=False, height=False)



click = Label(root, text='Кликов сделано: 0', font='Arial 25', padx='20', pady='90')
click.pack()



count = 0
def clicked():
    global count
    count += 1
    click.configure(text=f'Кликов сделано: {count}')


dir = os.path.abspath(os.curdir)
cookie = PhotoImage(file=f'{dir}/cookie.png')
cookie = cookie.subsample(1,1)
Button(root, image=cookie, highlightthickness=0, bd=0, command=clicked).place(x=155, y=250)



root.mainloop()