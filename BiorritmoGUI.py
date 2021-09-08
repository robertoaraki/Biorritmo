# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:29:07 2021

@author: Roberto Takachi Araki
"""
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as msgb

import datetime as dt
from dateutil.relativedelta import relativedelta

import numpy as np
import matplotlib.pyplot as pl

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)


class Application:

    def __init__(self, master=None):
        self.fonte = ("Verdana", "10")

        # Frames ---
        self.cabec1_frame = tk.Frame(master)
        self.cabec1_frame.place(x=0, y=0, height=32, relwidth=0.96)

        self.cabec2_frame = tk.Frame(master)
        self.cabec2_frame.place(x=0, y=33, height=32, relwidth=0.99)

        self.cabec3_frame = tk.Frame(master)
        self.cabec3_frame.place(x=0, y=66, height=32, relwidth=0.96)

        self.graf_frame = tk.Frame(master, bd=1.5)
        self.graf_frame.place(x=0, y=110, relwidth=1, relheight=0.91)
        self.graf_frame["bg"] = "light gray"
        # ---------------

        # Formulario ----
        self.lbldatanasc = tk.Label(self.cabec1_frame)
        self.lbldatanasc.place(x=2, y=1, height=30, width=260)
        self.lbldatanasc["text"] = "Data de nascimento (dd/mm/aaaa):"
        self.lbldatanasc["font"] = self.fonte
        self.lbldatanasc["anchor"] = "e"

        ttk.Style().configure('pad.TEntry', padding='1 1 1 1')

        self.txtdatanasc = ttk.Entry(self.cabec1_frame, style='pad.TEntry')
        self.txtdatanasc["font"] = self.fonte
        self.txtdatanasc.place(x=265, y=1, height=30, width=150)

        self.lbldatanasctooltip = tk.Label(self.cabec1_frame)
        self.lbldatanasctooltip.place(x=430, y=1, height=30, width=450)
        self.lbldatanasctooltip["text"] = "Idade máxima de 150 anos."
        self.lbldatanasctooltip["font"] = ["Verdana", "9", "italic"]
        self.lbldatanasctooltip["fg"] = "gray"
        self.lbldatanasctooltip["anchor"] = "w"

        self.lbldatabiortm = tk.Label(self.cabec2_frame)
        self.lbldatabiortm.place(x=2, y=1, height=30, width=260)
        self.lbldatabiortm["text"] = "Data p/o biorritmo (dd/mm/aaaa):"
        self.lbldatabiortm["font"] = self.fonte
        self.lbldatabiortm["anchor"] = "e"

        self.txtdatabiortm = ttk.Entry(self.cabec2_frame, style='pad.TEntry')
        self.txtdatabiortm["font"] = self.fonte
        self.txtdatabiortm.place(x=265, y=1, height=30, width=150)
        self.txtdatabiortm.bind("<Key>", self.txtdatabiortm_keypress)

        self.lblperiodo = tk.Label(self.cabec2_frame)
        self.lblperiodo.place(x=420, y=1, height=30, width=140)
        self.lblperiodo["text"] = "Período (mm/aaaa):"
        self.lblperiodo["font"] = self.fonte
        self.lblperiodo["anchor"] = "e"

        self.txtperiodo = ttk.Entry(self.cabec2_frame, style='pad.TEntry')
        self.txtperiodo["font"] = self.fonte
        self.txtperiodo.place(x=563, y=1, height=30, width=150)
        self.txtperiodo.bind("<Key>", self.txtperiodo_keypress)

        self.lblperiodotooltip = tk.Label(self.cabec2_frame)
        self.lblperiodotooltip.place(x=730, y=1, height=30, width=440)
        self.lblperiodotooltip["text"] = "Se deixar o período em branco, " + \
            "o data de hoje é usada como padrão."
        self.lblperiodotooltip["font"] = ["Verdana", "9", "italic"]
        self.lblperiodotooltip["fg"] = "gray"
        self.lblperiodotooltip["anchor"] = "w"

        self.btnenviar = tk.Button(self.cabec3_frame)
        self.btnenviar.place(x=265, y=1, height=30, width=450)
        self.btnenviar["text"] = "Calcular Biorritmo"
        self.btnenviar["font"] = self.fonte
        self.btnenviar["command"] = self.recebe_data

        self.figura = pl.Figure(figsize=(10, 7), dpi=100)
        self.figura.subplots_adjust(bottom=0.2)
        self.graf = FigureCanvasTkAgg(self.figura, self.graf_frame)
        self.graf.get_tk_widget().pack(side='top', fill='both', expand=0)
        # fim Formulario ----

    def limpa_grafico(self):
        self.graf_frame = None
        self.graf_frame = tk.Frame(root, bd=1.5)
        self.graf_frame.place(x=0, y=110, relwidth=1, relheight=0.91)
        self.graf_frame["bg"] = "light gray"

        self.figura = pl.Figure(figsize=(10, 7), dpi=100)
        self.figura.subplots_adjust(bottom=0.2)
        self.graf = FigureCanvasTkAgg(self.figura, self.graf_frame)
        self.graf.get_tk_widget().pack(side='top', fill='both', expand=0)

    # se for digitado algo em txtdatabiortm, txtperiodo é apagado
    def txtdatabiortm_keypress(self, event):
        self.txtperiodo.delete(0, tk.END)

    # se for digitado algo em txtperiodo, txtdatabiortm é apagado
    def txtperiodo_keypress(self, event):
        self.txtdatabiortm.delete(0, tk.END)

    def verifica_data(self, data):
        msg = ""

        if len(data) in [8, 9, 10]:
            try:
                dia, mes, ano = data.split('/')

            except Exception:
                msg = "A data está no formato errado! Tente novamente!"
                data = None
                return msg, data

        elif len(data) in [6, 7]:
            try:
                mes, ano = data.split('/')
                dia = 1

            except Exception:
                msg = "A data está no formato errado! Tente novamente!"
                data = None
                return msg, data

        else:
            msg = "A data está no formato errado! Tente novamente!"
            data = None
            return msg, data

        try:
            data = dt.datetime(int(ano), int(mes), int(dia))

        except Exception:
            msg = "A data inválida! Tente novamente!"
            data = None
            return msg, data

        # se a for menor que 150 anos
        data_min = dt.datetime.now() - relativedelta(years=150)
        if (data - data_min).days <= 0:
            msg = "A data tem mais de 150 anos! Tente novamente!"
            data = None

        return msg, data

    def recebe_data(self):
        dtnasc = self.txtdatanasc.get()
        dtbior = self.txtdatabiortm.get()
        dtper = self.txtperiodo.get()

        msg = ""
        msg, dtnasc = self.verifica_data(dtnasc)
        if dtnasc is None:
            msgb.showerror(title="Validação de Data de Nascimento",
                           message=msg)
            self.txtdatanasc.selection_range(0, tk.END)
            self.txtdatanasc.focus()
            return

        if dtbior != "":
            msg = ""
            msg, dtbior = self.verifica_data(dtbior)
            if dtbior is None:
                msgb.showerror(title="Validação de Data para Biorritmo",
                               message=msg)
                self.txtdatabiortm.selection_range(0, tk.END)
                self.txtdatabiortm.focus()
                return

        elif dtper != "":
            msg = ""
            msg, dtper = self.verifica_data(dtper)
            if dtper is None:
                msgb.showerror(title="Validação de Período para Biorritmo",
                               message=msg)
                self.txtperiodo.selection_range(0, tk.END)
                self.txtperiodo.focus()
                return

        self.calcular_biorritmo(dtnasc)

    def calcular_data_inicio(self):
        dtbior = self.txtdatabiortm.get()
        dtper = self.txtperiodo.get()

        if dtbior != "":
            msg, dtbior = self.verifica_data(dtbior)
            dt_inic = dtbior - relativedelta(days=15)

        elif dtper != "":
            msg, dtper = self.verifica_data(dtper)
            dt_inic = dtper

        else:
            hoje = dt.datetime.now()
            dt_inic = hoje - relativedelta(days=15)

        dt_inic = dt.date(dt_inic.year, dt_inic.month, dt_inic.day)
        return dt_inic, dtper

    def calcular_biorritmo(self, data_nasc):
        self.limpa_grafico()

        dt_nasc = data_nasc.date()
        dt_inic, dt_period = self.calcular_data_inicio()

        dias_vida = (dt_inic-dt_nasc).days

        doispi = 2 * np.pi

        X = np.arange(dias_vida, dias_vida + 30, 1/128)
        Fi = np.sin(doispi / 23 * X)
        Em = np.sin(doispi / 28 * X)
        In = np.sin(doispi / 33 * X)

        lista_dias_a = list(range(dias_vida, dias_vida + 31))
        date_list = [(dt_inic +
                      dt.timedelta(days=x)).strftime('%d-%m-%y')
                     for x in range(31)]

        axf = self.figura.add_subplot()
        axf.clear()
        axf.plot(X, Fi, X, Em, X, In)

        axf.legend(['Físico', 'Emocional', 'Intelectual'],
                   loc='best', fontsize='small')

        axf.set_xticks(lista_dias_a)
        axf.set_xticklabels(date_list)

        axf.set(xlim=[dias_vida, dias_vida + 30],
                ylim=[-1.1, 1.1],
                xlabel='Período',
                ylabel='Fase',
                title='Biorritmo para o período')

        pl.setp(axf.get_xticklabels(), rotation=80, fontsize='small')
        pl.setp(axf.get_yticklabels(), fontsize='x-small')

        if dt_period == "":
            axf.axvline(x=dias_vida+15, ls='--',
                        color='gray', label='Hoje', lw=1)
            axf.get_xticklabels()[15].set_color("red")
            axf.get_xticklabels()[15].set_weight("bold")

        axf.grid(axis='x')
        axf.grid(axis='y')

        self.graf.draw()


# Raiz ---
root = tk.Tk()
root.geometry('1200x800')
root.title("Biorritmo")

Application(root)
# ---------------

root.mainloop()
