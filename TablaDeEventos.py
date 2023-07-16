import tkinter as tk
from tkinter import ttk,messagebox;
from VentanaDetalleEvento import VentanaDetalleEvento
from AdministradorDeFechas import AdministradorDeFechas
from datetime import datetime
from EventosModelo import EventosModelo
from EventosYEtiquetasModel import EventosYEtiquetasModelos
class TablaDeEventos(tk.Frame):
    colorDeFondo = "#BFDFB2"
    fuenteTextos = "consolas 14 bold"
    fuenteBotones="consolas 11 bold"
    fuenteSemanasMeses="consolas 12 bold"
    colorBotones = "#62CFA4"
    colorBotonesExploradoresDeFecha = "#086A52";

    def __init__(self,padre,manejadorJson,conexionDB):
        super().__init__(padre);
        self.contadorSiguienteSemana=7;
        self.padre=padre;
        self.conexionDB=conexionDB;
        self.evento_modelo=EventosModelo();
        self.administradorDeFecha=AdministradorDeFechas();
        self.administradorDeFecha.getMesActual(datetime.now().date())
        self.accesorAlFicheroJson = manejadorJson;
        self.ingresobuscarEvento=tk.StringVar()
        self.estilo = ttk.Style()
        # Modifico la fuente de las filas
        self.estilo.configure("mystyle.Treeview", highlightthickness=0, bd=0,font=('consolas', 11))  
        # Modifico la fuente del header de la tabla
        self.estilo.configure("mystyle.Treeview.Heading", font=('consolas', 12, 'bold')) 
        # remuevo los bordes
        self.estilo.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) 
        
        self.contenedorTabla = tk.LabelFrame(self, text="Eventos", font=self.fuenteTextos, padx=30, pady=30)
        self.contenedorTabla.grid(row=0, column=0, padx=10, pady=10)

        self.labelBuscarEvento=tk.Label(self.contenedorTabla,text="Buscar Evento",font=self.fuenteTextos);
        self.labelBuscarEvento.grid(row=0,column=0,columnspan=2,pady=15,sticky="w");
        self.buscarEventoInput=tk.Entry(self.contenedorTabla,textvariable=self.ingresobuscarEvento,
                                        font=self.fuenteBotones,justify="center");
        self.buscarEventoInput.grid(row=1,column=0,sticky="snwe")
        self.botonBuscarEvento=tk.Button(self.contenedorTabla,text="Buscar evento",
                                         bg="#0D4AA7", fg="white", font=self.fuenteBotones,command=self.buscarEvento);
        #self.botonBuscarEvento.bind("<Button-1>",self.buscarEvento);
        self.botonBuscarEvento.grid(row=1,column=1)

        self.botonAnteriorSemana = tk.Button(self.contenedorTabla, text="Anterior Semana",
                                             bg=self.colorBotonesExploradoresDeFecha,fg="white" ,font=self.fuenteBotones)
        self.botonAnteriorSemana.bind("<Button-1>", self.anteriorSemana)
        self.botonAnteriorSemana.grid(row=1, column=2,sticky="e")
        
        self.botonSiguienteSemana=tk.Button(self.contenedorTabla,text="Siguiente Semana",
                                            bg=self.colorBotonesExploradoresDeFecha, fg="white",font=self.fuenteBotones)
        self.botonSiguienteSemana.bind("<Button-1>", self.siguienteSemana)
        self.botonSiguienteSemana.grid(row=1, column=3,sticky="e")

  
        
        self.botonMesSiguiente = tk.Button(self.contenedorTabla, text="Mes siguiente",
                                           bg=self.colorBotonesExploradoresDeFecha, fg="white", font=self.fuenteBotones)
        self.botonMesSiguiente.bind("<Button-1>", self.siguienteMes)

        self.botonMesAnterior = tk.Button(self.contenedorTabla, text="Mes anterior",
                                          bg=self.colorBotonesExploradoresDeFecha, fg="white", font=self.fuenteBotones)
        self.botonMesAnterior.bind("<Button-1>", self.mesAnterior)

        self.comboOpcionesDeFiltro=ttk.Combobox(self.contenedorTabla,values=["Filtrar por Mes","Filtrar por Semana"],
                                                font=self.fuenteBotones);
        #Por defecto estara apuntando a filtrar por semana
        self.comboOpcionesDeFiltro.current(1)
        self.comboOpcionesDeFiltro.bind("<<ComboboxSelected>>",self.seleccionDeFiltro);
        self.comboOpcionesDeFiltro.grid(row=0,column=2,columnspan=2,sticky="we",pady=15);
        
        self.tabla = ttk.Treeview(self.contenedorTabla,
                                  columns=("ID","Titulo", "Fecha", "Hora",
                                           "Duracion", "Descripcion", "Importante"), style="mystyle.Treeview")
        
        #Defino las columnas
        self.tabla.column("#0", width=0)
        self.tabla.column('ID', width=20,anchor="center")
        self.tabla.column("Titulo", width=200, anchor="center")
        self.tabla.column("Fecha", width=90, anchor="center")
        self.tabla.column("Hora", width=50, anchor="center")
        self.tabla.column("Duracion", width=100, anchor="center")
        self.tabla.column("Descripcion", width=110, anchor="center")
        self.tabla.column("Importante", width=130, anchor="center")        
        #Defino las cabeceras        
        self.tabla.heading("#0", text="")
        self.tabla.heading('ID', text='ID',anchor='center')
        self.tabla.heading("Titulo", text="Titulo", anchor="center")
        self.tabla.heading("Fecha", text="Fecha", anchor="center")
        self.tabla.heading("Hora", text="Hora", anchor="center")
        self.tabla.heading("Duracion", text="Duracion", anchor="center")
        self.tabla.heading("Descripcion", text="Descripcion", anchor="center")
        self.tabla.heading("Importante", text="Importante", anchor="center")
        #Defino tag para setear el color para filas importantes
        self.tabla.tag_configure("importante", background="#33B289",foreground="white")
        self.tabla.tag_configure("sinImportancia", background="white",foreground="black")
        self.tabla.grid(row=3,column=0,columnspan=4);
        self.cargarTablaPorSemana();
        self.labelFechaInferior = tk.Label(self.contenedorTabla,
                                           text=AdministradorDeFechas.mostrarFormateadaFechaDiaMes(self.administradorDeFecha.fechaLimiteInferior),
                                           font=self.fuenteSemanasMeses)
        self.labelFechaInferior.grid(row=2, column=0, columnspan=2,padx=5,pady=5)
        self.labelFechaSuperior = tk.Label(self.contenedorTabla, text=AdministradorDeFechas.mostrarFormateadaFechaDiaMes(
            self.administradorDeFecha.fechaLimiteSuperior), font=self.fuenteSemanasMeses)
        self.labelFechaSuperior.grid(row=2,column=2,columnspan=2,padx=5,pady=5);

        self.labelMesActual = tk.Label(self.contenedorTabla, text=self.administradorDeFecha.getNombreMesActual(),
                                        font=self.fuenteSemanasMeses)
        
        self.tabla.bind("<Double-1>", self.mostrarDetalleEventoSeleccionado)
    
    def mostrarDetalleEventoSeleccionado(self, e):        
        seleccionado=self.tabla.focus();
        valor = self.tabla.item(seleccionado,"value");
        evento_seleccionado = EventosYEtiquetasModelos().get_evento_y_etiqueta(self.conexionDB, valor[0])
        VentanaDetalleEvento(self.padre, evento_seleccionado)

    def agregarEventoATabla(self,evento):
        #Se guarda el evento formateado al json que a su vez lo guarda en la lista de la clase
        noSeEncuentraRepetido=self.accesorAlFicheroJson.agregarObjetoAFichero(evento.getEventoComoDict());
        if (noSeEncuentraRepetido):
            fechaTipoDate = AdministradorDeFechas.cadenaDeFechaADate(evento.fecha)
            seEncuentraEnLaSemana = self.administradorDeFecha.seEncuentraEnLaSemana(fechaTipoDate,  # Retorna un booleano
                                                                            self.contadorSiguienteSemana)
            seEncuentraEnElMes = AdministradorDeFechas.comprobarSiSeEncuentraEnElMesActual(fechaTipoDate,
                                                                                       self.administradorDeFecha.fechaPrimerDia,
                                                                                       self.administradorDeFecha.fechaUltimoDia)
            #Si esta en mes y se encuentra en los intervalos del mes se agrega a la tabla
            if (self.comboOpcionesDeFiltro.get() == "Filtrar por Mes" and seEncuentraEnElMes):
                self.agregarEventoOrdenado(evento);
            #Si esta en la semana y se encuentra entre los intervalos de la semana se agrega a la tabla
            elif (self.comboOpcionesDeFiltro.get() == "Filtrar por Semana" and seEncuentraEnLaSemana):
                self.agregarEventoOrdenado(evento);

            messagebox.showinfo("Evento agregado", "Evento agregado con exito");
        else:
            messagebox.showerror("Evento existente","Ya existe un evento con la fecha y hora indicada");
           
        
    
    def agregarEventoOrdenado(self,evento):
        tuplaNuevoEvento = (evento.titulo,
                            evento.fecha,
                            evento.hora,
                            evento.duracion,
                            evento.descripcion,
                            self.esImportante(evento.importancia))
        self.tabla.insert("", tk.END, values=tuplaNuevoEvento,tags=self.colorFilaImportante(evento.importancia));
        self.agregarFechaOrdenada();
        
    def incializar_tabla(self):
        print("Carga la tabla de eventos")
        lista_eventos = self.evento_modelo.get_eventos(self.conexionDB)
        self.cargarTabla(lista_eventos)

    def cargarTabla(self,lista):        
        for evento in lista:
            fecha,hora=AdministradorDeFechas.separar_fecha_hora(evento[2])
            self.tabla.insert("", tk.END, values=(evento[0],
                                                   evento[1],
                                                      fecha,
                                                      hora,
                                                      evento[3],
                                                      evento[4],
                                                      self.esImportante(evento[5])),
                                                      tags=self.colorFilaImportante(evento[5]));

    def cargarTablaPorSemana(self):
        self.eliminarFilas();        
        listaDeEventosPrimeraSemana=self.evento_modelo.get_eventos_semanales(self.conexionDB,self.contadorSiguienteSemana)
        self.cargarTabla(listaDeEventosPrimeraSemana);

    def cargarRegistrosDelMesEnTabla(self):
        self.eliminarFilas()
        listaDeEventosDentroDelMes = self.accesorAlFicheroJson.obtenerMes(self.administradorDeFecha.fechaPrimerDia,
                                                                          self.administradorDeFecha.fechaUltimoDia);
        self.cargarTabla(listaDeEventosDentroDelMes);
            
    def esImportante(self,valor):
        if (valor==1):
            esImportante = "Si"
        else:
            esImportante="No"
        return esImportante;
    def colorFilaImportante(self,valor):
        if (valor==1):
            return "importante"
        else:
            return "sinImportancia"
    def eliminarFilas(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila);
    
    def agregarFechaOrdenada(self):
        filasDeTabla=self.tabla.get_children();
        filasDeTabla = sorted(filasDeTabla, key=lambda e: AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(
            self.tabla.item(e)["values"][1], self.tabla.item(e)["values"][2]))
        
        for index,k in enumerate(filasDeTabla):
            self.tabla.move(k, '', index)

    def actualizarLabelsDeSemanas(self):
        self.administradorDeFecha.actualizarAtributosFecha(self.contadorSiguienteSemana)
        self.labelFechaInferior.config(text=AdministradorDeFechas.mostrarFormateadaFechaDiaMes(self.administradorDeFecha.fechaLimiteInferior))
        self.labelFechaSuperior.config(text=AdministradorDeFechas.mostrarFormateadaFechaDiaMes(self.administradorDeFecha.fechaLimiteSuperior))

    def siguienteSemana(self,e):
        self.contadorSiguienteSemana += 7
        self.actualizarLabelsDeSemanas();
        self.cargarTablaPorSemana();
        
    def anteriorSemana(self,e):
        self.contadorSiguienteSemana -= 7
        self.actualizarLabelsDeSemanas();
        self.cargarTablaPorSemana();

    def modificarFila(self,evento,indiceFila):
       self.tabla.item(indiceFila, values=(evento.titulo,
                                     evento.fecha,
                                     evento.hora,
                                     evento.duracion,
                                     evento.descripcion,
                                     self.esImportante(evento.importancia)),
                                    tags=self.colorFilaImportante(evento.importancia))
       self.agregarFechaOrdenada();
       messagebox.showinfo("Evento modificado","Evento modificado con éxito");
    
    def filtrarPorMes(self):
        self.cargarRegistrosDelMesEnTabla();
        self.botonMesSiguiente.grid(row=1, column=3)
        self.botonMesAnterior.grid(row=1,column=2);
    
    def siguienteMes(self,e):
        self.administradorDeFecha.aumentarMes();
        self.administradorDeFecha.getMesActual(self.administradorDeFecha.fechaUltimoDia);
        self.labelMesActual.config(text=self.administradorDeFecha.getNombreMesActual());
        self.cargarRegistrosDelMesEnTabla();        
        
    def mesAnterior(self,e):
        self.administradorDeFecha.restarMes();
        self.administradorDeFecha.getMesActual(self.administradorDeFecha.fechaPrimerDia);
        self.labelMesActual.config(text=self.administradorDeFecha.getNombreMesActual());
        self.cargarRegistrosDelMesEnTabla(); 
    
    def seleccionDeFiltro(self,e):
        self.botonAnteriorSemana.grid_forget();
        self.botonSiguienteSemana.grid_forget();
        self.botonMesSiguiente.grid_forget();
        self.botonMesAnterior.grid_forget();
        self.labelFechaInferior.grid_forget();
        self.labelFechaSuperior.grid_forget();
        self.labelMesActual.grid_forget();
        if(self.comboOpcionesDeFiltro.get()=="Filtrar por Semana"):            
            self.cargarTablaPorSemana();
            self.botonSiguienteSemana.grid(row=1,column=3);
            self.botonAnteriorSemana.grid(row=1,column=2);
            self.labelFechaInferior.grid(row=2,column=0,columnspan=2);
            self.labelFechaSuperior.grid(row=2, column=2, columnspan=2);
        else:
            self.labelMesActual.config(text = self.administradorDeFecha.getNombreMesActual())
            self.labelMesActual.grid(row=2, column=1, columnspan=2);
            self.filtrarPorMes();

    def buscarEvento(self):
        valorDelInput = self.ingresobuscarEvento.get();
        listaDeCoincidencias = EventosYEtiquetasModelos().get_eventos_por_etiqueta(self.conexionDB,valorDelInput);
        if(len(listaDeCoincidencias)>0):
            self.eliminarFilas();
            self.cargarTabla(listaDeCoincidencias);
        else:
            messagebox.showinfo("Sin coincidencias",
                                "No se encontraron eventos que coincidan con " + valorDelInput);
