import tkinter as tk
from datetime import datetime
import time
import threading
import os
import pandas as pd
from getTime import getTime

#def bot(roomID , count):
    

#เวลาบนโปรแกรม
def runTime():
    while True:
        current_time['text'] = getTime('time')
        current_date['text'] = getTime('date')
        time.sleep(0.1)

#เมนูอัพเดทข้อมูล
def updateData():
    readData = pd.read_excel('Data.xlsx')
    getGaosData = readData.iloc[0,1]
    getMuradData = readData.iloc[1,1]

    lb_GaosValue['text'] = getGaosData
    lb_MuradValue['text'] = getMuradData

#เพิ่มจำนวนหัวใจกาออส
def addGaos():
    Value = int(get_Value.get())
    readHistory = pd.read_excel('History.xlsx')
    newHistory = pd.DataFrame({'Date' : [getTime('date')] , 'Time' : [getTime('time')] , 'Item List' : ['หัวใจกาออส'] , 'Value' : [Value]})
    updateHistory = [readHistory , newHistory]
    resultHistory = pd.concat(updateHistory)
    writeHistory = pd.ExcelWriter('History.xlsx',engine='xlsxwriter')
    resultHistory.to_excel(writeHistory,index = False)
    writeHistory.save()

    readData = pd.read_excel('Data.xlsx')
    getData = readData.loc[0,['Value']]
    datatoNum = int(getData)
    newData = datatoNum + Value
    readData.loc[0,['Value']] = [newData]
    editData = readData
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    editData.to_excel(writeData,index = False)
    writeData.save()

    lb_GaosValue['text'] = newData

#ลดจำนวนหัวใจกาออส
def removeGaos():
    Value = int(get_Value.get())
    NValue = '-' + str(Value)
    readHistory = pd.read_excel('History.xlsx')
    newHistory = pd.DataFrame({'Date' : [getTime('date')] , 'Time' : [getTime('time')] , 'Item List' : ['หัวใจกาออส'] , 'Value' : [NValue]})
    updateHistory = [readHistory , newHistory]
    resultHistory = pd.concat(updateHistory)
    writeHistory = pd.ExcelWriter('History.xlsx',engine='xlsxwriter')
    resultHistory.to_excel(writeHistory,index = False)
    writeHistory.save()

    readData = pd.read_excel('Data.xlsx')
    getData = readData.loc[0,['Value']]
    datatoNum = int(getData)
    newData = datatoNum - Value
    readData.loc[0,['Value']] = [newData]
    editData = readData
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    editData.to_excel(writeData,index = False)
    writeData.save()

    lb_GaosValue['text'] = newData

#เพิ่มจำนวนแร่ไฟ
def addMurad():
    Value = int(get_Value.get())
    readHistory = pd.read_excel('History.xlsx')
    newHistory = pd.DataFrame({'Date' : [getTime('date')] , 'Time' : [getTime('time')] , 'Item List' : ['แร่ไฟ'] , 'Value' : [Value]})
    updateHistory = [readHistory , newHistory]
    resultHistory = pd.concat(updateHistory)
    writeHistory = pd.ExcelWriter('History.xlsx',engine='xlsxwriter')
    resultHistory.to_excel(writeHistory,index = False)
    writeHistory.save()

    readData = pd.read_excel('Data.xlsx')
    getData = readData.loc[1,['Value']]
    datatoNum = int(getData)
    newData = datatoNum + Value
    readData.loc[1,['Value']] = [newData]
    editData = readData
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    editData.to_excel(writeData,index = False)
    writeData.save()

    lb_MuradValue['text'] = newData

#ลดจำนวนแร่ไฟ
def removeMurad():
    Value = int(get_Value.get())
    NValue = '-' + str(Value)
    readHistory = pd.read_excel('History.xlsx')
    newHistory = pd.DataFrame({'Date' : [getTime('date')] , 'Time' : [getTime('time')] , 'Item List' : ['แร่ไฟ'] , 'Value' : [NValue]})
    updateHistory = [readHistory , newHistory]
    resultHistory = pd.concat(updateHistory)
    writeHistory = pd.ExcelWriter('History.xlsx',engine='xlsxwriter')
    resultHistory.to_excel(writeHistory,index = False)
    writeHistory.save()

    readData = pd.read_excel('Data.xlsx')
    getData = readData.loc[1,['Value']]
    datatoNum = int(getData)
    newData = datatoNum - Value
    readData.loc[1,['Value']] = [newData]
    editData = readData
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    editData.to_excel(writeData,index = False)
    writeData.save()

    lb_MuradValue['text'] = newData

#ปรับการตั้งค่าโปรแกรม
app = tk.Tk()
app.title('Item for Sell and Pricelist')
app.resizable(0,0)
app.geometry('250x200')
icon = tk.PhotoImage(file = 'D:\\Python\\12 หาง\\Sell_Item\\diamond_carrot.png')
app.iconphoto(False,icon)

menuBar = tk.Menu(master = app)

#File Menu
menu_File = tk.Menu(master = menuBar , tearoff = 0)
menu_File.add_command(label = 'Update' , command = updateData)
#menu_File.add_command(label = 'Open')
#menu_File.add_command(label = 'Save')
#menu_File.add_command(label = 'Save as')
#menu_File.add_separator()
#menu_File.add_command(label = 'Exit' , command = app.quit)
menuBar.add_cascade(label = 'File' , menu = menu_File)

#Edit Menu
menu_Edit = tk.Menu(master = menuBar , tearoff = 0)
#menu_Edit.add_command(label = 'Undo' , command = test)
#menu_Edit.add_command(label = 'Redo')
#menuBar.add_cascade(label = 'Edit' , menu = menu_Edit)

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

#รายการไอเท็ม
lb_Itemlist = tk.Label(master = app , text = 'รายการไอเท็ม')
lb_Itemlist.grid(row = 2 , column = 0 , padx = (5,5) , pady = (10,0))
lb_Itemlist.config(font = ('Tahoma' , 10))

lb_Gaos = tk.Label(master = app , text = 'หัวใจกาออส')
lb_Gaos.grid(row = 3 , column = 0 , padx = (5,5) , pady = (5,0))
lb_Gaos.config(font = ('Tahoma' , 10))

lb_Murad = tk.Label(master = app , text = 'แร่ไฟ')
lb_Murad.grid(row = 4 , column = 0 , padx = (5,5) , pady = (0,0))
lb_Murad.config(font = ('Tahoma' , 10))

#จำนวนที่มี
lb_Value = tk.Label(master = app , text = 'จำนวน')
lb_Value.grid(row = 2 , column = 1 , padx = (5,5) , pady = (10,0))
lb_Value.config(font = ('Tahoma' , 10))

lb_GaosValue = tk.Label(master = app , text = '-')
lb_GaosValue.grid(row = 3 , column = 1 , padx = (5,5) , pady = (5,0))
lb_GaosValue.config(font = ('Tahoma' , 10))

lb_MuradValue = tk.Label(master = app , text = '-')
lb_MuradValue.grid(row = 4 , column = 1 , padx = (5,5) , pady = (0,0))
lb_MuradValue.config(font = ('Tahoma' , 10))

#ปุ่มเพิ่มไอเท็ม
bt_addGaos = tk.Button(master = app , text = 'เพิ่ม' , command = addGaos)
bt_addGaos.grid(row = 3 , column = 2 , padx = (0,0) , pady = (5,0))
bt_addGaos.config(font = ('Tahoma' , 8))

bt_addMurad = tk.Button(master = app , text = 'เพิ่ม' , command = addMurad)
bt_addMurad.grid(row = 4 , column = 2 , padx = (0,0) , pady = (0,0))
bt_addMurad.config(font = ('Tahoma' , 8))

#ปุ่มลดไอเท็ม
bt_removeGaos = tk.Button(master = app , text = 'ลด' , command = removeGaos)
bt_removeGaos.grid(row = 3 , column = 3 , padx = (15,0) , pady = (5,0))
bt_removeGaos.config(font = ('Tahoma' , 8))

bt_removeMurad = tk.Button(master = app , text = 'ลด' , command = removeMurad)
bt_removeMurad.grid(row = 4 , column = 3 , padx = (15,0) , pady = (0,0))
bt_removeMurad.config(font = ('Tahoma' , 8))

#ช่องใส่จำนวน
lb_getValue = tk.Label(master = app , text = 'จำนวนที่ต้องการ')
lb_getValue.grid(row = 5 , column = 0 , padx = (5,0) , pady = (20,0))
lb_getValue.config(font = ('Tahoma' , 10))

get_Value = tk.Entry(master = app , width = 5)
get_Value.grid(row = 5 , column = 1 , padx = (5,5) , pady = (20,0))

runThread = threading.Thread(target = runTime)
runThread.start()

app.config(menu = menuBar)
app.mainloop()
