import tkinter as tk
from datetime import datetime
from getTime import getTime
import time
import threading
import os

#เวลาบนโปรแกรม
def runTime():
    while True:
        current_time['text'] = getTime('time')
        current_date['text'] = getTime('date')
        time.sleep(0.1)

def hpDrainCal():
    class double_effect:
        def Yes():
            cb1_2.deselect()

        def No():
            cb1_1.deselect()

    class weapon:
        def Yes():
            cb2_2.deselect()

        def No():
            cb2_1.deselect()

    class accessory:
        def Yes():
            cb3_2.deselect()

        def No():
            cb3_1.deselect()

    def remove():
        lb1_1.grid_remove()
        cb1_1.grid_remove()
        cb1_2.grid_remove()
        lb2_1.grid_remove()
        cb2_1.grid_remove()
        cb2_2.grid_remove()
        lb3_1.grid_remove()
        cb3_1.grid_remove()
        cb3_2.grid_remove()
        lb4_1.grid_remove()
        lb4_2.grid_remove()
        entry4_fLck.grid_remove()
        entry4_bLck.grid_remove()
        bt5_1.grid_remove()
        lb6_1.grid_remove()
        lb6_2.grid_remove()
        lb7_1.grid_remove()
        lb7_2.grid_remove()
        menuBar.delete('Reset Program')
        menuBar.entryconfigure('Program' , state = 'normal')


    def calculate():
        fLck = int(entry4_fLck.get())
        bLck = int(entry4_bLck.get())
        TotalLck = fLck + bLck
        lb6_2['text'] = TotalLck

        hpDrain = 0

        if value2_1.get() == 'True':
            hpDrain = hpDrain + 12
        
        elif value2_2.get() == 'False':
            hpDrain = hpDrain + 0

        if value1_1.get() == 'True':
            hpDrain = hpDrain * 2

        elif value1_2.get() == 'False':
            hpDrain = hpDrain + 0

        if value3_1.get() == 'True':
            hpDrain = hpDrain + 8

        elif value3_2.get() == 'False':
            hpDrain = hpDrain +0

        x = hpDrain * ((TotalLck / 100) + 1)
        percent_hpDrain = ((x * 100) / (x - hpDrain + 100))
        hpDrain_text = '{0:.2f} {1:s}'.format(percent_hpDrain,'%')

        lb7_2['text'] = hpDrain_text
    
    #DoubleEffect
    lb1_1 = tk.Label(master = app , text = 'Have Double Effect line C ?')
    lb1_1.grid(row = 2 , column = 0 , columnspan = 2 , padx = (5,5) , pady = (10,0))
    lb1_1.config(font = ('Tahoma' , 10))
    
    value1_1 = tk.StringVar()
    value1_2 = tk.StringVar()
    
    cb1_1 = tk.Checkbutton(master = app , text = 'Yes' , variable = value1_1 , onvalue = 'True' , offvalue = '' , command = double_effect.Yes)
    cb1_1.grid(row = 3 , column = 0 , padx = (0,0) , pady = (0,0))
    cb1_1.config(font = ('Tahoma' , 10))

    cb1_2 = tk.Checkbutton(master = app , text = 'No' , variable = value1_2 , onvalue = 'False' , offvalue = '' , command = double_effect.No)
    cb1_2.grid(row = 3 , column = 1 , padx = (0,0) , pady = (0,0))
    cb1_2.config(font = ('Tahoma' , 10))

    #Weapon
    lb2_1 = tk.Label(master = app , text = 'Have Water Dungeon Weapon ?')
    lb2_1.grid(row = 4 , column = 0 , columnspan = 2 , padx = (5,5) , pady = (0,0))
    lb2_1.config(font = ('Tahoma' , 10))

    value2_1 = tk.StringVar()
    value2_2 = tk.StringVar()

    cb2_1 = tk.Checkbutton(master = app , text = 'Yes' , variable = value2_1 , onvalue = 'True' , offvalue = '' , command = weapon.Yes)
    cb2_1.grid(row = 5 , column = 0 , padx = (0,0) , pady = (0,0))
    cb2_1.config(font = ('Tahoma' , 10))

    cb2_2 = tk.Checkbutton(master = app , text = 'No' , variable = value2_2 , onvalue = 'False' , offvalue = '' , command = weapon.No)
    cb2_2.grid(row = 5 , column = 1 , padx = (0,0) , pady = (0,0))
    cb2_2.config(font = ('Tahoma' , 10))

    #Accessory
    lb3_1 = tk.Label(master = app , text = 'Have Water Dungeon Accessory ?')
    lb3_1.grid(row = 6 , column = 0 , columnspan = 2 , padx = (5,5) , pady = (0,0))
    lb3_1.config(font = ('Tahoma' , 10))

    value3_1 = tk.StringVar()
    value3_2 = tk.StringVar()

    cb3_1 = tk.Checkbutton(master = app , text = 'Yes' , variable = value3_1 , onvalue = 'True' , offvalue = '' , command = accessory.Yes)
    cb3_1.grid(row = 7 , column = 0 , padx = (0,0) , pady = (0,0))
    cb3_1.config(font = ('Tahoma' , 10))

    cb3_2 = tk.Checkbutton(master = app , text = 'No' , variable = value3_2 , onvalue = 'False' , offvalue = '' , command = accessory.No)
    cb3_2.grid(row = 7 , column = 1 , padx = (0,0) , pady = (0,0))
    cb3_2.config(font = ('Tahoma' , 10))

    #Enter LCK
    lb4_1 = tk.Label(master = app , text = 'Enter Front LCK')
    lb4_1.grid(row = 8 , column = 0 , padx = (0,0) , pady = (0,0))
    lb4_1.config(font = ('Tahoma' , 10))

    lb4_2 = tk.Label(master = app , text = 'Enter Back LCK')
    lb4_2.grid(row = 8 , column = 1 , padx = (0,0) , pady = (0,0))
    lb4_2.config(font = ('Tahoma' , 10))
    
    entry4_fLck = tk.Entry(master = app , width = 5)
    entry4_fLck.grid(row = 9 , column = 0 , padx = (0,0) , pady = (0,0))

    entry4_bLck = tk.Entry(master = app , width = 5)
    entry4_bLck.grid(row = 9 , column = 1 , padx = (0,0) , pady = (0,0))

    #Calculate
    bt5_1 = tk.Button(master = app , text = 'Calculate' , command = calculate)
    bt5_1.grid(row = 10 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (5,5))
    bt5_1.config(font = ('Tahoma' , 10))

    #Total Lck
    lb6_1 = tk.Label(master = app , text = 'Total Lck')
    lb6_1.grid(row = 11 , column = 0 , padx = (0,0) , pady = (0,0))
    lb6_1.config(font = ('Tahoma' , 10))
        
    lb6_2 = tk.Label(master = app , text = '-')
    lb6_2.grid(row = 11 , column = 1 , padx = (0,0) , pady = (0,0))
    lb6_2.config(font = ('Tahoma' , 10))

    #Percent of hpDrain
    lb7_1 = tk.Label(master = app , text = 'hpDrain')
    lb7_1.grid(row = 12 , column = 0 , padx = (0,0) , pady = (0,5))
    lb7_1.config(font = ('Tahoma' , 10))

    lb7_2 = tk.Label(master = app , text = '- %')
    lb7_2.grid(row = 12 , column = 1 , padx = (0,0) , pady = (0,5))
    lb7_2.config(font = ('Tahoma' , 10))

    menuBar.add_cascade(label = 'Reset Program' , menu = '' , command = remove)
    menuBar.entryconfigure('Program' , state = 'disabled')

def EffectCal():
    def remove():
        lb1_1.grid_remove()
        entry1_1.grid_remove()
        lb2_1.grid_remove()
        lb2_2.grid_remove()
        entry2_fLck.grid_remove()
        entry2_bLck.grid_remove()
        bt3_1.grid_remove()
        lb4_1.grid_remove()
        lb4_2.grid_remove()
        lb5_1.grid_remove()
        lb5_2.grid_remove()
        menuBar.delete('Reset Program')
        menuBar.entryconfigure('Program' , state = 'normal')

        
    def calculate():
        fLck = int(entry2_fLck.get())
        bLck = int(entry2_bLck.get())
        TotalLck = fLck + bLck
        lb4_2['text'] = TotalLck

        effect_percent = float(entry1_1.get())
        x = effect_percent * ((TotalLck / 100) + 1)
        percent_effect = ((x * 100) / (x - effect_percent + 100))
        effect_text = '{0:.2f} {1:s}'.format(percent_effect,'%')

        lb5_2['text'] = effect_text
        
    #Enter Percent
    lb1_1 = tk.Label(master = app , text = 'Enter Total Percent of Effect')
    lb1_1.grid(row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (10,0))
    lb1_1.config(font = ('Tahoma' , 10))

    entry1_1 = tk.Entry(master = app , width = 5)
    entry1_1.grid(row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (0,0))

    #Enter Lck
    lb2_1 = tk.Label(master = app , text = 'Enter Front LCK')
    lb2_1.grid(row = 4 , column = 0 , padx = (5,0) , pady = (0,0))
    lb2_1.config(font = ('Tahoma' , 10))

    lb2_2 = tk.Label(master = app , text = 'Enter Back LCK')
    lb2_2.grid(row = 4 , column = 1 , padx = (0,5) , pady = (0,0))
    lb2_2.config(font = ('Tahoma' , 10))
    
    entry2_fLck = tk.Entry(master = app , width = 5)
    entry2_fLck.grid(row = 5 , column = 0 , padx = (0,0) , pady = (0,0))

    entry2_bLck = tk.Entry(master = app , width = 5)
    entry2_bLck.grid(row = 5 , column = 1 , padx = (0,0) , pady = (0,0))

    #Calculate
    bt3_1 = tk.Button(master = app , text = 'Calculate' , command = calculate)
    bt3_1.grid(row = 6 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (5,5))
    bt3_1.config(font = ('Tahoma' , 10))

    #Total Lck
    lb4_1 = tk.Label(master = app , text = 'Total Lck')
    lb4_1.grid(row = 7 , column = 0 , padx = (0,0) , pady = (0,0))
    lb4_1.config(font = ('Tahoma' , 10))
        
    lb4_2 = tk.Label(master = app , text = '-')
    lb4_2.grid(row = 7 , column = 1 , padx = (0,0) , pady = (0,0))
    lb4_2.config(font = ('Tahoma' , 10))

    #Percent of Effect
    lb5_1 = tk.Label(master = app , text = 'Effect')
    lb5_1.grid(row = 8 , column = 0 , padx = (0,0) , pady = (0,5))
    lb5_1.config(font = ('Tahoma' , 10))

    lb5_2 = tk.Label(master = app , text = '- %')
    lb5_2.grid(row = 8 , column = 1 , padx = (0,0) , pady = (0,5))
    lb5_2.config(font = ('Tahoma' , 10))

    menuBar.add_cascade(label = 'Reset Program' , menu = '' , command = remove)
    menuBar.entryconfigure('Program' , state = 'disabled')


#def chaCal():

#ปรับการตั้งค่าโปรแกรม
app = tk.Tk()
app.title('Calculator Skill')
app.resizable(0,0)
#app.geometry('250x200')
#icon = PhotoImage(file = '')
#app.iconphoto(False,icon)

menuBar = tk.Menu(master = app)

#date
lb_date = tk.Label(master = app  , text = 'Current Date :')
lb_date.grid(row = 0 , column = 0 , padx = (5,0) , pady = (5,0))
lb_date.config(font = ('Tahoma' , 10))

current_date = tk.Label(master = app , text = 'Waiting...')
current_date.grid(row = 0 , column = 1 , padx = (0,5) , pady = (5,0))
current_date.config(font = ('Tahoma' , 10))

#time
lb_time = tk.Label(master = app , text = 'Current Time :')
lb_time.grid(row = 1 , column = 0 , padx = (5,0) , pady = (0,0))
lb_time.config(font = ('Tahoma' , 10))

current_time = tk.Label(master = app , text = 'Waiting...')
current_time.grid(row = 1 , column = 1 , padx = (0,5) , pady = (0,0))
current_time.config(font = ('Tahoma' , 10))

#Program Menu
menu_Program = tk.Menu(master = menuBar , tearoff = 0)
menu_Program.add_command(label = 'HP Drain Calculator' , command = hpDrainCal)
menu_Program.add_command(label = 'Effect Calculator' , command = EffectCal)
menu_Program.add_command(label = 'Cha Calculator' , command = '')
menu_Program.add_command(label = 'Original Cool Down Calculator' , command = '')
menu_Program.add_command(label = 'Cha Agi Optimization' , command = '')
menu_Program.add_command(label = 'TT&CO Success Rate' , command = '')
#menu_Program.add_separator()
menu_Program.add_command(label = 'Reset Program' , command = hpDrainCal)
menuBar.add_cascade(label = 'Program' , menu = menu_Program)

runThread = threading.Thread(target = runTime)
runThread.start()

app.config(menu = menuBar)
app.mainloop()
