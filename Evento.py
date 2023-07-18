class Evento:
    def __init__(self, titulo, fecha, hora, duracion, identificadorEvento, descripcion="", importancia=False,id=None):
        self.titulo=titulo;
        self.fecha = self.convertirFechaEnString(fecha);
        self.hora=hora;
        self.duracion=duracion;
        self.descripcion=descripcion
        self.importancia=importancia;
        self.identificadorEvento=identificadorEvento;
        self.id=id;
    def getEventoComoDict(self):
        return self.__dict__;
    def convertirFechaEnString(self, fecha):
        return fecha.strftime('%d-%m-%Y')
    