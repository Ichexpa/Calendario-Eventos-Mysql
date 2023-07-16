import tkinter as tk
from tkinter import ttk
from AdministradorDeFechas import AdministradorDeFechas

class VentanaDetalleEvento(tk.Frame):
    titulosEvento = "consolas 14"
    informacionEvento="consolas 14 bold";
    colorFondoWidget = "#F0F0F0";
    colorFuente="black"
    colorDeFondoEventoImportante ="#37A0A2"
    def __init__(self, padre,evento):
        super().__init__(padre);
        self.ventana=tk.Toplevel(padre,padx=20,pady=20);
        self.ventana.title(evento[1]);
        fecha, hora = AdministradorDeFechas.separar_fecha_hora(evento[2])
        importante="No";
        if(evento[5]==1):
            importante="Si";
            self.colorFondoWidget = self.colorDeFondoEventoImportante
            self.ventana.configure(background=self.colorDeFondoEventoImportante);
            self.colorFuente="white";
        self.grid();
        tk.Label(self.ventana,text="Titulo",font=self.titulosEvento,fg=self.colorFuente,bg=self.colorFondoWidget).grid(row=0,column=0);
        tk.Label(self.ventana, text=evento[1], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=0, column=1);
        tk.Label(self.ventana, text="Fecha", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=1, column=0);
        tk.Label(self.ventana, text=fecha, font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=1, column=1);
        tk.Label(self.ventana, text="Hora", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=2, column=0);
        tk.Label(self.ventana, text=hora, font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=2, column=1);
        tk.Label(self.ventana, text="Duracion", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=3, column=0);
        tk.Label(self.ventana, text=f'{evento[3]} minutos', font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=3, column=1);
        tk.Label(self.ventana, text="Importante", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=4, column=0);
        tk.Label(self.ventana, text=importante, font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=4, column=1);
        tk.Label(self.ventana, text="Identificador de Evento", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid( row=5, column=0,columnspan=2);
        tk.Label(self.ventana, text=evento[6], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=6, column=0,columnspan=2);
        tk.Label(self.ventana, text="Descripción", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=7, column=0, columnspan=2);
        tk.Label(self.ventana, text=evento[4], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=8, column=0, columnspan=2);
        


