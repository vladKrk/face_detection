from cProfile import label
from tempfile import template
import tkinter
from task1 import useTemplateAnalyze
from task2 import useCascadeAnalyze
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import Image, ImageTk

templates = {
    'Голова': 'template1',
    'Лицо': 'template2',
    'Глаза и нос': 'template3',
    'Глаза': 'template4',
    'Левый глаз': 'template4a',
    'Правый глаз': 'template4b',
    'Рот': 'template5',
    'Нос': 'template6',
}


class GUI:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Task 1")
        self.window.geometry('800x600')
        

    def start(self):
        self.window.mainloop()

    def open_file(self):
        global img, file_path
        my_str = tkinter.StringVar()
        l2 = tkinter.Label(self.window,textvariable=my_str,fg='black' )
        l2.place(x=250, y=150)
        my_str.set("")
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*jpg')])
        if file_path is not None:
            img=Image.open(file_path)
            width, height = img.size  
            width_new=int(width/3)
            height_new=int(height/3)
            img_resized=img.resize((width_new,height_new))
            img=ImageTk.PhotoImage(img_resized)
            my_str.set(file_path)
            b2 = Button(self.window,image=img)
            b2.place(width=700, height=400, x=50, y=200)
            
    
    def addTemplateButton(self, templateName, x, y):
        style = tkinter.ttk.Style()
        style.configure("TButton", background='grey', pady='16', padx='16')
        btn = tkinter.ttk.Button(self.window, text=templateName, 
                                style="TButton", command=lambda: useTemplateAnalyze(templates[templateName], file_path))
        btn.place(width=80, height=40, x=x, y=y)
    def uploadButton(self):
        my_font1=('times', 18, 'bold')
     
        face = Label(self.window, text='Загрузите фото для распознавания в формате jpg ', width=50,font=my_font1 )
        face.pack()
        facebtn = Button(self.window, text ='Выберите фото', width=20, command = lambda: gui.open_file()) 
        facebtn.pack()
    def addCascadeButton(self):
        my_font1=('times', 18, 'bold')
        label2 = Label(self.window, text='Метод Виолы-Джонса', anchor=CENTER, width=30,font=my_font1 )
        label2.place(width=250, height=40, x=20, y=110)
        btn = tkinter.ttk.Button(self.window, text='Метод Виолы-Джонса', style="TButton", command=lambda: useCascadeAnalyze(file_path))
        btn.place(width=140, height=40, x=290, y=110)
    
gui = GUI()

gui.uploadButton()
gui.addTemplateButton('Голова', 20, 60)
gui.addTemplateButton('Лицо', 110, 60)
gui.addTemplateButton('Глаза и нос', 200, 60)
gui.addTemplateButton('Глаза', 290, 60)
gui.addTemplateButton('Левый глаз', 380, 60)
gui.addTemplateButton('Правый глаз', 470, 60)
gui.addTemplateButton('Рот', 560, 60)
gui.addTemplateButton('Нос', 650, 60)

gui.addCascadeButton()

gui.start()
    