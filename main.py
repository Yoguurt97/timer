from os import system
from tkinter import *

def start():
    time = int(var.get())*60
    time_2 = time//60
    system('shutdown -s -t {0} -c "Ваш компьютер будет выключен через: {1} минут"'.format(time, time_2))
    root.state('iconic')
def stop():
    system('shutdown -a')
if __name__ == "__main__":
    root= Tk()
    root.geometry('200x200')
    root.title('Timer')
    var = DoubleVar()
    label = Label(root, text='Укажите время в минутах.').pack()
    scale = Scale(root, length=300, orient=HORIZONTAL, from_=1, to=120, resolution=1, variable=var).pack()
    Button(root, text='Установить время', command=start).pack()
    Button(root, text='Остановить таймер', command=stop).pack()
    root.mainloop()