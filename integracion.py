import diccionario
import ahorcado
import constantes as const
import random


# Cambie esta valiable para que acepte si desea letras o no y cuantas
def seleccion_palabra(desea_letras, cant_letras):
    """
    Autor: Federico Aldrighetti.

    Esta función pregunta al usuario si quiere jugar con una cantidad determinada de letras. Si dice que sí,
    le pide que especifique la cantidad y le da la palabra con esa longitud validada. En caso contrario, le
    proporciona una palabra con una longitud al azar.
    """

    dicc = diccionario.devolver_diccionario()

    if desea_letras.lower() == 'si' or desea_letras.lower() == "no":
        while not cant_letras.isnumeric() or diccionario.elegir_palabra(dicc, int(cant_letras)) == None:
            if not cant_letras.isnumeric():
                cant_letras = input('Ingrese cantidad de letras correcta: ')
            elif diccionario.elegir_palabra(dicc, int(cant_letras)) == None:
                cant_letras = input(f'No hay palabras con esa longitud. Elige una longitud entre {const.LONGITUD_MINIMA_PALABRA} y {const.LONGITUD_MAXIMA_PALABRA}: ')

        palabra_adivinar = diccionario.elegir_palabra(dicc, int(cant_letras))

    return palabra_adivinar


def asignar_palabras_jugadores(nombres_jugadores):
    """
    Autor: Facundo Sanso.

    Asigna una palabra a cada uno de los jugadores.
    La longitud de todas las palabras será la misma y corresponderá al valor ingresado por el primer jugador.

    """
    saber_si_quiere_letras = "" # Pregunta si quiere letras
    
    while saber_si_quiere_letras.lower() != "si" and saber_si_quiere_letras.lower() != "no":
        saber_si_quiere_letras = input(const.DESEA_LETRAS)    
    
    if saber_si_quiere_letras == "si":
        cant_letras = input('Cuantas letras? ')
    
    elif saber_si_quiere_letras == "no":
        # En el caso de "no" se crea una lista con las longuitudes que tenemos
        lista = list(range(5, 16))
        # Se elige un numero al azar de esa lista que sera la cantidad de letras
        cant_letras = str(random.choice(lista))
    
    palabras_asignadas = {}  # Diccionario con nombres de los jugadores y su palabra asignada
    
    for jugador in nombres_jugadores:
        # Por cada jugador elige una palabra
        palabra_a_adivinar = seleccion_palabra(saber_si_quiere_letras, cant_letras)
        # Las sube al diccionario
        palabras_asignadas[jugador] = palabra_a_adivinar
        
    print(palabras_asignadas)

    return palabras_asignadas  # Para ver la lista


def actualizar_estadisticas_acumuladas(dicc_estadisticas_acumuladas, dicc_estadisticas_partida):
    """
    Actualiza las estadísticas acumuladas de todas las partidas.
    Ordena los datos de los jugadores en base a su puntaje total.

    Parámetros:
        - dicc_estadisticas_acumuladas: estadísticas de todas las partidas anteriores.
        - dicc_estadisticas_partida: estadísticas de la última partida jugada.

    """
    # TODO: Completar!

    return dicc_estadisticas_acumuladas


def mostrar_resultados_acumulados(dicc_estadisticas_acumuladas, cant_partidas):
    print("Resultados Generales:")
    print(f"Cantidad de partidas jugadas: {cant_partidas}")

    for jugador in dicc_estadisticas_acumuladas:
        print(f"Jugador {jugador}")
        print(f"Puntaje Total: {dicc_estadisticas_acumuladas[jugador][0]}")
        print(f"Cantidad de aciertos: {dicc_estadisticas_acumuladas[jugador][1]}")
        print(f"Cantidad de desaciertos: {dicc_estadisticas_acumuladas[jugador][2]}")
        print(f"Cantidad de victorias: {dicc_estadisticas_acumuladas[jugador][3]}")


def jugar_una_partida(nombres_jugadores, nombre_ultimo_ganador):
    """
    TODO: Añadir descripción

    """
    nombres_jugadores = ahorcado.asignar_turno_jugadores(nombres_jugadores, nombre_ultimo_ganador)
    ahorcado.informar_turnos_jugadores(nombres_jugadores)
    dicc_palabras = asignar_palabras_jugadores(nombres_jugadores)

    dicc_estadisticas_partida = {}
    for jugador in dicc_palabras:
        dicc_estadisticas_partida[jugador] = [dicc_palabras[jugador], 0, [], [], False]

    existe_ganador = False
    todos_perdieron = False
    cant_perdedores = 0
    
    while not existe_ganador and not todos_perdieron:
        i = 0

        while i < len(nombres_jugadores) and not existe_ganador and not todos_perdieron:

            jugador = nombres_jugadores[i]
            
            if ahorcado.tiene_intentos(dicc_estadisticas_partida[jugador][3]):
                print(f"\n====================== Turno de {jugador} ======================")
                dicc_estadisticas_partida[jugador] = ahorcado.jugar_ahorcado(dicc_estadisticas_partida[jugador])

                if dicc_estadisticas_partida[jugador][4]:
                    existe_ganador = True
                    nombre_ultimo_ganador = jugador
            
            else:
                cant_perdedores += 1
                if cant_perdedores == len(nombres_jugadores):
                    todos_perdieron = True

            i += 1

    return dicc_estadisticas_partida, nombre_ultimo_ganador


def jugar_multiples_partidas():
    """
    TODO: Añadir descripción

    """
    nombres_jugadores = ahorcado.solicitar_nombres_jugadores()

    cant_partidas = 0
    dicc_estadisticas_partida = {}
    dicc_estadisticas_acumuladas = {}

    seguir_jugando = "si"
    nombre_ultimo_ganador = ""

    while seguir_jugando.lower() == "si":

        dicc_estadisticas_partida, nombre_ultimo_ganador = jugar_una_partida(nombres_jugadores, nombre_ultimo_ganador)

        dicc_estadisticas_acumuladas = actualizar_estadisticas_acumuladas(dicc_estadisticas_acumuladas, dicc_estadisticas_partida)

        cant_partidas += 1

        mostrar_resultados_acumulados(dicc_estadisticas_acumuladas, cant_partidas)

        while seguir_jugando not in ["si", "no"]:
            seguir_jugando = input(f"\n{const.SEGUIR_JUGANDO}")

    print(const.MENSAJE_DESPEDIDA)


jugar_multiples_partidas()