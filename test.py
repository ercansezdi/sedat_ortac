# -*- coding: utf8 -*-
from fpdf import FPDF
import fpdf
import os
from datetime import datetime
from time import strftime

class pdf_generator:

    def __init__(self,data):
        self.data= data
        self.pdf = FPDF(orientation='L', unit='mm', format='A4')
        self.pdf.set_font("Arial")
        self.Tr2Eng = str.maketrans("çÇğGıİöÖşŞüÜ", "cCgGiIoOsSuU")

    def ayristirma(self,data):
        bolum_adlari = []
        for i in data:
            if i[3] not in bolum_adlari:
                bolum_adlari.append(i[3])
        ayristirlmis_data = {}
        for i in bolum_adlari:
            ayristirlmis_data[i] = []
        for i in data:
            ayristirlmis_data[i[3]].append(i)
        return ayristirlmis_data
    def create_pdf(self,name, location=os.getcwd()):
        self.pdf.add_page()
        self.create_header()
        new_data = self.ayristirma(self.data)
        sec_names = ["Bölüm", "no", "adı soyadı", "bölüm kodu", "fazla","mesai", "mesaide yapılacak işler",
                     "kullanılan servis"]
        array = ['iç montaj', 'kalite güvence', 'plastik spiral ve çelik spiral', 'sayımhane ', 'idari işler', 'kalıphane', 'dsdsd']

        counterx = [0,0]
        countery = 0
        name_counter =0
        header_len = 16
        space = 20
        self.pdf.set_font_size(8)
        dikey_extra = 0
        for data_names in new_data:

            if ((countery +len(new_data[array[name_counter]]) * 5 + header_len + space)> 200):
                if counterx[0] == 0:
                    countery = 0
                    counterx = [1,150]
                else:
                    countery = 0
                    counterx = [0, 0]
                    self.pdf.add_page()
                    self.create_header()

            self.create_work_header(sec_names, data_names,ykaydirma=countery,xkaydirma=counterx[1])
            self.create_wowk_lines(countery * 2, counterx[1] * 2,
                                   dikey_eksen_uzunlugu=(len(new_data[array[name_counter]]) * 5))
            dikey_extra = 0

            for data in new_data[data_names]:
                print(data)
                print((countery +len(new_data[array[name_counter]]) * 5 + header_len ))
                if ((countery + len(new_data[array[name_counter]]) * 5 + header_len) > 200):
                    if counterx[0] == 0:
                        countery = 0
                        counterx = [1, 150]
                    else:
                        countery = 0
                        counterx = [0, 0]
                        self.pdf.add_page()
                        self.create_header()
                        self.create_work_header(sec_names, data_names, ykaydirma=countery, xkaydirma=counterx[1])
                        self.create_wowk_lines(countery * 2, counterx[1] * 2)
                        dikey_extra = 0

                extra = self.write_text(data,ykaydirma=countery,xkaydirma=counterx[1])
                countery += (5 + extra)
                dikey_extra += extra



            countery += 20
            #self.pdf.line(142 + xkaydirma, 37 + ykaydirma, 142 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
            name_counter +=1



        #self.pdf.line(151, 40, 293, 40)
        self.pdf.output(location + "/" + name + ".pdf")
    def create_work_header(self,sec_names,sec_name,ykaydirma=0,xkaydirma=0):
        self.pdf.set_font_size(8)
        self.pdf.text(55 + xkaydirma, 41+ykaydirma,(sec_names[0] + ":     " + sec_name).upper().translate(self.Tr2Eng))
        self.pdf.text( 5+ xkaydirma, 49 + ykaydirma, (sec_names[1]).upper().translate(self.Tr2Eng))
        self.pdf.text(15 + xkaydirma, 49 + ykaydirma, (sec_names[2]).upper().translate(self.Tr2Eng))
        self.pdf.text(36 + xkaydirma, 49 + ykaydirma, (sec_names[3]).upper().translate(self.Tr2Eng))
        self.pdf.text(60 + xkaydirma, 47 + ykaydirma, (sec_names[4]).upper().translate(self.Tr2Eng))
        self.pdf.text(60 + xkaydirma, 51 + ykaydirma, (sec_names[5]).upper().translate(self.Tr2Eng))
        self.pdf.text(73 + xkaydirma, 49 + ykaydirma, (sec_names[6]).upper().translate(self.Tr2Eng))
        self.pdf.text(113 + xkaydirma, 49 + ykaydirma, (sec_names[7]).upper().translate(self.Tr2Eng))


    def create_wowk_lines(self,ykaydirma=0,xkaydirma=0,dikey_eksen_uzunlugu=0):
        xkaydirma /= 2
        ykaydirma /= 2
        # yataylar
        self.pdf.line(2+xkaydirma, 37+ykaydirma, 142+xkaydirma, 37+ykaydirma)
        self.pdf.line(2+xkaydirma, 43+ykaydirma, 142+xkaydirma, 43+ykaydirma)
        self.pdf.line(2+xkaydirma, 53+ykaydirma, 142+xkaydirma, 53+ykaydirma)
        #dikeyler
        self.pdf.line(2+xkaydirma, 37+ykaydirma, 2+xkaydirma, 53+ykaydirma+dikey_eksen_uzunlugu)
        self.pdf.line(12+xkaydirma, 43+ykaydirma, 12+xkaydirma, 53+ykaydirma+dikey_eksen_uzunlugu)
        self.pdf.line(33+xkaydirma, 43+ykaydirma, 33+xkaydirma, 53+ykaydirma+dikey_eksen_uzunlugu)
        self.pdf.line(57+xkaydirma, 43+ykaydirma, 57+xkaydirma, 53+ykaydirma+dikey_eksen_uzunlugu)
        self.pdf.line(72+xkaydirma, 43+ykaydirma, 72+xkaydirma, 53+ykaydirma+dikey_eksen_uzunlugu)
        self.pdf.line(112+xkaydirma, 43+ykaydirma, 112+xkaydirma, 53+ykaydirma+dikey_eksen_uzunlugu)
        self.pdf.line(142+xkaydirma, 37+ykaydirma, 142+xkaydirma, 53+ykaydirma+dikey_eksen_uzunlugu)
    def create_work_header_columns(self,ykaydirma=0,xkaydirma=0,dikey_eksen_uzunlugu=0):
        self.pdf.line(2 + xkaydirma, 37 + ykaydirma, 2 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
        self.pdf.line(12 + xkaydirma, 43 + ykaydirma, 12 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
        self.pdf.line(33 + xkaydirma, 43 + ykaydirma, 33 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
        self.pdf.line(57 + xkaydirma, 43 + ykaydirma, 57 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
        self.pdf.line(72 + xkaydirma, 43 + ykaydirma, 72 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
        self.pdf.line(112 + xkaydirma, 43 + ykaydirma, 112 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
        self.pdf.line(142 + xkaydirma, 37 + ykaydirma, 142 + xkaydirma, 53 + ykaydirma + dikey_eksen_uzunlugu)
    def split_by_space(self,text,karekter_siniri):

        space = text.count(" ")
        text = text.split(" ")
        return_text = []
        counter = 0
        text_ = ""
        while counter < space:
            if len(text) > counter:
                if len(text_ + " " + text[counter]) > karekter_siniri:
                    return_text.append(text_)
                    text_ = text[counter]
                else:
                    text_ += (" " +text[counter])
            counter += 1

        return_text.append(text_)

        return return_text
    def split_by_lenght(self,text,karekter_siniri):
        text_ = ""
        return_text = []
        for i in text:
            text_ += i
            if len(text_) == karekter_siniri:
                return_text.append(text_)
                text_ = ""
        if text_ != "":
            return_text.append(text_)
        return return_text
    def align(self, sec_names, ykaydirma=0, xkaydirma=0):
        self.pdf.set_font_size(7)
        fake_ykaydirma = 0
        fake_ykaydirma_2 = 0
        control = [0,0,0,0,0,0,0]
        text = sec_names[5].translate(self.Tr2Eng)
        if len(text) > 34:
            result = self.split_by_space(text, 34)
            for i in result:
                fake_ykaydirma_2 += 2.5

        if fake_ykaydirma_2 > fake_ykaydirma:
            fake_ykaydirma = fake_ykaydirma_2
            fake_ykaydirma_2 = 0
        control[5] = fake_ykaydirma

        text = (sec_names[1]).translate(self.Tr2Eng)
        if len(text) > 12:
            result = self.split_by_space(text,15)
            for text in result:
                fake_ykaydirma_2 +=2
        else:
            pass
        control[1] = fake_ykaydirma_2
        if fake_ykaydirma_2 > fake_ykaydirma:
            fake_ykaydirma = fake_ykaydirma_2
            fake_ykaydirma_2 = 0

        text = (sec_names[2]).translate(self.Tr2Eng)
        if len(text) > 12:
            result = self.split_by_space(text, 15)
            for text in result:
                fake_ykaydirma_2 += 2
        control[2] = fake_ykaydirma_2
        if fake_ykaydirma_2 > fake_ykaydirma:
            fake_ykaydirma = fake_ykaydirma_2
            fake_ykaydirma_2 = 0


        text = (sec_names[6]).translate(self.Tr2Eng)
        if len(text) > 31:
            result = self.split_by_space(text, 27)
            for text in result:
                fake_ykaydirma_2 += 2
        control[6] = fake_ykaydirma_2

        if fake_ykaydirma_2 > fake_ykaydirma:
            fake_ykaydirma = fake_ykaydirma_2
            fake_ykaydirma_2 = 0
        return  control,fake_ykaydirma
    def write_text(self, sec_names, ykaydirma=0, xkaydirma=0):
        control,align = self.align(sec_names,ykaydirma,xkaydirma)
        align = max(control)

        #align = control.sort()
        self.pdf.set_font_size(6)
        fake_ykaydirma = 0
        fake_ykaydirma_2 = 0
        #------------------------------------------------------------
        text = sec_names[5].translate(self.Tr2Eng) # mesaide yapılacka işler
        if control[5] == align:
            ortalama=0
        else:
            ortalama = align
        if len(text) > 34:
            result = self.split_by_space(text, 34)
            for i in result:
                self.pdf.text(73 + xkaydirma, 57 + ykaydirma + fake_ykaydirma+ortalama/2, (i))
                fake_ykaydirma += 2.5
        else:
            self.pdf.text(73 + xkaydirma, 55 + ykaydirma + ortalama/2, (text))
        # ------------------------------------------------------------
        ortalama = align
        if int(sec_names[0]) > 99:
            self.pdf.text(4 + xkaydirma, 55 + ykaydirma+ortalama/2, (sec_names[0]))
        elif int(sec_names[0]) > 9:
            self.pdf.text(5 + xkaydirma, 55 + ykaydirma+ortalama/2, (sec_names[0]))
        else:
            self.pdf.text(5 + xkaydirma, 55 + ykaydirma+ortalama/2, (sec_names[0]))
        # ------------------------------------------------------------
        text = (sec_names[1]).translate(self.Tr2Eng) #adi soyadi
        if control[1] == align:
            ortalama=0
        else:
            ortalama = align
        if len(text) > 15:
            result = self.split_by_space(text,15)
            for text in result:
                self.pdf.text(13 + xkaydirma, 55 + ykaydirma+fake_ykaydirma_2+ortalama/2, text)
                fake_ykaydirma_2 +=2
        else:
            self.pdf.text(13 + xkaydirma, 55 + ykaydirma+ortalama/2, text)
        # ------------------------------------------------------------
        text = (sec_names[2]).translate(self.Tr2Eng) # bolum kodu
        if control[2] == align:
            ortalama = 0
        else:
            ortalama = align
        if len(text) > 24:
            result = self.split_by_space(text, 24)
            for text in result:
                self.pdf.text(33 + xkaydirma, 55 + ykaydirma+fake_ykaydirma_2+ortalama/2, text)
                fake_ykaydirma_2 += 2
        else:
            self.pdf.text(34 + xkaydirma, 56 + ykaydirma + ortalama/2, text)
        # ------------------------------------------------------------
        text = str(sec_names[4]) # fazla mesai
        if len(text) > 1:
            text = text.split("-")
            self.pdf.text(62 + xkaydirma, 54 + ykaydirma+ortalama/2, (text[0].strip()))
            self.pdf.text(62 + xkaydirma, 56 + ykaydirma+ortalama/2, (text[1].strip()))
        else:
            self.pdf.text(64 + xkaydirma, 56 + ykaydirma+ortalama/2, (sec_names[4]))

        # ------------------------------------------------------------
        self.pdf.text(113 + xkaydirma, 56 + ykaydirma+ortalama/2, (sec_names[6]).translate(self.Tr2Eng)) # kullanılan servis
        # ------------------------------------------------------------

        self.pdf.line(2 + xkaydirma, 58 + ykaydirma+align, 142 + xkaydirma, 58 + ykaydirma+align)
        self.create_work_header_columns(xkaydirma=xkaydirma,ykaydirma=ykaydirma,dikey_eksen_uzunlugu=align+5)



        return align
    def create_header(self):
        # header
        # yataylar

        self.pdf.line(2, 3, 295, 3)  # x1 y1 x2 y2
        self.pdf.image("pics/ortac.png", x=5, y=5, w=37, h=14)
        self.pdf.line(2, 23, 295, 23)
        self.pdf.line(2, 30, 295, 30)
        for i in range(0, 21, 5):
            self.pdf.line(200, 3 + i, 295, 3 + i)
        # dikeyler
        self.pdf.line(2, 3, 2, 30)
        self.pdf.line(45, 3, 45, 23)
        self.pdf.line(200, 3, 200, 23)
        self.pdf.line(295, 3, 295, 30)

        # yazılar

        self.pdf.set_font_size(15)
        self.pdf.text(70, 15, "FAZLA MESAI YOL YEMEK MASRAF FORMU")
        self.pdf.set_font_size(10)
        self.pdf.text(220, 7,"Yayin Tarihi : 15.03.2012")
        self.pdf.text(220, 12, "Rev. No:2")
        self.pdf.text(220, 17, "Rev. Tarihi: 15.08.2018")
        self.pdf.text(220, 22, "Sayfa : 1/1")
        self.pdf.set_font_size(20)
        self.pdf.text(100, 29, str(datetime.now().strftime("%d %B %y %A")))
if __name__ == "__main__":
    #assadasdsadasdassadasdsadasdassadasdsadasdassadasdsadasdassadasdsadasdassadasdsadasdassadasdsadasdassadasdsadasd
    data = [('100', 'ahmetah metahmet ahmet ahmet ahmet', '3. kat depo elemanı', 'iç montaj', '4', 'adadadadad|adadadadad|adadada', 'letters in a given string000000'), ('2', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('3', 'muhammet', 'iç montaj sorumlusu', 'plastik spiral ve çelik spiral', '21:00- 08:00', 'dadadadad', 'arnavutköy'), ('4', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', \
            'If you want the counts for a lot of the letters in a given string, Counter provides them all in a more succinct form. If you want the count for one letter from a lot of different strings.', 'bahçelievler'), ('5', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('6', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('7', 'ahmet ', '3. kat depo elemanı 3. kat depo elemanı 3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('8', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('9', 'muhammet', 'iç montaj sorumlusu', 'plastik spiral ve çelik spiral', '21:00- 08:00', 'dadadadad', 'arnavutköy'), ('10', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('11', 'ahmetahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('12', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('13', 'muhammet', 'iç montaj sorumlusu', 'plastik spiral ve çelik spiral', '21:00- 08:00', 'dadadadad', 'arnavutköy'), ('14', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('15', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('16', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('17', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('18', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('19', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('20', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('21', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('22', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('23', 'muhammet', 'iç montaj sorumlusu', 'plastik spiral ve çelik spiral', '21:00- 08:00', 'dadadadad', 'arnavutköy'), ('24', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('25', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('26', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('27', 'muhammet', 'iç montaj sorumlusu', 'plastik spiral ve çelik spiral', '21:00- 08:00', 'dadadadad', 'arnavutköy'), ('28', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('29', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('30', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('31', 'muhammet', 'iç montaj sorumlusu', 'plastik spiral ve çelik spiral', '21:00- 08:00', 'dadadadad', 'arnavutköy'), ('32', 'aman', '2. kat depo elemanı', 'sayımhane ', '6', '+55+4654655', 'esenyurt'), ('33', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('34', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('35', 'muhammet', 'iç montaj sorumlusu', 'plastik spiral ve çelik spiral', '21:00- 08:00', 'dadadadad', 'arnavutköy'), ('36', 'ahmet ', '3. kat depo elemanı', 'iç montaj', '4', 'assadasdsadasd', 'bahçelievler'), ('37', 'engin', 'çelik spiral oprt.', 'kalite güvence', '4', '242424', 'esenyurt'), ('38', 'mardon ', 'plastik spiral sorumlusu ', 'plastik spiral ve çelik spiral', '18:00-08:00', 'asdsadsadsad\n', 'kıraç'), ('39', 'sezai ', 'iç montaj sorumlusu', 'idari işler', '5', 'asdsadsadsad\n', 'kıraç'), ('40', 'sezai ', 'iç montaj sorumlusu', 'idari işler', '5', 'asdsadsadsad\n', 'kıraç'), ('41', 'sezai ', 'iç montaj sorumlusu', 'idari işler', '5', 'asdsadsadsad\n', 'kıraç'), ('42', 'ahmet ', 'plastik spiral sorumlusu ', 'plastik spiral ve çelik spiral', '18:00-08:00', 'jjsjsj\n', 'hadımköy'), ('43', 'ahmet ', 'plastik spiral sorumlusu ', 'plastik spiral ve çelik spiral', '18:00-08:00', 'jjsjsj\n', 'hadımköy'), ('44', 'sezai ', 'iç montaj sorumlusu', 'kalıphane', '2', 'dsdsdsdsd\n', 'kıraç'), ('45', 'aydın ', 'sdsd', 'dsdsd', '4', 'dsdsdsdsd\n', 'bahçelievler')]
    pdf = pdf_generator(data)
    pdf.create_pdf("ercan")
