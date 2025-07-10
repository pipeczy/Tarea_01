# Introducción a la Programación - NRC 2432
# Tarea 1: Programación estructurada en Python
# Integrantes: [Nicolas Flores, Mario Robles, Felipe Castro]


import random

# Función principal del juego
def juego_preguntas_respuestas():
    # Variables para almacenar información de los jugadores
    nombre_jugador1 = ""  
    nombre_jugador2 = ""  
    cantidad_preguntas = 0  
    puntaje_jugador1 = 0  
    puntaje_jugador2 = 0  
    
    #region Preguntas
    # Base de datos de preguntas: cada pregunta tiene formato [pregunta, opción_a, opción_b, opción_c, respuesta_correcta]
    # Formato: pregunta = [0], opción a = [1], opción b = [2], opción c = [3], respuesta correcta = [4] 
    preguntas = [
        ["¿Cuál es la capital de Francia?", "Madrid", "París", "Londres", "b"],
        ["¿Quién escribió 'Don Quijote de la Mancha'?", "Miguel de Cervantes", "Gabriel García Márquez", "William Shakespeare", "a"],
        ["¿Cuál es el planeta más grande del sistema solar?", "Saturno", "Júpiter", "Neptuno", "b"],
        ["¿En qué año llegó el hombre a la luna?", "1969", "1968", "1970", "a"],
        ["¿Cuál es el océano más grande del mundo?", "Atlántico", "Índico", "Pacífico", "c"],
        ["¿Quién pintó 'La Mona Lisa'?", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", "b"],
        ["¿Cuál es el río más largo del mundo?", "Amazonas", "Nilo", "Misisipi", "b"],
        ["¿En qué continente se encuentra Egipto?", "Asia", "África", "Europa", "b"],
        ["¿Cuál es el elemento químico más abundante en el universo?", "Hidrógeno", "Oxígeno", "Carbono", "a"],
        ["¿Quién fue el primer presidente de Chile?", "Bernardo O'Higgins", "Manuel Blanco Encalada", "José Miguel Carrera", "b"],
        ["¿Cuál es la montaña más alta del mundo?", "K2", "Everest", "Aconcagua", "b"],
        ["¿En qué año se fundó la ONU?", "1945", "1944", "1946", "a"],
        ["¿Cuál es la capital de Australia?", "Sídney", "Melbourne", "Canberra", "c"],
        ["¿Quién escribió 'Cien años de soledad'?", "Mario Vargas Llosa", "Gabriel García Márquez", "Julio Cortázar", "b"],
        ["¿Cuál es el metal más abundante en la corteza terrestre?", "Hierro", "Aluminio", "Cobre", "b"],
        ["¿En qué país se encuentra Machu Picchu?", "Bolivia", "Ecuador", "Perú", "c"],
        ["¿Cuál es el idioma más hablado en el mundo?", "Inglés", "Chino mandarín", "Español", "b"],
        ["¿Quién desarrolló la teoría de la relatividad?", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "b"],
        ["¿Cuál es el país más pequeño del mundo?", "Mónaco", "Vaticano", "San Marino", "b"],
        ["¿En qué año cayó el Muro de Berlín?", "1989", "1988", "1990", "a"]
    ]
    
    #endregion

    # FASE 1: CONFIGURACIÓN DEL JUEGO
    print("=" * 50)
    print("¡BIENVENIDO AL JUEGO DE PREGUNTAS Y RESPUESTAS!")
    print("=" * 50)
    print("Dos jugadores competirán respondiendo preguntas de cultura general")
    print("Cada jugador tendrá 1 intento por pregunta")
    print()
    
    # Solicitar nombre del primer jugador
    while nombre_jugador1 == "":
        nombre_jugador1 = input("Ingrese el nombre del Jugador 1: ").strip()
        if nombre_jugador1 == "":
            print("El nombre no puede estar vacío. Intente nuevamente.")
    
    # Solicitar nombre del segundo jugador
    while nombre_jugador2 == "":
        nombre_jugador2 = input("Ingrese el nombre del Jugador 2: ").strip()
        if nombre_jugador2 == "":
            print("El nombre no puede estar vacío. Intente nuevamente.")
    
    # Solicitar cantidad de preguntas (máximo 10)
    while cantidad_preguntas <= 0 or cantidad_preguntas > 10:
        try:
            cantidad_preguntas = int(input("Ingrese la cantidad de preguntas por jugador (máximo 10): "))
            if cantidad_preguntas <= 0:
                print("La cantidad debe ser mayor a 0. Intente nuevamente.")
            elif cantidad_preguntas > 10:
                print("La cantidad máxima es 10. Intente nuevamente.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    
    # Verificar que hay suficientes preguntas para el juego
    if cantidad_preguntas * 2 > len(preguntas):
        print("No hay suficientes preguntas para el juego solicitado.")
        return
    
    # FASE 2: JUEGO DE PREGUNTAS Y RESPUESTAS
    print("\n" + "=" * 50)
    print("COMENZANDO EL JUEGO")
    print("=" * 50)
    
    # Crear una lista mezclada de preguntas para que sean diferentes para cada jugador
    preguntas_mezcladas = preguntas.copy()
    random.shuffle(preguntas_mezcladas)
    
    # Asignar preguntas a cada jugador
    preguntas_jugador1 = preguntas_mezcladas[:cantidad_preguntas]
    preguntas_jugador2 = preguntas_mezcladas[cantidad_preguntas:cantidad_preguntas*2]
    
    # Ciclo principal del juego - itera por cada pregunta
    for numero_pregunta in range(cantidad_preguntas):
        print(f"\n--- RONDA {numero_pregunta + 1} ---")
        
        # Turno del Jugador 1
        print(f"\nTurno de {nombre_jugador1}:")
        pregunta_actual = preguntas_jugador1[numero_pregunta]
        
        # Mostrar la pregunta y opciones
        print(f"Pregunta {numero_pregunta + 1}: {pregunta_actual[0]}")
        print(f"a) {pregunta_actual[1]}")
        print(f"b) {pregunta_actual[2]}")
        print(f"c) {pregunta_actual[3]}")
        
        # Solicitar respuesta del jugador 1
        respuesta_jugador1 = ""
        while respuesta_jugador1 not in ["a", "b", "c"]:
            respuesta_jugador1 = input("Ingrese la letra de su respuesta correcta (a-b-c): ").lower().strip()
            if respuesta_jugador1 not in ["a", "b", "c"]:
                print("Por favor ingrese una opción válida (a, b, o c).")
        
        # Verificar respuesta del jugador 1
        if respuesta_jugador1 == pregunta_actual[4]:
            print("¡Tu respuesta es correcta!")
            puntaje_jugador1 += 1  # Incrementar puntaje si es correcta
        else:
            print(f"Tu respuesta es incorrecta. La respuesta correcta era: {pregunta_actual[4]}")
        
        # Turno del Jugador 2
        print(f"\nTurno de {nombre_jugador2}:")
        pregunta_actual = preguntas_jugador2[numero_pregunta]
        
        # Mostrar la pregunta y opciones
        print(f"Pregunta {numero_pregunta + 1}: {pregunta_actual[0]}")
        print(f"a) {pregunta_actual[1]}")
        print(f"b) {pregunta_actual[2]}")
        print(f"c) {pregunta_actual[3]}")
        
        # Solicitar respuesta del jugador 2
        respuesta_jugador2 = ""
        while respuesta_jugador2 not in ["a", "b", "c"]:
            respuesta_jugador2 = input("Ingrese la letra de su respuesta correcta (a-b-c): ").lower().strip()
            if respuesta_jugador2 not in ["a", "b", "c"]:
                print("Por favor ingrese una opción válida (a, b, o c).")
        
        # Verificar respuesta del jugador 2
        if respuesta_jugador2 == pregunta_actual[4]:
            print("¡Tu respuesta es correcta!")
            puntaje_jugador2 += 1  # Incrementar puntaje si es correcta
        else:
            print(f"Tu respuesta es incorrecta. La respuesta correcta era: {pregunta_actual[4]}")
        
        # Mostrar puntajes parciales
        print(f"\nPuntajes actuales:")
        print(f"{nombre_jugador1}: {puntaje_jugador1}")
        print(f"{nombre_jugador2}: {puntaje_jugador2}")
    
    # FASE 3: CIERRE Y DETERMINACIÓN DEL GANADOR
    print("\n" + "=" * 50)
    print("RESULTADOS FINALES")
    print("=" * 50)
    
    # Mostrar puntajes finales
    print(f"Puntaje final de {nombre_jugador1}: {puntaje_jugador1}/{cantidad_preguntas}")
    print(f"Puntaje final de {nombre_jugador2}: {puntaje_jugador2}/{cantidad_preguntas}")
    
    # Determinar y anunciar el ganador
    if puntaje_jugador1 > puntaje_jugador2:
        print(f"\n¡FELICITACIONES! {nombre_jugador1} es el ganador con {puntaje_jugador1} respuestas correctas!")
    elif puntaje_jugador2 > puntaje_jugador1:
        print(f"\n¡FELICITACIONES! {nombre_jugador2} es el ganador con {puntaje_jugador2} respuestas correctas!")
    else:
        print(f"\n¡EMPATE! Ambos jugadores obtuvieron {puntaje_jugador1} respuestas correctas!")
    
    print("\n¡Gracias por jugar!")
    print("=" * 50)

# Ejecutar el juego principal
if __name__ == "__main__":
    juego_preguntas_respuestas()