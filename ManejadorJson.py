import json;
from AdministradorDeFechas import AdministradorDeFechas
class ManejadorJson:
    def __init__(self,ruta):
        self.ruta=ruta;
        self.contenedorObjetos=[];
        self.cargarContenedorEvento()
    def comprobarRepitencia(self,evento):
        #if(evento[""])
        pass
    def agregarObjetoAFichero(self, evento):
        tuplaFechaYHora=(" ",evento["fecha"],evento["hora"]);
        if (self.encontrarObjeto(tuplaFechaYHora) == False):
            self.contenedorObjetos.append(evento);          
            self.escribirEnFichero();
            return True
        else:
            return False

    def encontrarObjeto(self, evento):
        eventoAEncontrar=AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(evento[1],evento[2]);
        for indice,objeto in enumerate(self.contenedorObjetos):
            fechaDelEventoAEncontrar = AdministradorDeFechas.unirFechaYHoraCadenasEnDatetime(objeto["fecha"],
                                                                                             objeto["hora"])
            if (eventoAEncontrar == fechaDelEventoAEncontrar):
                return indice,objeto;
        #Si no se encuentra el indice
        return False 
    
    def limpiarCadenas(palabra):

        a, b = 'áéíóú', 'aeiou'
        trans = str.maketrans(a, b);
        return  palabra.translate(trans).strip().upper();
      
    def encontrarEventoPorPalabraClaveOTitulo(self,NombreeventoOPalabraClave):
        cadenaLimpia = ManejadorJson.limpiarCadenas(NombreeventoOPalabraClave);
        eventosCoincidentes=[];
        for evento in self.contenedorObjetos:
            if (cadenaLimpia == ManejadorJson.limpiarCadenas(evento["titulo"]) or cadenaLimpia == ManejadorJson.limpiarCadenas(evento["identificadorEvento"])):
                eventosCoincidentes.append(evento);
        return eventosCoincidentes;
    def eliminarObjeto(self,evento):
        indice=self.encontrarObjeto(evento)[0];
        print("Indice del objeto a eliminar"+ str(indice));
        del self.contenedorObjetos[indice];
        self.escribirEnFichero();
    
    def escribirEnFichero(self):
        with open(self.ruta, "w", encoding="UTF-8") as archivo:
            json.dump(self.contenedorObjetos, archivo)

    def cargarContenedorEvento(self):
        try:
            with open(self.ruta, "r", encoding="UTF-8") as archivo:
                self.contenedorObjetos = json.load(archivo);
        #Si no se encuentra creado el archivo se crea
        except FileNotFoundError:
            print("No se encontro la ruta especificada, Se procedera a crearla");
            archivo=open(self.ruta,"w");
            archivo.close();
        #En caso de que el json exista pero no tenga informacion se incializa con una lista vacia
        except json.JSONDecodeError:
            self.escribirEnFichero();
    
    def obtenerPrimerosSieteDias(self,dias=7):
        listaPrimerosDias=[]
        adminFechas = AdministradorDeFechas();
        for indice,item in enumerate(self.contenedorObjetos):
            fechaAComparar = AdministradorDeFechas.cadenaDeFechaADate(item["fecha"]);
            if (adminFechas.seEncuentraEnLaSemana(fechaAComparar, dias)):
                listaPrimerosDias.append(self.contenedorObjetos[indice]);
        return listaPrimerosDias;

    def obtenerMes(self,mesInferior,mesSuperior):
        listaDeEventosMeses=[];
        for indice, item in enumerate(self.contenedorObjetos):
            fechaAComparar = AdministradorDeFechas.cadenaDeFechaADate(item["fecha"]);
            if (AdministradorDeFechas.comprobarSiSeEncuentraEnElMesActual(fechaAComparar,mesInferior,mesSuperior)):
                listaDeEventosMeses.append(self.contenedorObjetos[indice]);
        return listaDeEventosMeses
