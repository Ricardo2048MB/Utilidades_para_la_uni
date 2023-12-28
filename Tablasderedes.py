
""" 
    Autor del módulo: Ricardo Muñoz Bolaños
    Fecha de creación: 25 de noviembre de 2023
"""

from netaddr import IPNetwork
from netaddr import IPAddress
from math import ceil
from math import log2

class Segmento(IPNetwork):

    """
    Ésta es simplemente una subclase de IPNetwork que uso para que dé toda la información relevante en la creación de tablas 
    de segmentos IPv4 para la clase de redes de área local. Para instanciar un Segmento se requiere una dirección de red
    en notación CIDR y el nombre del segmento. El método __str__() de ésta subclase está modificado de tal forma que devuelve 
    la información relevante antes mencionada.
    """

    def __init__(self, addr, nombre=None):
        super().__init__(addr)
        self.nombre = nombre

    def __str__(self) -> str:
        if not self.nombre == None:
            cadena = f"\nNombre del segmento: {self.nombre}"
            cadena += f"\nNotación CIDR: {super().__str__()}"
        else:
            cadena = f"\nNotación CIDR: {super().__str__()}"
        cadena += f"\nDirección de red: {self.network}"
        cadena += f"\tDirección de broadcast: {self.broadcast}"
        cadena += f"\nRango de IPs asignables: [{IPAddress(self.first + 1)} - {IPAddress(self.last - 1)}]"
        cadena += f"\nTamaño del segmento: {self.size}"
        cadena += f"\tPrefijo de longitud: {self.prefixlen}"
        cadena += f"\tMáscara de subred: {self.netmask}\n"
        return cadena
    
    def __repr__(self):
        """:return: Representación de una instancia de la clase Segmento."""
        return "%s('%s', '%s')" % (self.__class__.__name__, super().__str__(), self.nombre)
    
    
def filetear(segmento, prefijo=None, primero=False, n_enlaces=None):

    """
        Ésta función recibe el segmento a filetear (requerido), un prefijo, si acaso es el primer segmento, y cuántos enlaces se requieren.
        Los últimos tres son argumentos opcionales, pero en el caso de no usar prefijo, deberá ser porque se están obteniendo los enlaces.
        
        Dada una topología instanciada así: topologia_completa = IPNetwork('192.168.0.0/16')

        Ejemplo de uso:
        
        Primer segmento
        departamento_B = filetear(topologia_completa, prefijo=24, primero=True)
        
        Un segmento que no sea el primero
        departamento_C = filetear(departamento_B, prefijo=25)
        
        Enlaces
        e1, e2, e3 = filetear(topologia_completa, n_enlaces=3)

        ----------------------------------------------------------------------

        También puede hacerse lo siguiente:

        departamento_B = Segmento(filetear(topologia_completa, prefijo=24, primero=True), 'Departamento B')
        departamento_C = Segmento(filetear(departamento_B, prefijo=25), 'Departamento C')
        departamento_A = Segmento(filetear(departamento_C, prefijo=26), 'Departamento A')
        e1, e2, e3 = filetear(topologia_completa, n_enlaces=3)
        e1 = Segmento(e1, 'Enlace 1')
        e2 = Segmento(e2, 'Enlace 2')
        e3 = Segmento(e3, 'Enlace 3')
        topologia_completa = Segmento(topologia_completa, 'Topología')
        
        ----------------------------------------------------------------------
    """
    
    resultado = None
    if primero and prefijo != None:
        resultado = segmento.subnet(prefijo).__next__() # Con esto se obtiene el primer segmento /prefijo del generador, el primer filete.
    elif prefijo != None:
        resultado = segmento.next().subnet(prefijo).__next__() # Con esto se obtiene el primer segmento /prefijo a partir del siguiente segmento con respecto a este.
    elif n_enlaces != None:
        if n_enlaces == 1:
            resultado = list(segmento.subnet(30)).pop()
        elif n_enlaces > 1:
            auxiliar = list(segmento.subnet(30)).pop()
            resultado = list()
            resultado.append(auxiliar)
            for i in range(n_enlaces - 1):
                resultado.append(auxiliar.previous(i + 1))
            resultado.reverse()
    return resultado

def calcula_diagonal(hosts, escalabilidad=0):
    """ 
        hosts: El número de hosts en total que habrá en el segmento.
        escalabilidad: El número de hosts que podrían necesitarse en el futuro. (por defecto es 0)
    """
    return 32 - ceil(log2(hosts+2+escalabilidad))