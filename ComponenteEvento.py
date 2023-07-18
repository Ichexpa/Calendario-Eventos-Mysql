import tkinter as tk
from Evento import Evento;
from tkcalendar import DateEntry
from AdministradorDeFechas import AdministradorDeFechas
from tkinter import messagebox
import locale
from datetime import datetime
class ComponenteEvento(tk.Frame):

    colorDeFondo = "#BFDFB2"
    fuenteDelComponente = "consolas 13 bold"
    colorBotones = "#62CFA4";

    def __init__(self, padre,tabla,manejadorDeLaListaEventos):
        super().__init__(padre)
        self.tablaEventos=tabla;
        self.manejadorDeLaListaEventos = manejadorDeLaListaEventos
        locale.setlocale(locale.LC_ALL, "es_ES");

        self.titulo=tk.StringVar();
        self.hora =tk.StringVar();
        self.minutos =tk.StringVar();
        self.duracion=tk.StringVar(value="1 Hora");
        self.importancia=tk.BooleanVar();
        """ self.horaRecordatorio = tk.StringVar()
        self.minutosRecordatorio = tk.StringVar() """
        self.identificadorEvento=tk.StringVar();
        self.contenedorForm=tk.LabelFrame(self,text="Agregar nuevo Evento",font=self.fuenteDelComponente,padx=30,pady=30);
        self.contenedorForm.grid(row=0, column=0,padx=10,pady=10);

        tk.Label(self.contenedorForm, text="Titulo", font=self.fuenteDelComponente).grid(row=0, column=0)
        self.tituloInput=tk.Entry(self.contenedorForm, textvariable=self.titulo, font=self.fuenteDelComponente,justify="center")
        self.tituloInput.grid(row=0, column=1, columnspan=3, sticky="we")
        tk.Label(self.contenedorForm, text="Fecha",
                 font=self.fuenteDelComponente).grid(row=1, column=0)
        self.fechaInput = DateEntry(self.contenedorForm, locale="es_ES", font=self.fuenteDelComponente)
        self.fechaInput.grid(row=1, column=1,sticky="we");
        tk.Label(self.contenedorForm, text="Hora", font=self.fuenteDelComponente).grid(
            row=1, column=2, ipadx=5, ipady=5)
        
        self.contenedorHoraMinutoEvento = tk.Frame(self.contenedorForm);
        self.contenedorHoraMinutoEvento.grid(row=1, column=3, padx=5, pady=5);

        self.horaInput=tk.Spinbox(self.contenedorHoraMinutoEvento, textvariable=self.hora,
                                  font=self.fuenteDelComponente, justify="center",width=5,
                                  increment=1, from_=0, to=23)
        self.hora.set("");
        self.horaInput.grid(row=0,column=0);

        self.minutosInput=tk.Spinbox(self.contenedorHoraMinutoEvento, textvariable=self.minutos,
                                font=self.fuenteDelComponente, justify="center",width=5,
                                increment=1,from_=0, to=60)
        self.minutos.set("")
        self.minutosInput.grid(row=0, column=1)

        tk.Label(self.contenedorForm, text="Duracion", font=self.fuenteDelComponente).grid(
            row=2, column=0,padx=5,pady=5);
        self.duracionInput=tk.Entry(self.contenedorForm, textvariable=self.duracion, font=self.fuenteDelComponente, justify="center")
        self.duracionInput.grid(row=2, column=1);
        tk.Label(self.contenedorForm, text="Importante", font=self.fuenteDelComponente).grid(
            row=2, column=2, padx=10, pady=10)
        self.checkButtonInput=tk.Checkbutton(self.contenedorForm, variable=self.importancia, font=self.fuenteDelComponente)
        self.checkButtonInput.grid(row=2, column=3)

        tk.Label(self.contenedorForm, text="Identificar Evento como", font=self.fuenteDelComponente).grid(row=3, column=0,columnspan=2,pady=10)
        self.identificadoInput=tk.Entry(self.contenedorForm, textvariable=self.identificadorEvento,font=self.fuenteDelComponente, justify="center")
        self.identificadoInput.grid( row=4, column=0, columnspan=4, sticky="we", pady=10)
        tk.Label(self.contenedorForm,text="Descripción",font=self.fuenteDelComponente).grid(row=5,column=0,columnspan=4,pady=5);
        self.descripcion = tk.Text(self.contenedorForm, font=self.fuenteDelComponente,height=5,width=60);
        self.descripcion.grid(row=6, column=0, columnspan=4,padx=5,pady=5);
        self.botonCrearEvento=tk.Button(self.contenedorForm, text="Agregar Evento", command=self.agregarEvento,
                  padx=5, pady=5,font=self.fuenteDelComponente,fg="white",bg=self.colorBotones);
        self.botonCrearEvento.grid(
            row=7, column=0, columnspan=4, sticky="snew");
        self.botonEditarEvento = tk.Button(
        self.contenedorForm, text="Editar",fg="white", font=self.fuenteDelComponente, bg=self.colorBotones,
        command=self.modificarEvento);
        self.botonCancelarEdicion = tk.Button(self.contenedorForm, text="Cancelar Edicion",
                                              fg="white",command=self.reestabecerBotonOriginal, font=self.fuenteDelComponente, bg="#CF6562")
    
    def agregarEvento(self):
        if(not self.comprobarEntrysVacios()):
            if (AdministradorDeFechas.validarHora(self.hora.get(), self.minutos.get())):
                self.cargarEvento()
                self.tablaEventos.agregarEventoATabla(self.evento)
            else:
                messagebox.showwarning("Advertencia", "Hora de Evento o Recordatorio ingresada invalida");

        else:
            messagebox.showwarning("Advertencia", "Existen entradas sin completar");


    def colocarRegistrosCargadosEnCampos(self,evento):
        self.limpiarTabla();
        self.cargarCampos(evento);

    def limpiarTabla(self):
        fechaActual = datetime.now().date();
        self.tituloInput.delete(0, tk.END);
        self.horaInput.delete(0, tk.END);
        self.fechaInput.set_date(fechaActual)
        self.minutosInput.delete(0,tk.END);
        self.duracionInput.delete(0, tk.END);
        self.checkButtonInput.deselect();
        self.fechaRecordatorioInput.set_date(fechaActual)
        self.horaRecordatorioInput.delete(0, tk.END);
        self.minutosRecordatorioInput.delete(0, tk.END);
        self.identificadoInput.delete(0, tk.END);
        self.descripcion.delete("1.0", 'end-1c');

    def cargarCampos(self,evento):
        fechaFormateadaADate = AdministradorDeFechas.cadenaDeFechaADate(evento["fecha"])
        fechaRecordatorioFormateada = AdministradorDeFechas.cadenaDeFechaADate(evento["fechaRecordatorio"])
        horaEvento,minutoEvento=AdministradorDeFechas.horaYMinutoSeparados(evento["hora"]);
        horaRecordatorio,minutoRecordatorio=AdministradorDeFechas.horaYMinutoSeparados(evento["horaRecordatorio"]);

        self.tituloInput.insert(0, evento["titulo"])
        self.fechaInput.set_date(fechaFormateadaADate)        
        self.horaInput.insert(0, horaEvento)      
        self.minutosInput.insert(0,minutoEvento);        
        self.duracionInput.insert(0, evento["duracion"])

        if (evento["importancia"]):
            self.checkButtonInput.select()
        else:
            self.checkButtonInput.deselect()                    
        self.fechaRecordatorioInput.set_date(fechaRecordatorioFormateada)        
        self.horaRecordatorioInput.insert(0, horaRecordatorio)        
        self.minutosRecordatorioInput.insert(0, minutoRecordatorio)        
        self.identificadoInput.insert(0, evento["identificadorEvento"])        
        self.descripcion.insert(tk.INSERT, evento["descripcion"])

    def editarRegistro(self,evento,indice,indiceFilaTabla):
        #print(evento);
        #Declaro los botones
        self.contenedorForm.configure(text="Modificar Evento")
        self.botonCrearEvento.grid_forget()
      
        #Para que los botones no se agregue el mismo componente en la misma posicion
        self.botonCancelarEdicion.grid_forget();
        self.botonEditarEvento.grid_forget();
        
        #Se guardan los indices para luego pasarlos a la clase de la tabla
        self.indiceElementoAEditar=indice;
        self.indiceFilaTabla=indiceFilaTabla;       

        self.colocarRegistrosCargadosEnCampos(evento);

        self.botonEditarEvento.grid(row=7, column=0, columnspan=2,sticky="we",padx=5);
        
        self.botonCancelarEdicion.grid(row=7, column=2, columnspan=2,sticky="we",padx=5);

    def reestabecerBotonOriginal(self):
        self.botonEditarEvento.grid_forget();
        self.botonCancelarEdicion.grid_forget();
        self.contenedorForm.configure(text="Agregar nuevo Evento");
        self.botonCrearEvento.grid(row=8, column=0, columnspan=4, sticky="snew");
    
    def comprobarEntrysVacios(self):
        lista=[self.tituloInput,self.duracionInput,self.identificadorEvento];
        for entry in lista:
            if(not entry.get()):
               return True;    


    def cargarEvento(self):
        self.evento = Evento(self.titulo.get(),
                             self.fechaInput.get_date(),
                             AdministradorDeFechas.getFechaFormateada(self.hora.get(),self.minutos.get()),
                             self.duracion.get(),                             
                             self.identificadorEvento.get(),
                             self.descripcion.get("1.0", 'end-1c'),
                             self.importancia.get())
        print(f'Fecha: {self.evento.fecha}, Hora: {self.evento.hora},impportancia:{self.evento.importancia}')

    def modificarEvento(self):
        self.cargarEvento();
        tuplaABuscar=("",self.evento.fecha,self.evento.hora);
        resBusqueda=self.manejadorDeLaListaEventos.encontrarObjeto(tuplaABuscar);   
        if (resBusqueda!=False):
            #obtengo el indice del objeto para comprobar si el que quiero editar
            indice=resBusqueda[0]
            esElMismoEvento= indice==self.indiceElementoAEditar;
                
        if(resBusqueda==False or esElMismoEvento):
            self.manejadorDeLaListaEventos.contenedorObjetos[self.indiceElementoAEditar] = self.evento.getEventoComoDict()
            self.manejadorDeLaListaEventos.escribirEnFichero()
            self.tablaEventos.modificarFila(self.evento, self.indiceFilaTabla)
            
            
        else:
            messagebox.showerror("Hora ya registrada",
                                 f"El registro del evento {self.evento.fecha} {self.evento.hora} ya se encuentra en uso")
        self.limpiarTabla();
        self.reestabecerBotonOriginal()