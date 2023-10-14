"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """

    data_structs = {
        "results": lt.newList(),
        "goalscorers": lt.newList(),
        "shootouts": lt.newList(),

        "teams": mp.newMap(),
        "scorers": mp.newMap(),
        "tournaments": mp.newMap()
    }

    return data_structs


# Funciones para agregar informacion al modelo

def add_data_results(data_structs, diccionario):
    """
    Función para agregar nuevos elementos a la lista
    """
    results = data_structs["results"]
    teams = data_structs["teams"]
    lt.addLast(results,diccionario)
    diccionario["date"] = datetime.fromisoformat(diccionario["date"])

    home_team = diccionario["home_team"]
    away_team = diccionario["away_team"]

    add_team(home_team, data_structs, diccionario, "local")
    add_team(away_team, data_structs, diccionario, "visitante")
    
def add_team(team, data_structs, diccionario, condicion):
    mapa_teams = data_structs["teams"]

    if mp.contains(mapa_teams,team):
        value = me.getValue(mp.get(mapa_teams,team))
    else:
        value = {"local": lt.newList(),
                 "visitante": lt.newList(),
                 "partidos": lt.newList()}
        mp.put(mapa_teams,team,value)
    if condicion == "visitante":
        lt.addLast(value["visitante"],diccionario)
    else: 
        lt.addLast(value["local"],diccionario)
    lt.addLast(value["partidos"],diccionario)


def add_data_goalscorers(data_structs, diccionario):
    """
    Función para agregar nuevos elementos a la lista
    """
    goalscorer = data_structs["goalscorers"]
    lt.addLast(goalscorer,diccionario)
    diccionario["date"] = datetime.fromisoformat(diccionario["date"])

def add_data_shootouts(data_structs, diccionario):
    """
    Función para agregar nuevos elementos a la lista
    """
    shootouts = data_structs["shootouts"]
    lt.addLast(shootouts,diccionario)
    diccionario["date"] = datetime.fromisoformat(diccionario["date"])


def ordenar_fechas(lista):
    merg.sort(lista,sort_date)

def sort_date(data1,data2):
    return data1["date"] > data2["date"]

# def add_map(map, key, data, file):
#    if  mp.contains(map,key):
#        entry = mp.get(map,key)
#        value = me.getValue(entry)
#    else:
#        llave = key
#        value = mp.newMap()
#        mp.put(value,"results",lt.newList())
#        mp.put(value,"goalscorers",lt.newList())
#        mp.put(value,"shootouts",lt.newList())

#    if file == "results":
#        lista= me.getValue(mp.get(value,"results"))
       
#    elif file == "goalscorers":
#        lista= me.getValue(mp.get(value,"goalscorers"))
#    else:
#        lista= me.getValue(mp.get(value,"shootouts"))

#    lt.addLast(lista,data)



# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size_results(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    results = data_structs["results"]
    return lt.size(results)

def data_size_goalscorers(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    goalscorers = data_structs["goalscorers"]
    return lt.size(goalscorers)

def data_size_shootouts(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    shootouts = data_structs["shootouts"]
    return lt.size(shootouts)


def req_1(data_structs, n, equipo, condicion):
    """
    Función que soluciona el requerimiento 1
    """
    mapa_teams = data_structs["teams"]
    diccionario_partidos = me.getValue(mp.get(mapa_teams, equipo))
    if condicion == "local":
        lista = diccionario_partidos["local"]
    elif condicion == "visitante":
        lista = diccionario_partidos["visitante"]
    else:
        lista = diccionario_partidos["partidos"]

    ordenar_fechas(lista)
    return lt.subList(lista,1,n)
    

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
