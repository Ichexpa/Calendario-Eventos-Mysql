from datetime import date, datetime,timedelta,time;
from calendar import monthrange

class AdministradorDeFechas:

    def __init__(self):
        self.actualizarAtributosFecha(7);

    def cadenaDeFechaADate(fecha):
       return datetime.strptime(fecha,'%d-%m-%Y').date()

    def actualizarAtributosFecha(self,dias):
        fechaActual = datetime.now().date();
        self.fechaLimiteSuperior=fechaActual+timedelta(days=dias);
        self.fechaLimiteInferior = self.fechaLimiteSuperior-timedelta(days=7)

    def seEncuentraEnLaSemana(self,fecha,dias):
        self.actualizarAtributosFecha(dias);
        return fecha >= self.fechaLimiteInferior and fecha <= self.fechaLimiteSuperior
    
    def mostrarFormateadaFechaDiaMes(fecha):
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'];
        return f'{dias[fecha.weekday()]} {fecha.day} de {meses[fecha.month-1]} del {fecha.year}';

    def unirFechaYHoraCadenasEnDatetime(fecha,hora):

        fechaYhora=f'{fecha} {hora}';
        print(fechaYhora)
        fechaYhoraConvertidos=datetime.strptime(fechaYhora,"%d-%m-%Y %H:%M");
        return fechaYhoraConvertidos;

    def getMesActual(self,fecha):

        ultimoDiaDelMes=monthrange(fecha.year,fecha.month);
        self.fechaPrimerDia = date(fecha.year,fecha.month, 1)
        self.fechaUltimoDia = date(fecha.year, fecha.month, ultimoDiaDelMes[1])        
        
    def aumentarMes(self):
        self.fechaUltimoDia = self.fechaUltimoDia+timedelta(days=1)

    def restarMes(self):
        self.fechaPrimerDia=self.fechaPrimerDia-timedelta(days=1);

    def comprobarSiSeEncuentraEnElMesActual(fecha,fechaInferior, fechaSuperior):
        return fecha>=fechaInferior and fecha<=fechaSuperior;

    def getNombreMesActual(self):
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
        return f'{meses[self.fechaPrimerDia.month-1]} del {self.fechaPrimerDia.year}'

    def validarHora(hora, minutos):
        try:
            hora=int(hora);
            minutos=int(minutos);
            print(type(hora))
            print(type(minutos))
            print("test Hora Entro Bien")
            if (hora >= 0 and hora <= 23 and minutos >= 0 and minutos < 60):
                return True
        except ValueError:
            print(f'{hora}:{minutos}');
            print("Agarro campos como invalidos")
            if (hora == "" or minutos == ""):
                return True;
        return False;

    def getFechaFormateada(hora,minutos):
        if (hora == "" or minutos == ""):
            horaActual = datetime.now().time();  
        else:
            horaActual = time(int(hora), int(minutos));
    
        return AdministradorDeFechas.agregarCeroAHoraMinuto(horaActual);
        
    def agregarCeroAHoraMinuto(hora):
        parteHora=str(hora.hour);
        parteMinuto=str(hora.minute);
        if(int(parteHora)<10):
            parteHora="0"+parteHora;
        if(int(parteMinuto)<10):
            parteMinuto="0"+parteMinuto;
        return f'{parteHora}:{parteMinuto}';
    
    def horaYMinutoSeparados(horaString):
        return horaString[:2], horaString[3:]

    def separar_fecha_hora(fechaHoraDt):
        fecha = fechaHoraDt.date().strftime("%d-%m-%Y")
        hora = AdministradorDeFechas.agregarCeroAHoraMinuto(fechaHoraDt.time())
        return fecha, hora

