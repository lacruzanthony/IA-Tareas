from constraint import Problem

PROMEDIO = 1

class Trabajador:
    def __init__ (self, id, capacidad, trabajo):
        self.id = id
        self.trabajo = trabajo
        self.capacidad = capacidad

def Supervisar(trabajadores) :
    cargaColega = 1.0
    primeraAsignacion = True
    for idx, trabajador in trabajadores :
        trabajo = trabajador.trabajo + 1
        capacidad = trabajador.capacidad
        if((trabajo / capacidad) < cargaColega ) :
            
            if(trabajadores[idx-1] and not primeraAsignacion) : 
                trabajadores[idx-1].trabajo - 1                

            primeraAsignacion = True
            trabajador.trabajo + 1
            cargaColega = capacidad
            totalTrabajo += trabajo/capacidad
    
    promedioTrabajo = totalTrabajo / len(trabajadores)
    
    return(promedioTrabajo)
    


def Trabajar(trabajadores) :
        Supervisar(trabajadores)

def Balanceo (trabajadores, tarea) :
    problema = Problem()
    variables = list()
    for objTrabajador in trabajadores:
        dominio = range(0, int(objTrabajador.capacidad)+1)
        variable = str(objTrabajador.id)
        variables.append(problema.addVariable(variable, dominio))

    while (tarea != 0) :
        problema.addConstraint(Trabajar(trabajadores) <= PROMEDIO)
        tarea -= 1

    print(problema.getSolutions())

if __name__ == '__main__':
    
    # Se asume que por cada capacidad, hay 1 trabajador.
    capacidad = input().strip().split()

    dni = 0
    trabajadores = list()
    for i in capacidad:
        trabajadores.append(Trabajador(dni, i, 0))
        dni += 1

    tarea = input().strip()

    Balanceo(trabajadores, tarea)




