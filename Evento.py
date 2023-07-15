class Evento:
    def __init__(self, titulo, fecha, hora, duracion, fechaRecordatorio, horaRecordatorio, identificadorEvento, descripcion="", importancia=False):
        self.titulo=titulo;
        self.fecha = self.convertirFechaEnString(fecha);
        self.hora=hora;
        self.duracion=duracion;
        self.descripcion=descripcion
        self.importancia=importancia;
        self.fechaRecordatorio=self.convertirFechaEnString(fechaRecordatorio);
        self.horaRecordatorio=horaRecordatorio;
        self.identificadorEvento=identificadorEvento;
    def getEventoComoDict(self):
        return self.__dict__;
    def convertirFechaEnString(self, fecha):
        return fecha.strftime('%d-%m-%Y')
