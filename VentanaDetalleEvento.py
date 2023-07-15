import tkinter as tk
from tkinter import ttk


class VentanaDetalleEvento(tk.Frame):
    titulosEvento = "consolas 14"
    informacionEvento="consolas 14 bold";
    colorFondoWidget = "#F0F0F0";
    colorFuente="black"
    colorDeFondoEventoImportante ="#37A0A2"
    def __init__(self, padre,evento):
        super().__init__(padre);
        self.ventana=tk.Toplevel(padre,padx=20,pady=20);
        self.ventana.title(evento["titulo"]);        
        importante="No";
        if(evento["importancia"]):
            importante="Si";
            self.colorFondoWidget = self.colorDeFondoEventoImportante
            self.ventana.configure(background=self.colorDeFondoEventoImportante);
            self.colorFuente="white";
        self.grid();
        tk.Label(self.ventana,text="Titulo",font=self.titulosEvento,fg=self.colorFuente,bg=self.colorFondoWidget).grid(row=0,column=0);
        tk.Label(self.ventana, text=evento["titulo"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=0, column=1);
        tk.Label(self.ventana, text="Fecha", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=1, column=0);
        tk.Label(self.ventana, text=evento["fecha"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=1, column=1);
        tk.Label(self.ventana, text="Hora", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=2, column=0);
        tk.Label(self.ventana, text=evento["hora"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=2, column=1);
        tk.Label(self.ventana, text="Duracion", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=3, column=0);
        tk.Label(self.ventana, text=evento["duracion"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=3, column=1);
        tk.Label(self.ventana, text="Importante", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=4, column=0);
        tk.Label(self.ventana, text=importante, font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=4, column=1);
        tk.Label(self.ventana, text="Fecha de Recordatorio", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=5, column=0);
        tk.Label(self.ventana, text=evento["fechaRecordatorio"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=5, column=1);
        tk.Label(self.ventana, text="Hora de Recordatorio", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=6, column=0);
        tk.Label(self.ventana, text=evento["horaRecordatorio"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=6, column=1);
        tk.Label(self.ventana, text="Identificador de Evento", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid( row=7, column=0);
        tk.Label(self.ventana, text=evento["identificadorEvento"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=7, column=1);
        tk.Label(self.ventana, text="Descripción", font=self.titulosEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=8, column=0, columnspan=2);
        tk.Label(self.ventana, text=evento["descripcion"], font=self.informacionEvento,
                 fg=self.colorFuente, bg=self.colorFondoWidget).grid(row=9, column=0, columnspan=2);
        


