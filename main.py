#!/usr/bin/env python
# -*- coding: utf8 -*-
from tkinter import *
import pandas as pd
from tkinter.filedialog import askopenfile
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageTk
import sqlite3
import os
from math import ceil
from functools import partial
import time
from datetime import datetime
class tkinterGUI(Frame):
    def __init__(self,parent,parent2):
        Frame.__init__(self,parent)
        self.database = parent2
        self.variables()
        self.initGui()

    def initGui(self):
        self.canvas = Canvas(self, width=1000, height=900)
        img = ImageTk.PhotoImage(Image.open('pics/g33961.png').resize((1000, 1000), Image.ANTIALIAS))  #
        self.canvas.background = img  #
        bg_pic = self.canvas.create_image(0, 0, anchor=NW, image=img)
        self.canvas.grid(row=0, column=0, rowspan=1000, columnspan=1000)

        y = 3
        label = Label(self, text=self.columns[0], anchor=W,bg="black",fg="white")
        self.canvas.create_window(20, 5+y, anchor=NW, window=label)

        label = Label(self, text=self.columns[1], anchor=W, bg="black", fg="white")
        self.canvas.create_window(70, 5+y, anchor=NW, window=label)

        label = Label(self, text=self.columns[2], anchor=W, bg="black", fg="white")
        self.canvas.create_window(200, 5+y, anchor=NW, window=label)

        label = Label(self, text=self.columns[3], anchor=W, bg="black", fg="white")
        self.canvas.create_window(340, 5+y, anchor=NW, window=label)

        label = Label(self, text=self.columns[4], anchor=W, bg="black", fg="white")
        self.canvas.create_window(477, 5+y, anchor=NW, window=label)

        label = Label(self, text=self.columns[5], anchor=W, bg="black", fg="white")
        self.canvas.create_window(580, 5+y, anchor=NW, window=label)

        label = Label(self, text=self.columns[6], anchor=W, bg="black", fg="white")
        self.canvas.create_window(770, 5+y, anchor=NW, window=label)

        label = Label(self, text="Ekle / Sil", anchor=W, bg="black", fg="white")
        self.canvas.create_window(920, 5+y, anchor=NW, window=label)


        y_column = 35
        label_no = Label(self, text="", anchor=W, bg="white", fg="white")
        self.canvas.create_window(20, y_column+5, anchor=NW, window=label_no)
        self.select_button_1 = Button(self,text = "İçe Aktar",command = lambda: self.open_file_xlxs(self.columns[1]))
        self.canvas.create_window(65, y_column, anchor=NW, window=self.select_button_1)
        self.select_button_2 = Button(self, text="İçe Aktar", command=lambda: self.open_file_xlxs(self.columns[2]))
        self.canvas.create_window(195, y_column, anchor=NW, window=self.select_button_2)
        self.select_button_3 = Button(self, text="İçe Aktar", command= lambda: self.open_file_xlxs(self.columns[3]))
        self.canvas.create_window(345, y_column, anchor=NW, window=self.select_button_3)
        self.select_button_4 = Button(self, text="İçe Aktar", command= lambda: self.open_file_xlxs(self.columns[4]))
        self.canvas.create_window(478, y_column, anchor=NW, window=self.select_button_4)

        self.select_button_6 = Button(self, text="İçe Aktar", command= lambda: self.open_file_xlxs(self.columns[6]))
        self.canvas.create_window(790, y_column, anchor=NW, window=self.select_button_6)

        self.select_button_7 = Button(self, text="Database", command=self.clear_database)
        self.canvas.create_window(910, y_column, anchor=NW, window=self.select_button_7)

        y_plus =45
        self.month_cb = Label(self,textvariable=str(self.counter))
        self.canvas.create_window(20, y_column + y_plus, anchor=NW, window=self.month_cb)

        self.names = ttk.Combobox(self, textvariable=self.stringVar[0],width=10)
        self.canvas.create_window(60, y_column+y_plus, anchor=NW, window=self.names)
        self.names.bind("<<ComboboxSelected>>", self.combobox_selected_event)

        self.section_code = ttk.Combobox(self, textvariable=self.stringVar[1], width=15)
        self.canvas.create_window(170, y_column + y_plus, anchor=NW, window=self.section_code)

        self.section_name = ttk.Combobox(self, textvariable=self.stringVar[2], width=15)
        self.canvas.create_window(320, y_column + y_plus, anchor=NW, window=self.section_name)

        self.shift = ttk.Combobox(self, textvariable=self.stringVar[3], width=10)
        self.canvas.create_window(470, y_column + y_plus, anchor=NW, window=self.shift)

        self.work = Text(self, height=4, width=23)
        self.canvas.create_window(580, y_column + y_plus-42, anchor=NW, window=self.work)

        self.from_ = ttk.Combobox(self, textvariable=self.stringVar[4], width=14)
        self.canvas.create_window(770, y_column + y_plus, anchor=NW, window=self.from_)

        self.add = Button(self, text="ADD",width=5,height=1,font =("Helvatica",7),command = self.add_people)
        self.canvas.create_window(920, y_column + y_plus-5, anchor=NW, window=self.add)

        #------------------------------------------------------------------------------------------------------------------------------------------
        self.excel_1 = Button(self, text="Import Exel", font=("Helvatica", 10), command=self.next_page)
        self.canvas.create_window(10, 855, anchor=NW, window=self.excel_1)

        self.excel_2 = Button(self, text="Export Exel -1", font=("Helvatica", 10), command=self.export_excel_1) # +
        self.canvas.create_window(120, 855, anchor=NW, window=self.excel_2)

        self.excel_3 = Button(self, text="Export Exel -2", font=("Helvatica", 10), command=self.next_page)
        self.canvas.create_window(245, 855, anchor=NW, window=self.excel_3)

        self.pdf_1 = Button(self, text="Export Pdf", font=("Helvatica", 10), command=self.export_pdf)
        self.canvas.create_window(370, 855, anchor=NW, window=self.pdf_1)
        # ------------------------------------------------------------------------------------------------------------------------------------------

        self.next_button = Button(self, text=">", font=("Helvatica", 10), command=self.next_page)
        self.canvas.create_window(950, 855, anchor=NW, window=self.next_button)

        self.back_button = Button(self, text="<", font=("Helvatica", 10), command=self.back_page)
        self.canvas.create_window(900, 855, anchor=NW, window=self.back_button)

        self.next_button = Button(self, text=">",font =("Helvatica",10), command=self.next_page)
        self.canvas.create_window(950, 855, anchor=NW, window=self.next_button)


        self.draw_lines()
        self.set_data()

        self.write_screen()

    def draw_lines(self):
        # dikey çizgiler
        self.canvas.create_line(2, 1, 2, 898, fill="black", width=2)
        self.canvas.create_line(48, 1, 48, 843, fill="black", width=2) #x1 y1 x2 y2
        self.canvas.create_line(163, 1, 163, 843, fill="black", width=2)
        self.canvas.create_line(312, 1, 312, 843, fill="black", width=2)
        self.canvas.create_line(465, 1, 465, 843, fill="black", width=2)
        self.canvas.create_line(573, 1, 573, 843, fill="black", width=2)
        self.canvas.create_line(760, 1, 760, 843, fill="black", width=2)
        self.canvas.create_line(907, 1, 907, 843, fill="black", width=2)
        self.canvas.create_line(998, 1, 998, 898, fill="black", width=2)
        #yatay çizgiler
        self.canvas.create_line(1, 2, 998, 2, fill="black", width=2)  # x1 y1 x2 y2
        self.canvas.create_line(1, 31, 998, 31, fill="black", width=2)
        self.canvas.create_line(1, 70, 998, 70, fill="black", width=2)
        self.canvas.create_line(1, 119, 998, 119, fill="black", width=5)

        self.canvas.create_line(1, 843, 998, 843, fill="black", width=5)
        self.canvas.create_line(1, 898, 998, 898, fill="black", width=2)
    def add_people(self):
        array = []
        array.append(str(self.people_counter))
        array.append(self.names.get())
        array.append(self.section_code.get())
        array.append(self.section_name.get())
        array.append(self.shift.get())
        array.append(self.work.get("1.0",END))
        array.append(self.from_.get())


        for i in array:
            if i == "":
                array = []
        if len(array) != 0:
            self.adding_people.append(array)
            self.people_counter += 1
            self.counter.set(self.people_counter)
            self.database.write_database(array)
            self.database.write_database_log(array)
            self.clear_page()
            self.clear_all_combobox()
    def combobox_selected_event(self,_):
        data = self.database.read_log(self.names.get())
        if len(data) != 0:
            counter = [0,0]
            for i in self.combobox_items[self.columns[2]]:
                if i == data[1]:
                    break
                else:
                    counter[0] += 1
            for i in self.combobox_items[self.columns[6]]:
                if i == data[2]:
                    break
                else:
                    counter[1] += 1
            self.section_code.set(self.combobox_items[self.columns[2]][counter[0]])
            self.from_.set(self.combobox_items[self.columns[6]][counter[1]])
    def variables(self):
        self.stringVar = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
        self.adding_people = []
        self.page_counter= [0,0]
        self.page_id_counter = []
        self.delete_button_id = [Button(self, text="")]
        self.columns = ['No',"Adı Soyadı","Bölüm Adı","Çalışacağı Bölüm","Fazla Mesai","Mesaide yapacağı iş","Kullanılan Servis"]
        self.combobox_items = {}
        for i in self.columns:
            self.combobox_items[i] = []
        self.people_counter = 1
        self.counter = IntVar()
        self.counter.set(self.people_counter)
    def open_file_xlxs(self,args):
        file = askopenfile(mode='r', filetypes=[("Excel Files", ".xlsx"), ("all files", ".*")])
        if file is not (None):
            file = str(file).split("'")[1]
            data = pd.read_excel(file)
            df = pd.DataFrame(data)
            first = ""
            for i in df:
                first = str(i)
            self.combobox_items[args].append(first)
            for i in df[str(first)]:
                self.combobox_items[args].append(str(i))
        print(self.combobox_items)
        if args == self.columns[1]:
            self.database.write_exel_data(1,self.combobox_items[args])
        elif args == self.columns[2]:
            self.database.write_exel_data(2, self.combobox_items[args])
        elif args == self.columns[3]:
            self.database.write_exel_data(3, self.combobox_items[args])
        elif args == self.columns[4]:
            self.database.write_exel_data(4, self.combobox_items[args])
        elif args == self.columns[6]:
            self.database.write_exel_data(6, self.combobox_items[args])
        self.set_data()
    def clear_all_combobox(self):
        self.names.set("")
        self.section_code.set("")
        self.section_name.set("")
        self.shift.set("")
        self.from_.set("")
        self.work.delete('1.0', END)
    def set_data(self):
        if (os.path.exists('kayitlar/logs')):
            if os.path.isfile('kayitlar/logs/config1.db'):
                data = self.database.read_database("config1.db")
                if len(data) != 0:
                    self.names['values'] = data
                    self.names.set("")
                    self.combobox_items[self.columns[1]] =data
            if os.path.isfile('kayitlar/logs/config2.db'):
                data = self.database.read_database("config2.db")
                if len(data) != 0:
                    self.section_code['values'] = data
                    self.section_code.set("")
                    self.combobox_items[self.columns[2]] =data
            if os.path.isfile('kayitlar/logs/config3.db'):
                data = self.database.read_database("config3.db")
                if len(data) != 0:
                    self.section_name['values'] = data
                    self.section_name.set("")
                    self.combobox_items[self.columns[3]] =data
            if os.path.isfile('kayitlar/logs/config4.db'):
                data = self.database.read_database("config4.db")
                if len(data) != 0:
                    self.shift['values'] = data
                    self.shift.set("")
                    self.combobox_items[self.columns[4]] =data
            if os.path.isfile('kayitlar/logs/config6.db'):
                data = self.database.read_database("config6.db")
                if len(data) != 0:
                    self.from_['values'] = data
                    self.from_.set("")
                    self.combobox_items[self.columns[6]] =data
    def write_screen(self,start=0):
        ret = self.database.read_draw_log()
        counter = 0
        self.people_counter = len(ret) +1
        self.counter.set(self.people_counter)
        loop_counter = 0
        self.page_counter[1] = ceil(len(ret)/24) - 1
        for i in ret:
            if loop_counter >= start*24:
                self.text_id = self.canvas.create_text(20, 135 + counter, fill="darkblue", font="Times 10 italic bold",text=i[0])
                self.page_id_counter.append(self.text_id )
                self.text_id = self.canvas.create_text(90, 135 + counter, fill="darkblue", font="Times 10 italic bold", text=i[1])
                self.page_id_counter.append(self.text_id)
                self.text_id = self.canvas.create_text(240, 135 + counter, fill="darkblue", font="Times 10 italic bold", text=i[2])
                self.page_id_counter.append(self.text_id)
                self.text_id= self.canvas.create_text(390, 135 + counter, fill="darkblue", font="Times 10 italic bold", text=i[3])
                self.page_id_counter.append(self.text_id)
                self.text_id= self.canvas.create_text(520, 135 + counter, fill="darkblue", font="Times 10 italic bold", text=i[4])
                self.page_id_counter.append(self.text_id)
                if len(i[5]) > 20:
                    text = str(i[5])[0:25]
                else:
                    text = str(i[5])
                self.text_id = self.canvas.create_text(665, 135 + counter, fill="darkblue", font="Times 10 italic bold", text=text)
                self.page_id_counter.append(self.text_id)

                self.text_id = self.canvas.create_text(830, 135 + counter, fill="darkblue", font="Times 10 italic bold", text=i[6])
                self.page_id_counter.append(self.text_id)

                delete_button = Button(self, text="X",command=partial(self.delete_people,i[0]),font =("Helvatica",8),height=1,width=1)
                self.text_id = self.canvas.create_window(935, 122 + counter, anchor=NW, window=delete_button)
                self.delete_button_id.append(delete_button)
                self.page_id_counter.append(self.text_id)

                self.text_id = self.canvas.create_line(1, 151 + counter, 998, 151 + counter, fill="black", width=2)
                self.page_id_counter.append(self.text_id)


                if counter > 680:
                    break
                counter += 30
            loop_counter += 1
    def clear_page(self):
        for i in self.page_id_counter:
            self.canvas.delete(i)
        self.page_id_counter = []
        self.write_screen(self.page_counter[0])
    def delete_people(self,id):
        self.database.delete_database_for_user(id)
        self.clear_page()
    def back_page(self):
        if self.page_counter[0] > 0:
            self.page_counter[0] -= 1
        self.clear_page()
        self.write_screen(self.page_counter[0])
    def next_page(self):
        if (self.page_counter[0] + 1) <= self.page_counter[1]:
            self.page_counter[0] += 1
        self.clear_page()



    def anytihng(self):
        print(1)
    def clear_database(self):
        #clear all database
        pass
    def export_excel_1(self):
        data = self.database.read_draw_log()

        self.dates = [[],[],[],[],[],[],[]]

        for i in data:
            self.dates[0].append(i[0])
            self.dates[1].append(i[1])
            self.dates[2].append(i[2])
            self.dates[3].append(i[3])
            self.dates[4].append(i[4])
            self.dates[5].append(i[5])
            self.dates[6].append(i[6])
        print(data)
        self.win = Toplevel()
        self.win.wm_title("Export Exel")
        self.win.geometry("300x100")

        self.exel_location = Label(self.win, text="Dosya Kayıt Konumu ")
        self.exel_location.grid(row=0, column=0)
        self.exel_location_entry = Entry(self.win)
        self.exel_location_entry.grid(row=0, column=1)
        self.exel_location_entry.insert(0,os.getcwd())


        self.exel_name = Label(self.win, text = "Dosyanın ismi ")
        self.exel_name.grid(row=1,column=0)
        self.exel_name_entry = Entry(self.win)
        self.exel_name_entry.grid(row=1,column=1)
        self.exel_name_entry.insert(0,datetime.now().strftime("%d-%m-%y_%H:%M:%S"))
        self.exel_name_button = Button(self.win,text = "Export",command=self.export_1)
        self.exel_name_button.grid(row=2,column=0,columnspan=2)
    def export_1(self):
        data = {}
        for i in range(0,len(self.columns)):
            data[self.columns[i]] = self.dates[i]
        df = pd.DataFrame(data,columns=self.columns)
        location = str(self.exel_location_entry.get()) + "/" + str(self.exel_name_entry.get()) + ".xlsx"
        df.to_excel(location, index=False, header=True)
        self.win.destroy()

    def export_pdf(self):
        pass
class database:
    def __init__(self):
        self.create_folders()
    def create_folders(self):
        if not (os.path.exists('kayitlar/')):
            os.mkdir('kayitlar/')
            if not (os.path.exists('kayitlar/logs')):
                os.mkdir('kayitlar/logs')
                self.create_database()
    def create_database(self):
        name_array = ["name","sec_code","sec_name","mesai","servis"]
        array = [1,2,3,4,6]
        for i in range(0,5):
            baglan = sqlite3.connect('kayitlar/logs/config'+str(array[i])+'.db')
            veri = baglan.cursor()
            veri.execute("""CREATE TABLE data ('""" + name_array[i] + """'     TEXT);""")
            baglan.commit()
            baglan.close()

        baglan = sqlite3.connect('kayitlar/logs/config0.db')
        veri = baglan.cursor()
        veri.execute("""CREATE TABLE data (
                                    'No'	 TEXT,
                                    'Ad_Soyad'	 TEXT,
                                    'Bolum_Kodu'      TEXT,
                                    'Calisma_Bolum' TEXT,
                                    'Mesai' TEXT,
                                    'is_time'     TEXT,
                                    'Servis' TEXT);""")
        baglan.commit()
        baglan.close()

        baglan = sqlite3.connect('kayitlar/logs/config5.db')
        veri = baglan.cursor()
        veri.execute("""CREATE TABLE data (
                                            'Ad_Soyad'	 TEXT,
                                            'Bolum_Kodu'      TEXT,
                                            'Servis' TEXT);""")
        baglan.commit()
        baglan.close()
    def write_exel_data(self,args,data):
        name_array = ["", "name","sec_code","sec_name","mesai","","servis"]
        baglan = sqlite3.connect('kayitlar/logs/config' + str(args) + '.db')
        veri = baglan.cursor()

        for i in data:
            buKisiEklimi = veri.execute("select exists(select * from data where " + name_array[args] + "= '" + str(i) + "')").fetchone()[0]
            if buKisiEklimi == 0:
                veri.execute("INSERT INTO data (" + name_array[args] + ") VALUES (?)", (i,))

        baglan.commit()
        baglan.close()
    def write_database(self,data):
        baglan = sqlite3.connect('kayitlar/logs/config0.db')
        veri = baglan.cursor()
        veri.execute("INSERT INTO data (No,Ad_Soyad,Bolum_Kodu,Calisma_Bolum,Mesai,is_time,Servis) VALUES (?,?,?,?,?,?,?)",(data[0],data[1],data[2],data[3],data[4],data[5],data[6],))
        baglan.commit()
        baglan.close()

    def write_database_log(self, data):
        baglan = sqlite3.connect('kayitlar/logs/config5.db')
        veri = baglan.cursor()
        buKisiEklimi = \
        veri.execute("select exists(select * from data where " + "Ad_Soyad" + "= '" + str(data[1]) + "')").fetchone()[0]
        if buKisiEklimi == 0:
            veri.execute(
                "INSERT INTO data (Ad_Soyad,Bolum_Kodu,Servis) VALUES (?,?,?)",(data[1], data[2], data[6],))
        baglan.commit()
        baglan.close()
    def read_database(self,database_name):
        data = []
        baglan = sqlite3.connect('kayitlar/logs/' +database_name)
        veri = baglan.cursor()
        res = veri.execute("SELECT * FROM data").fetchall()
        for i in res:
            data.append(i[0])
        baglan.commit()
        baglan.close()
        return data
    def read_log(self,name):
        baglan = sqlite3.connect('kayitlar/logs/config5.db')
        veri = baglan.cursor()
        res = veri.execute("SELECT * FROM data").fetchall()
        counter = 0
        for i in res:
            if i[0] == name:
                break
            else:
                counter +=1

        baglan.commit()
        baglan.close()
        if counter == len(res):
            return []
        else:
            return res[counter]
    def read_draw_log(self):
        baglan = sqlite3.connect('kayitlar/logs/config0.db')
        veri = baglan.cursor()
        res = veri.execute("SELECT * FROM data").fetchall()
        baglan.commit()
        baglan.close()
        if len(res) == 0:
            return []
        else:
            return res
    def delete_database_for_user(self,id):
        #try:
        baglan = sqlite3.connect('kayitlar/logs/config0.db')
        veri = baglan.cursor()
        sql_update_query = """DELETE from data where rowid = ?"""
        veri.execute(sql_update_query, (id,))
        baglan.commit()
        baglan.close()
        self.rebuild_database('kayitlar/logs/config0.db')
        #except:
        #    return False
        #return True
    def rebuild_database(self,address):
        data_ = []
        baglan = sqlite3.connect(address)
        veri = baglan.cursor()
        data = veri.execute("select * from data")
        for i in data:
            data_.append(i)
        baglan.commit()
        baglan.close()
        baglan = sqlite3.connect(address)
        veri = baglan.cursor()
        for i in data_:
            veri.execute("Delete from data where No='" + i[0] + "'")
        baglan.commit()
        baglan.close()
        counter = 1
        baglan = sqlite3.connect(address)
        veri = baglan.cursor()
        for data in data_:
            veri.execute(
                "INSERT INTO data (No,Ad_Soyad,Bolum_Kodu,Calisma_Bolum,Mesai,is_time,Servis) VALUES (?,?,?,?,?,?,?)",
                (counter, data[1], data[2], data[3], data[4], data[5], data[6],))
            counter += 1
        baglan.commit()
        baglan.close()
if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x900")
    root.config(bg="white")
    app = tkinterGUI(root,database())
    app.grid(row=0,column=0)
    root.mainloop()