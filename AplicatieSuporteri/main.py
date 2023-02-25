import tkinter as tk
import traceback
from tkinter import font
from PIL import ImageTk, Image
import cx_Oracle
from tkinter import ttk



def seteazaValoriActualePacient(e=None):
    nume = app.patient.pacientC.get()

    for i in app.patient.pacienti:
        if nume.__contains__(str(i)):
            nr = i
            try:
                app.cursor.execute('select * from suporter where nrtelefon = ' + nr)
                date = app.cursor.fetchall()
                app.patient.numeT.delete("1.0", "end")
                app.patient.numeT.insert(tk.END, date[0][1])

                app.patient.prenumeT.delete("1.0", "end")
                app.patient.prenumeT.insert(tk.END, date[0][2])


                app.patient.telefonT.delete("1.0", "end")
                app.patient.telefonT.insert(tk.END, date[0][3])

            except IndexError:
                open_popupEror('Selectati un element de modificat!\nCaseta vida!')
            except cx_Oracle.DatabaseError:
                open_popupEror('Selectati un element de modificat!\nCaseta vida!')


def modificaPacient(e=None):
    nume = app.patient.pacientC.get()
    app.patient.pacientC.set('')

    for i in app.patient.pacienti:
        if nume.__contains__(str(i)):
            nr = i
            try:
                app.patient.inserareNume = app.patient.numeT.get("1.0", "end")
                app.patient.inserarePrenume = app.patient.prenumeT.get("1.0", "end")
                app.patient.inserareTelefon = app.patient.telefonT.get("1.0", "end")


                app.patient.inserareNume = app.patient.inserareNume.replace('\n', '')
                app.patient.inserarePrenume = app.patient.inserarePrenume.replace('\n', '')
                app.patient.inserareTelefon = app.patient.inserareTelefon.replace(' ', '').replace('\n', '')


                app.cursor.execute(
                    'update suporter set nume = \'' + app.patient.inserareNume + '\' where nrtelefon = ' + nr)
                app.cursor.execute('update suporter set email = \'' + app.patient.inserarePrenume + '\' where '
                                                                                                     'nrtelefon = '
                                                                                                     '' + nr)
                app.cursor.execute(
                    'update suporter set nrtelefon = \'' + app.patient.inserareTelefon + '\' where nrtelefon = ' + nr)


                app.cursor.execute('COMMIT')
                app.patient.numeT.delete("0.0", "end")
                app.patient.prenumeT.delete("0.0", "end")
                app.patient.telefonT.delete("0.0", "end")
                open_popup('Datele au fost modificate cu succes!')
                valori1 = []
                app.patient.pacienti = []
                app.cursor.execute('select nume,email,nrtelefon from suporter order by suporter_id asc')
                rows = app.cursor.fetchall()
                app.patient.pacienti = []
                for i in rows:
                    app.patient.pacienti.append(i[2])
                    valori1.append(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))

                app.patient.pacientC['values'] = valori1  # se vor citi din baza de date
            except IndexError:
                open_popupEror('Selectati un element de sters!\nCaseta vida!')
                traceback.print_exc()
            except Exception as e:
                open_popupEror('Exista campuri necompletate sau cu valori eronate!')
                traceback.print_exc()

def modificaEveniment(e=None):
    nume = app.eveniment.evenimentC.get()
    app.eveniment.evenimentC.set('')

    for i in app.eveniment.evenimente:
        if nume.__contains__(str(i)):
            nr = i
            try:
                app.eveniment.inserareNume = app.eveniment.numeT.get("1.0", "end")
                app.eveniment.inserareNume = app.eveniment.inserareNume.replace('\n', '')
                app.cursor.execute(
                    'update eveniment set nume = \'' + app.eveniment.inserareNume + '\' where nume = ' + nr)

                app.cursor.execute('COMMIT')
                app.eveniment.numeT.delete("0.0", "end")
                app.eveniment.prenumeT.delete("0.0", "end")
                app.eveniment.telefonT.delete("0.0", "end")
                open_popup('Datele au fost modificate cu succes!')
                valori1 = []
                app.patient.pacienti = []
                app.cursor.execute('select nume,email,nrtelefon from suporter order by suporter_id asc')
                rows = app.cursor.fetchall()
                app.patient.pacienti = []
                for i in rows:
                    app.patient.pacienti.append(i[2])
                    valori1.append(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))

                app.patient.pacientC['values'] = valori1  # se vor citi din baza de date
            except IndexError:
                open_popupEror('Selectati un element de sters!\nCaseta vida!')
                traceback.print_exc()
            except Exception as e:
                open_popupEror('Exista campuri necompletate sau cu valori eronate!')
                traceback.print_exc()


def stergerePacient():
    nume = app.patient.pacientC.get()
    app.patient.pacientC.set('')
    for i in app.patient.pacienti:
        if nume.__contains__(str(i)):
            nr = i
            try:
                app.cursor.execute('delete from suporter where nrtelefon=' + str(nr))
                app.cursor.execute('commit')
                open_popup("Datele au fost sterse!")
                valori1 = []
                app.patient.pacienti = []
                app.cursor.execute('select nume,email,nrtelefon from suporter order by suporter_id asc')
                rows = app.cursor.fetchall()
                app.patient.pacienti = []
                for i in rows:
                    app.patient.pacienti.append(i[2])
                    valori1.append(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))
                app.patient.pacientC['values'] = valori1  # se vor citi din baza de date
            except IndexError:
                open_popupEror('Selectati un element de sters!\nCaseta vida!')
            except cx_Oracle.IntegrityError:
                open_popupEror('Nu poate fi sters.')


def printPacienti():
    try:
        app.cursor.execute('select * from suporter order by suporter_ID')
        rows = app.cursor.fetchall()
        name = ('ID', 'Nume', 'E-mail','Numar de telefon')
        ...
        nrelemente = int(app.height / (12 * 3))

        if app.patient.page > (len(rows) / nrelemente):
            app.patient.page = int(len(rows) / nrelemente)

        if app.patient.page < 0:
            app.patient.page = 0

        indexStat = app.patient.page * nrelemente
        indexStop = app.patient.page * nrelemente + nrelemente

        if indexStop > len(rows):
            indexStop = len(rows)

        for j in range(4):
            e = tk.Entry(app, width=(int(app.width / 50)), fg='blue', font=('Arial', 12, 'bold'), background='white')
            e.place(x=j * (app.width / 10) + (app.width / 10), y=((app.height / 3) - (int(app.width / 80))))
            e.insert(tk.END, name[j])
            app.patient.table.append(e)

        for i in range(indexStat, indexStop):
            for j in range(4):
                if j == 3:
                    e = tk.Entry(app, width=(int(app.width / 50)), fg='black', font=('Arial', 12, 'bold'),
                                 background='white')
                else:
                    e = tk.Entry(app, width=(int(app.width / 90)), fg='black', font=('Arial', 12, 'bold'),
                                 background='white')
                e.place(x=j * (app.width / 10) + (app.width / 10),
                        y=(i % nrelemente) * (int(app.width / 80)) + (app.height / 3))
                try:
                    e.insert(tk.END, rows[i][j])
                    app.patient.table.append(e)
                except:
                    app.patient.table.append(e)

    except cx_Oracle.DatabaseError as e:
        print(e)

def printEvenimente():
    try:
        app.cursor.execute('select * from eveniment order by eveniment_ID')
        rows = app.cursor.fetchall()
        name = ('ID', 'Nume')
        # print(rows)

        nrelemente = int(app.height / (12 * 3))

        if app.eveniment.page > (len(rows) / nrelemente):
            app.eveniment.page = int(len(rows) / nrelemente)

        if app.eveniment.page < 0:
            app.eveniment.page = 0

        indexStat = app.eveniment.page * nrelemente
        indexStop = app.eveniment.page * nrelemente + nrelemente

        if indexStop > len(rows):
            indexStop = len(rows)

        for j in range(2):
            e = tk.Entry(app, width=(int(app.width / 50)), fg='blue', font=('Arial', 12, 'bold'), background='white')
            e.place(x=j * (app.width / 10) + (app.width / 10), y=((app.height / 3) - (int(app.width / 80))))
            e.insert(tk.END, name[j])
            app.eveniment.table.append(e)

        for i in range(indexStat, indexStop):
            for j in range(2):
                if j == 1:
                    e = tk.Entry(app, width=(int(app.width / 50)), fg='black', font=('Arial', 12, 'bold'),
                                 background='white')
                else:
                    e = tk.Entry(app, width=(int(app.width / 90)), fg='black', font=('Arial', 12, 'bold'),
                                 background='white')
                e.place(x=j * (app.width / 10) + (app.width / 10),
                        y=(i % nrelemente) * (int(app.width / 80)) + (app.height / 3))
                try:
                    e.insert(tk.END, rows[i][j])
                    app.eveniment.table.append(e)
                except:
                    app.eveniment.table.append(e)

    except cx_Oracle.DatabaseError as e:
        print(e)

def afiseazaPortofel():
    try:
        app.cursor.execute('select * from portofel order by suporter_ID')
        rows = app.cursor.fetchall()
        name = ('ID', 'Suma')
        # print(rows)

        nrelemente = int(app.height / (12 * 3))

        if app.patient.page > (len(rows) / nrelemente):
            app.patient.page = int(len(rows) / nrelemente)

        if app.patient.page < 0:
            app.patient.page = 0

        indexStat = app.patient.page * nrelemente
        indexStop = app.patient.page * nrelemente + nrelemente

        if indexStop > len(rows):
            indexStop = len(rows)

        for j in range(2):
            e = tk.Entry(app, width=(int(app.width / 50)), fg='blue', font=('Arial', 12, 'bold'), background='white')
            e.place(x=j * (app.width / 10) + (app.width / 10), y=((app.height / 3) - (int(app.width / 100))))
            e.insert(tk.END, name[j])
            app.patient.table.append(e)

        for i in range(indexStat, indexStop):
            for j in range(2):
                if j == 1:
                    e = tk.Entry(app, width=(int(app.width / 50)), fg='LightBlue', font=('Arial', 12, 'bold'),
                                 background='gray10')
                else:
                    e = tk.Entry(app, width=(int(app.width / 90)), fg='LightBlue', font=('Arial', 12, 'bold'),
                                 background='gray10')
                e.place(x=j * (app.width / 10) + (app.width / 10),
                        y=(i % nrelemente) * (int(app.width / 100)) + (app.height / 3))
                try:
                    e.insert(tk.END, rows[i][j])
                    app.patient.table.append(e)
                except:
                    app.patient.table.append(e)

    except cx_Oracle.DatabaseError as e:
        print(e)


def selectOperatiePacient(e=None):
    valori1 = []
    app.patient.pacienti = []
    app.cursor.execute('select nume,email,nrtelefon from suporter order by suporter_id asc')
    rows = app.cursor.fetchall()
    app.patient.pacienti = []
    for i in rows:
        app.patient.pacienti.append(i[2])
        valori1.append(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))

    app.patient.pacientC['values'] = valori1  # se vor citi din baza de date
    app.HideAll()
    if app.patient.strOperatie.get() == ' Adaugare':
        app.patient.numeT.delete("0.0", "end")
        app.patient.prenumeT.delete("0.0", "end")
        app.patient.telefonT.delete("0.0", "end")
        app.patient.ShowPatient(1)
    if app.patient.strOperatie.get() == ' Vizualizare':
        app.patient.ShowPatient(0)
        printPacienti()
    elif app.patient.strOperatie.get() == ' Modificare':
        app.patient.numeT.delete("0.0", "end")
        app.patient.prenumeT.delete("0.0", "end")
        app.patient.telefonT.delete("0.0", "end")
        app.patient.ShowPatient(2)
    elif app.patient.strOperatie.get() == ' Stergere':
        app.patient.ShowPatient(3)

def selectOperatieEveniment(e=None):
    valori1 = []
    app.eveniment.evenimente = []
    app.cursor.execute('select nume from eveniment order by eveniment_id asc')
    rows = app.cursor.fetchall()
    app.eveniment.evenimente = []
    for i in rows:
        app.eveniment.evenimente.append(i[0])
        valori1.append(str(i[0]))

    app.eveniment.evenimentC['values'] = valori1  # se vor citi din baza de date
    app.HideAll()
    if app.eveniment.strOperatie.get() == ' Adaugare':
        app.eveniment.numeT.delete("0.0", "end")
        app.eveniment.ShowEveniment(1)
    if app.eveniment.strOperatie.get() == ' Vizualizare':
        app.eveniment.ShowEveniment(0)
        printEvenimente()
    # elif app.patient.strOperatie.get() == ' Modificare':
    #     app.patient.numeT.delete("0.0", "end")
    #     app.patient.prenumeT.delete("0.0", "end")
    #     app.patient.telefonT.delete("0.0", "end")
    #     app.patient.ShowPatient(2)
    # elif app.patient.strOperatie.get() == ' Stergere':
    #     app.patient.ShowPatient(3)




def okpopup():
    app.top.destroy()
    app.grab_set()


def open_popupEror(tip):
    # playsound('mySound.mp3')
    app.top = tk.Toplevel(app, background='red')
    app.top.geometry('400x200')
    app.top.title("Eroare")
    tk.Label(app.top, text=tip, background='red', font=('Mistral 12 bold')).place(relx=0.5, rely=0.2, anchor='center')
    tk.Button(app.top, text="OK", font='Mistral 12 bold', background='white', command=okpopup).place(relx=0.5, rely=0.5,
                                                                                                     anchor='center')
    app.eval(f'tk::PlaceWindow {str(app.top)} center')


def open_popup(tip):
    # playsound('check.mp3')
    app.top = tk.Toplevel(app, background='green')
    app.top.geometry('400x200')
    app.top.title("Mesaj")
    tk.Label(app.top, text=tip, background='green', font=('Mistral 12 bold')).place(relx=0.5, rely=0.2, anchor='center')
    tk.Button(app.top, text="OK", font=('Mistral 12 bold'), background='white', command=okpopup).place(relx=0.5,
                                                                                                       rely=0.5,
                                                                                                       anchor='center')
    app.eval(f'tk::PlaceWindow {str(app.top)} center')


def open_popupServer():
    app.top = tk.Toplevel(app, background='red')
    app.top.geometry('400x200')
    app.top.title("Mesaj")
    tk.Label(app.top, text="Aplicatia nu se poate conecta la server!\nContactati un administrator!", background='red',
             font=('Mistral 12 bold')).place(relx=0.5, rely=0.2, anchor='center')
    tk.Button(app.top, text="OK", font=('Mistral 12 bold'), background='white', command=okpopup).place(relx=0.5,
                                                                                                       rely=0.5,
                                                                                                       anchor='center')
    app.eval(f'tk::PlaceWindow {str(app.top)} center')



def adaugaPacient(e=None):
    app.patient.inserareNume = app.patient.numeT.get("1.0", "end")
    app.patient.inserarePrenume = app.patient.prenumeT.get("1.0", "end")
    app.patient.inserareTelefon = app.patient.telefonT.get("1.0", "end")

    app.patient.inserareNume = app.patient.inserareNume.replace('\n', '')
    app.patient.inserarePrenume = app.patient.inserarePrenume.replace('\n', '')
    app.patient.inserareTelefon = app.patient.inserareTelefon.replace(' ', '').replace('\n', '')


    try:
        app.cursor.execute(
            'insert into suporter values(null,\'' + app.patient.inserareNume + '\',\'' + app.patient.inserarePrenume + '\',\'' + app.patient.inserareTelefon + '\')')
        open_popup("Datele au fost introduse!")
        app.cursor.execute('commit')
        app.patient.numeT.delete("0.0", "end")
        app.patient.prenumeT.delete("0.0", "end")
        app.patient.telefonT.delete("0.0", "end")
    # except cx_Oracle.IntegrityError as e:
    #     if str(e).__contains__('PACIENT_NUME_CK'.upper()):
    #         open_popupEror("Numele este gresit!")
    #     elif str(e).__contains__('PACIENT_Prenume_CK'.upper()):
    #         open_popupEror("Prenumele este gresit!")
    #     elif str(e).__contains__('pacient_numar_telefon_ck'.upper()):
    #         open_popupEror("Numarul de telefon este invalid!")
    #     print(e)
    #     traceback.print_exc()
    # except cx_Oracle.DatabaseError as e:
    #     if str(e).upper().__contains__(
    #             'ORA-12899: value too large for column "BD034"."PACIENT"."NUMAR_TELEFON"'.upper()):
    #         open_popupEror("Numarul de telefon nu este valid!")
    #     traceback.print_exc()
    except Exception as e:
        print(e)
        traceback.print_exc()

def adaugaEveniment(e=None):
    app.eveniment.inserareNume = app.eveniment.numeT.get("1.0", "end")
    app.patient.inserareNume = app.patient.inserareNume.replace('\n', '')

    try:
        app.cursor.execute(
            'insert into eveniment values(null,\'' + app.patient.inserareNume + '\')')
        open_popup("Datele au fost introduse!")
        app.cursor.execute('commit')
        app.eveniment.numeT.delete("0.0", "end")
        app.eveniment.prenumeT.delete("0.0", "end")
        app.eveniment.telefonT.delete("0.0", "end")
    except Exception as e:
        print(e)
        traceback.print_exc()

class PageHome:
    def __init__(self, app):
        self.app = app
        image = Image.open("fotbal.jpg")
        test = ImageTk.PhotoImage(image)
        self.imgAcasa = tk.Label(image=test, borderwidth=0)
        self.imgAcasa.image = test

    def ShowHome(self):
        self.imgAcasa.place(relx=0.35, rely=0.3, anchor='nw')

    def HideHome(self):
        self.imgAcasa.place_forget()


class PagePatient:
    def __init__(self, app):
        image = Image.open("fotbal.jpg")
        test = ImageTk.PhotoImage(image)
        self.imgBrain = tk.Label(image=test, borderwidth=0, background="gray5")
        self.imgBrain.image = test
        self.app = app
        self.page = 0
        self.adaugareL = tk.Label(text="Adaugare suporter", borderwidth=0, bg="gray5", font=self.app.helv16,
                                  fg="White")
        self.vizualizareL = tk.Label(text="Vizualizare suporteri", borderwidth=0, bg="gray5", font=self.app.helv16,
                                     fg="White")
        self.modificareL = tk.Label(text="Selectati un suporter si modificati datele actuale", borderwidth=0, bg="gray5",
                                    font=self.app.helv16, fg="White")
        self.stergereL = tk.Label(text="Stergere suporteri", borderwidth=0, bg="gray5", font=self.app.helv16,
                                  fg="White")
        self.pacientiL = tk.Label(text="Suporteri", borderwidth=0, bg="gray5", font=self.app.helv30, fg="White")
        self.evenimenteL = tk.Label(text="Evenimente", borderwidth=0, bg="gray5", font=self.app.helv30, fg="White")
        self.numeT = tk.Text(self.app, height=1, width=int(self.app.width / 40))
        self.numeL = tk.Label(text="Nume*", borderwidth=0, bg="gray5", font=self.app.helv14, fg="White")
        self.prenumeT = tk.Text(self.app, height=1, width=int(self.app.width / 40))
        self.prenumeL = tk.Label(text="E-mail*", borderwidth=0, bg="gray5", font=self.app.helv14, fg="White")
        self.telefonT = tk.Text(self.app, height=1, width=int(self.app.width / 40))
        self.telefonL = tk.Label(text="Numar de telefon", borderwidth=0, bg="gray5", font=self.app.helv14,
                                 fg="White")
        self.adaugaB = tk.Button(master=self.app, text="Adauga", width=15, height=1, bg="blue", fg="White",
                                 font=self.app.helv14, background="grey10", borderwidth=1, command=adaugaPacient)


        self.stergeB = tk.Button(master=self.app, text="Sterge", width=15, height=1, bg="blue", fg="White",
                                 font=self.app.helv14, background="grey10", borderwidth=1, command=stergerePacient)

        self.modificaB = tk.Button(master=self.app, text="Modifica", width=15, height=1, bg="blue", fg="White",
                                   font=self.app.helv14, background="grey10", borderwidth=1, command=modificaPacient)

        self.afisareActualB = tk.Button(master=self.app, text="Afisati valorile actuale", width=25, height=1, bg="blue",
                                        fg="White", font=self.app.helv14, background="grey10", borderwidth=1,
                                        command=seteazaValoriActualePacient)
        self.afisarePortofelB = tk.Button(master=self.app, text="Afiseaza portofel", width=25, height=1, bg="blue",
                                        fg="White", font=self.app.helv14, background="grey10", borderwidth=1,
                                        command=afiseazaPortofel)
        self.stergereL1 = tk.Label(text="Alegeti suporterul de sters!", borderwidth=0, bg="gray5", font=app.helv14,
                                   fg="White")
        self.strPacient = tk.StringVar()
        self.pacientC = tk.ttk.Combobox(app, width=int(app.width / 32), textvariable=self.strPacient)

        app.cursor.execute('select nume,email, nrtelefon  from suporter order by suporter_id asc')
        rows = app.cursor.fetchall()
        self.pacienti = []
        pacienti1 = []

        for i in rows:
            self.pacienti.append(i[2])
            pacienti1.append((i[0] + ' ' + i[1] + ' ' + i[2]))

        self.pacientC['state'] = 'readonly'
        self.pacientC['values'] = pacienti1

        self.strOperatie = tk.StringVar()
        self.operatieC = tk.ttk.Combobox(self.app, width=int(app.width / 80), textvariable=self.strOperatie)
        self.operatieC['values'] = (
            ' Vizualizare', ' Adaugare', ' Modificare', ' Stergere')  # se vor citi din baza de date
        self.operatieC.current(1)
        self.operatieC.bind("<<ComboboxSelected>>", selectOperatiePacient)
        self.operatieC['state'] = 'readonly'
        self.table = []
        self.inserareNume = None
        self.inserarePrenume = None
        self.inserareTelefon = None

    def ShowPatient(self, tip):
        self.pacientiL.place(relx=0.5, rely=0.15, anchor='center')
        self.operatieC.place(relx=0.5, rely=0.20, anchor='center')
        if tip == 1:
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.adaugareL.place(relx=0.05, rely=0.25, anchor='w')
            self.numeT.place(relx=0.15, rely=0.3, anchor='w')
            self.numeL.place(relx=0.05, rely=0.3, anchor='w')
            self.prenumeT.place(relx=0.15, rely=0.35, anchor='w')
            self.prenumeL.place(relx=0.05, rely=0.35, anchor='w')
            self.telefonT.place(relx=0.15, rely=0.45, anchor='w')
            self.telefonL.place(relx=0.05, rely=0.45, anchor='w')
            self.adaugaB.place(relx=0.25, rely=0.65, anchor='center')

        elif tip == 0:
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.vizualizareL.place(relx=0.05, rely=0.25, anchor='w')
            self.afisarePortofelB.place(relx=0.95, rely=0.25, anchor='w')
        elif tip == 2:
            self.modificareL.place(relx=0.05, rely=0.25, anchor='w')
            self.pacientC.place(relx=0.35, rely=0.25, anchor='w')
            self.afisareActualB.place(relx=0.60, rely=0.25, anchor='w')
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.numeT.place(relx=0.15, rely=0.3, anchor='w')
            self.numeL.place(relx=0.05, rely=0.3, anchor='w')
            self.prenumeT.place(relx=0.15, rely=0.35, anchor='w')
            self.prenumeL.place(relx=0.05, rely=0.35, anchor='w')
            self.telefonT.place(relx=0.15, rely=0.45, anchor='w')
            self.telefonL.place(relx=0.05, rely=0.45, anchor='w')
            self.modificaB.place(relx=0.25, rely=0.65, anchor='center')


        elif tip == 3:
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.stergereL.place(relx=0.05, rely=0.25, anchor='w')
            self.stergereL1.place(relx=0.05, rely=0.35, anchor='w')
            self.pacientC.place(relx=0.25, rely=0.35, anchor='w')
            self.stergeB.place(relx=0.50, rely=0.35, anchor='w')

    def HidePatient(self):
        self.afisareActualB.place_forget()
        self.modificaB.place_forget()
        self.stergeB.place_forget()
        self.operatieC.place_forget()
        self.adaugaB.place_forget()
        self.afisarePortofelB.place_forget()
        self.vizualizareL.place_forget()
        self.modificareL.place_forget()
        self.stergereL.place_forget()
        self.adaugareL.place_forget()
        self.pacientiL.place_forget()
        self.imgBrain.place_forget()
        self.numeT.place_forget()
        self.numeL.place_forget()
        self.prenumeT.place_forget()
        self.prenumeL.place_forget()
        self.telefonT.place_forget()
        self.telefonL.place_forget()
        self.stergereL1.place_forget()
        self.pacientC.place_forget()
        for i in self.table:
            i.place_forget()


class PageEveniment:
    def __init__(self, app):
        image = Image.open("fotbal.jpg")
        test = ImageTk.PhotoImage(image)
        self.imgBrain = tk.Label(image=test, borderwidth=0, background="gray5")
        self.imgBrain.image = test
        self.app = app
        self.page = 0
        self.adaugareL = tk.Label(text="Adaugare eveniment", borderwidth=0, bg="gray5", font=self.app.helv16,
                                  fg="White")
        self.vizualizareL = tk.Label(text="Vizualizare evenimente", borderwidth=0, bg="gray5", font=self.app.helv16,
                                     fg="White")
        self.modificareL = tk.Label(text="Selectati un eveniment si modificati datele actuale", borderwidth=0, bg="gray5",
                                    font=self.app.helv16, fg="White")
        self.stergereL = tk.Label(text="Stergere eveniment", borderwidth=0, bg="gray5", font=self.app.helv16,
                                  fg="White")
        self.evenimenteL = tk.Label(text="Evenimente", borderwidth=0, bg="gray5", font=self.app.helv30, fg="White")

        self.numeT = tk.Text(self.app, height=1, width=int(self.app.width / 40))
        self.numeL = tk.Label(text="Nume", borderwidth=0, bg="gray5", font=self.app.helv14, fg="White")

        self.adaugaB = tk.Button(master=self.app, text="Adauga", width=15, height=1, bg="blue", fg="White",
                                 font=self.app.helv14, background="grey10", borderwidth=1, command=adaugaEveniment)

        # self.stergeB = tk.Button(master=self.app, text="Sterge", width=15, height=1, bg="blue", fg="White",
        #                          font=self.app.helv14, background="grey10", borderwidth=1, command=stergerePacient)

        self.modificaB = tk.Button(master=self.app, text="Modifica", width=15, height=1, bg="blue", fg="White",
                                   font=self.app.helv14, background="grey10", borderwidth=1, command=modificaEveniment)

        # self.afisareActualB = tk.Button(master=self.app, text="Afisati valorile actuale", width=25, height=1, bg="blue",
        #                                 fg="White", font=self.app.helv14, background="grey10", borderwidth=1,
        #                                 command=seteazaValoriActualeEveniment)
        #
        # self.afisarePretBileteB = tk.Button(master=self.app, text="Afiseaza pretul biletelor", width=25, height=1, bg="blue",
        #                                 fg="White", font=self.app.helv14, background="grey10", borderwidth=1,
        #                                 command=afiseazaPortofel)
        self.stergereL1 = tk.Label(text="Alegeti evenimentul de sters!", borderwidth=0, bg="gray5", font=app.helv14,
                                   fg="White")
        self.strEveniment = tk.StringVar()
        self.evenimentC = tk.ttk.Combobox(app, width=int(app.width / 32), textvariable=self.strEveniment)

        app.cursor.execute('select nume from eveniment order by eveniment_id asc')
        rows = app.cursor.fetchall()
        self.evenimente = []
        evenimente1 = []

        for i in rows:
            self.evenimente.append(i[0])
            evenimente1.append((i[0] ))

        self.evenimentC['state'] = 'readonly'
        self.evenimentC['values'] = evenimente1

        self.strOperatie = tk.StringVar()
        self.operatieC = tk.ttk.Combobox(self.app, width=int(app.width / 80), textvariable=self.strOperatie)
        self.operatieC['values'] = (
            ' Vizualizare', ' Adaugare', ' Modificare', ' Stergere')  # se vor citi din baza de date
        self.operatieC.current(1)
        self.operatieC.bind("<<ComboboxSelected>>", selectOperatieEveniment)
        self.operatieC['state'] = 'readonly'
        self.table = []
        self.inserareNume = None

    def ShowEveniment(self, tip):
        self.evenimenteL.place(relx=0.5, rely=0.15, anchor='center')
        self.operatieC.place(relx=0.5, rely=0.20, anchor='center')
        if tip == 1:
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.adaugareL.place(relx=0.05, rely=0.25, anchor='w')
            self.numeT.place(relx=0.15, rely=0.3, anchor='w')
            self.numeL.place(relx=0.05, rely=0.3, anchor='w')
            self.adaugaB.place(relx=0.25, rely=0.65, anchor='center')

        elif tip == 0:
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.vizualizareL.place(relx=0.05, rely=0.25, anchor='w')
            self.afisarePretBileteB.place(relx=0.95, rely=0.25, anchor='w')
        elif tip == 2:
            self.modificareL.place(relx=0.05, rely=0.25, anchor='w')
            self.evenimentC.place(relx=0.35, rely=0.25, anchor='w')
            self.afisareActualB.place(relx=0.60, rely=0.25, anchor='w')
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.numeT.place(relx=0.15, rely=0.3, anchor='w')
            self.numeL.place(relx=0.05, rely=0.3, anchor='w')
            self.modificaB.place(relx=0.25, rely=0.65, anchor='center')


        elif tip == 3:
            self.imgBrain.place(relx=0.8, rely=0.6, anchor='nw')
            self.stergereL.place(relx=0.05, rely=0.25, anchor='w')
            self.stergereL1.place(relx=0.05, rely=0.35, anchor='w')
            self.evenimentC.place(relx=0.25, rely=0.35, anchor='w')
            self.stergeB.place(relx=0.50, rely=0.35, anchor='w')

    def HideEveniment(self):
        self.modificaB.place_forget()
        self.operatieC.place_forget()
        self.adaugaB.place_forget()
        self.vizualizareL.place_forget()
        self.modificareL.place_forget()
        self.stergereL.place_forget()
        self.adaugareL.place_forget()
        self.evenimenteL.place_forget()
        self.imgBrain.place_forget()
        self.numeT.place_forget()
        self.numeL.place_forget()
        self.stergereL1.place_forget()
        self.evenimentC.place_forget()
        for i in self.table:
            i.place_forget()

class Menu:
    def __init__(self, app):
        # referire la fereastra de baza
        self.app = app
        # butoanele
        self.acasa = tk.Button(master=self.app, text="Acasa", width=int(self.app.width / 100), height=2, bg="blue",
                               fg="White", font=self.app.helv14, background="grey10", borderwidth=0,
                               command=self.onAcasa)
        self.pacient = tk.Button(master=self.app, text="Suporteri", width=int(self.app.width / 100), height=2, bg="blue",
                                 fg="White", font=self.app.helv14, background="grey10", borderwidth=0,
                                 command=self.onPacienti)
        self.eveniment = tk.Button(master=self.app, text="Evenimente", width=int(self.app.width / 100), height=2,
                                 bg="blue",
                                 fg="White", font=self.app.helv14, background="grey10", borderwidth=0,
                                 command=self.onEveniment)

        self.button = [self.acasa,self.pacient,self.eveniment]

    def ShowMenu(self):
        # afisare butoane
        for i in range(3):
            self.button[i].grid(row=0, column=i, padx=20, rowspan=2, pady=30)

        # adaugare functii callback la trecerea cu mouse-ul peste ele
        for i in self.button:
            i.bind("<Enter>", self.on_button)
            i.bind("<Leave>", self.off_button)

    def on_button(self, e):
        e.widget['background'] = 'LightBlue'
        e.widget['fg'] = 'grey10'

    def off_button(self, e):
        e.widget['background'] = 'grey10'
        e.widget['fg'] = 'LightBlue'

    def onAcasa(self, e=None):
        app.HideAll()
        app.home.ShowHome()

    def onPacienti(self, e=None):
        app.HideAll()
        app.patient.ShowPatient(1)
        app.patient.operatieC.current(1)

    def onEveniment(self, e=None):
        app.HideAll()
        app.eveniment.ShowEveniment(1)
        app.eveniment.operatieC.current(1)



# fereastra principala
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bilete meciuri de fotbal')

        # conectare server
        user = 'bd078'
        password = 'bd078'
        cx_Oracle.init_oracle_client(
            lib_dir="C:\\instantclient_21_7")
        dsn_tns = cx_Oracle.makedsn('bd-dc.cs.tuiasi.ro', '1539', service_name='orcl')
        self.conn = cx_Oracle.connect(user=user, password=password, dsn=dsn_tns)
        self.cursor = self.conn.cursor()

        # fonturi folosite
        self.helv14 = font.Font(size=14)
        self.helv16 = font.Font(size=20, underline=True, slant='italic')
        self.helv30 = font.Font(size=30)

        # configurare fereastra
        self.config(bg='white')
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.state("zoomed")  # maximizare fereastra

        # obiecte
        self.menu = Menu(self)
        self.patient = PagePatient(self)
        self.eveniment = PageEveniment(self)
        self.home = PageHome(self)
        self.top = None

    def HideAll(self):
        self.patient.HidePatient()
        self.eveniment.HideEveniment()
        self.home.HideHome()


if __name__ == "__main__":
    app = App()
    app.menu.ShowMenu()
    app.home.ShowHome()
    app.mainloop()

