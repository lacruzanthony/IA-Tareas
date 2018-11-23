from constraint import Problem
from collections.abc import Iterable
import os

PROMEDIO = 1.0
TOTAL_TRABAJO = 0
TAREA = 0
MAXIMO_TAREA = 0

class Trabajador:
    def __init__ (self, id, capacidad, trabajo, porcentajeOcupado):
        self.id = id
        self.trabajo = trabajo
        self.capacidad = capacidad
        self.porcentajeOcupado = porcentajeOcupado

        @property
        def trabajo(self):
            return self.trabajo

        @property 
        def porcentajeOcupado(self):
            return self.porcentajeOcupado

        @trabajo.setter
        def trabajo(self, value) :
            self.trabajo = self.trabajo + value

        @porcentajeOcupado.getter
        def porcentajeOcupado(self):
            return self.porcentajeOcupado

def ImprimirSalida(promedio, trabajadores):
    print("Trabajos asignados: ") 
    
    if(trabajadores) :
        for trabajador in trabajadores :
            print (trabajador.trabajo, end=" ")
    
    print("\nPromedio de la carga del trabajo:", promedio*100 , "%")
    os._exit(1)

def MenosOcupado(trabajadores) :
    equipo = list()
    for trabajador in trabajadores :
        if (trabajador.porcentajeOcupado < 1.0) :
            equipo.append(trabajador)
    
    sorted(equipo, key=lambda trabajador:trabajador.porcentajeOcupado)
        
    return equipo

def NoHayNadieMas(trabajador):
    trabajador.trabajo += 1
    trabajador.porcentajeOcupado = trabajador.trabajo / trabajador.capacidad

def TerminarTrabajo (trabajadores):
    global TOTAL_TRABAJO
    global TAREA
    while TAREA != 0 :
        t = trabajadores.pop()
        t.trabajo += 1
        t.porcentajeOcupado = t.trabajo/t.capacidad
        trabajadores.insert(0,t)
        TOTAL_TRABAJO += t.porcentajeOcupado
        TAREA -= 1
    
    return TOTAL_TRABAJO

def TrabajoListo (trabajadores) :
    maximo_tarea = 0
    for trabajador in trabajadores :
        maximo_tarea += trabajador.trabajo

    return maximo_tarea == MAXIMO_TAREA if True else False


def TrabajadoresDesocupados(trabajadores):
    estanDesocupados = False
    for trabajador in trabajadores :
        if(trabajador.capacidad - trabajador.trabajo > 1) :
            estanDesocupados = True
            break
    if(not estanDesocupados and not TrabajoListo(trabajadores)) :
        trabajador = MenosOcupado(trabajadores)
        TerminarTrabajo(trabajador)
             
    return estanDesocupados

def TrabajadoresIgual(trabajadores) :
    capacidades = list()
    for trabajador in trabajadores:
        capacidades.append(trabajador.capacidad)
    
    return capacidades[1:] == capacidades[:-1]

def Supervisar(trabajadores) :
    global TOTAL_TRABAJO
    global TAREA
    cargaColega = 1.0
    primeraAsignacion = False
    for idx, trabajador in enumerate(trabajadores) :
        desocupados = TrabajadoresDesocupados(trabajadores)
        if(TAREA == 0 ) : return TOTAL_TRABAJO / len(trabajadores)

        if(TrabajadoresIgual(trabajadores)):
            trabajo = trabajador.trabajo + 1
            capacidad = trabajador.capacidad
            if(trabajo < capacidad) : 
                trabajador.trabajo += 1
            if(trabajador.trabajo + 1 == capacidad) :
                trabajador.trabajo += 1
                trabajador.porcentajeOcupado = trabajador.trabajo / capacidad
            TAREA -= 1
            TOTAL_TRABAJO += trabajador.trabajo / trabajador.capacidad

        if(desocupados and not trabajador.capacidad == 1 and TAREA != 0) :
            trabajo = trabajador.trabajo + 1
            capacidad = trabajador.capacidad
            if((trabajo / capacidad) <= cargaColega) :
                if(primeraAsignacion and trabajadores[idx-1]) : 
                    trabajadores[idx-1].porcentajeOcupado -= 1/trabajadores[idx-1].capacidad
                    trabajadores[idx-1].trabajo = trabajadores[idx-1].trabajo -1

                primeraAsignacion = True
                trabajador.trabajo = trabajo
                cargaColega = trabajo / capacidad
                trabajador.porcentajeOcupado = cargaColega
    
    for porcentaje in trabajadores:
        TOTAL_TRABAJO += porcentaje.porcentajeOcupado

    promedioTrabajo = TOTAL_TRABAJO / len(trabajadores)
    TOTAL_TRABAJO = 0
    return(promedioTrabajo)
    
def Trabajar(trabajadores) :
    return Supervisar(trabajadores)

def Balanceo (trabajadores) :
    global TAREA
    problema = Problem()
    variables = list()
    for objTrabajador in trabajadores:
        dominio = range(0, objTrabajador.capacidad+1)
        variable = str(objTrabajador.id)
        variables.append(problema.addVariable(variable, dominio))

    while (TAREA > 0) :
        promedioActual = Trabajar(trabajadores)
        TAREA -= 1
    
    ImprimirSalida(promedioActual, trabajadores)

def HayTrabajadores(trabajadores) :

    return len(trabajadores) == 0 if True else False


if __name__ == '__main__':
    
    # Se asume que por cada capacidad, hay 1 trabajador.
    capacidad = input().strip().split()

    dni = 0
    trabajadores = list()
    for i in capacidad:
        if(int(i) != 0):
            trabajadores.append(Trabajador(dni, int(i), 0, 0))
        dni += 1
    
    TAREA = int(input().strip())
    MAXIMO_TAREA = TAREA
    
    bandera = HayTrabajadores(trabajadores)
    if (bandera) :
        ImprimirSalida(0, '')
    else:
        Balanceo(trabajadores)
    