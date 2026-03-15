import random

# Tu implementacion va aqui
def tirar_dados(jug_n):
    tirada = []
    tirada += [random.randint(1, 6) for _ in range(5)]
    print(f"Jugador {jug_n} ha tirado: {tirada}")
    
    for n in range(2):
        respuesta = input("¿Querés tirar algún dado de nuevo? (s/n): ")

        while respuesta.lower() not in ["s", "n"]:
            respuesta = input("¿Querés tirar algún dado de nuevo? (s/n): ")

        if respuesta.lower() == "s":
            for x in range(len(tirada)):
                res= input(f"Querés tirar el dado {x} de nuevo? (s/n):")

                while res.lower() not in ["s", "n"]:
                    res = input(f"Querés tirar el dado {x} de nuevo? (s/n):")

                if res.lower() == "s":
                    tirada[x] = random.randint(1, 6)
                    
            print(f"Jugador {jug_n} ha tirado: {tirada}")

        elif respuesta.lower() == "n":
            break  
    print(f"Jugador {jug_n} ha terminado su tirada: {tirada}")
    return tirada 

def evaluar_tirada(tirada):
    tirada.sort()
    generala = False
    poker = False
    full = False
    escalera = False 
    nada = False
    if tirada[0] == tirada[4]:
        return 'generala'
    if tirada[0] == tirada[3] or tirada[1] == tirada[4]:
        return 'poker'
    elif (tirada[0] == tirada[2] and tirada[3] == tirada[4]) or (tirada[0] == tirada[1] and tirada[2] == tirada[4]):
        return 'full'
    elif tirada== [1,2,3,4,5] or tirada == [2,3,4,5,6]:
        return 'escalera'
    else:
        nada = True 
        return nada
    
def sumar_puntaje(tirada, jug_n,num):
    num = int(num)
    puntaje = tirada.count(num) * num
    print(f"Jugador {jug_n} ha sumado {puntaje} puntos por el numero {num}")
    return puntaje


def decision(tirada, jug_n, tabla):
    print("¿Qué querés hacer?")
    print("1. Sumar puntaje")
    print("2. Evaluar tirada")
    opcion = input("Ingrese el número de la opción deseada: ")

    while opcion not in ["1", "2"]:
        opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        if tabla[4][1] != 0 and tabla[5][1] != 0 and tabla[6][1] != 0 and tabla[7][1] != 0 and tabla[8][1] != 0:
            print("Ya has sumado puntos para todos los numeros del 1 al 6. Por favor elige otra opción.")
            return decision(tirada, jug_n, tabla)

        else:    
            num = input("que numero queres sumar? (1-6):")

            while num not in ["1", "2", "3", "4", "5", "6"]:
                num = input("que numero queres sumar? (1-6):")  
            
            while tabla[int(num)+3][1] != 0:
                print(f"Ya has sumado puntos para el numero {num}. Por favor elige otro numero.")
                num = input("que numero queres sumar? (1-6):")
                while num not in ["1", "2", "3", "4", "5", "6"]:
                    num = input("que numero queres sumar? (1-6):")
            
            tabla[int(num)+3][1] = sumar_puntaje(tirada, jug_n,num) 

        return tabla
    
    elif opcion == "2":
        resultado = evaluar_tirada(tirada)
        print(f"Jugador {jug_n} ha obtenido: {resultado}")
        if resultado == 'generala':
            tabla[0][1] = 50
        elif resultado == 'poker':
            tabla[1][1] = 40
        elif resultado == 'full':
            tabla[2][1] = 30
        elif resultado == 'escalera':
            tabla[3][1] = 20
        else:
            print("No has obtenido ninguna combinación. Por favor elige otra opción.")
            return decision(tirada, jug_n, tabla)    
        return tabla
    
def main():
    # Aqui ejecutas tus soluciones
    #print(tirar_dados("JUGADOR 1"))
    tabla1 =[['generala', 0], ['poker', 0], ['full', 0], ['escalera', 0], ['puntos 1', 0], ['puntos 2', 0], ['puntos 3', 0], ['puntos 4', 0], ['puntos 5', 0], ['puntos 6', 0]]
    tabla2 =[['generala', 0], ['poker', 0], ['full', 0], ['escalera', 0], ['puntos 1', 0], ['puntos 2', 0], ['puntos 3', 0], ['puntos 4', 0], ['puntos 5', 0], ['puntos 6', 0]]
    tira1 = tirar_dados("JUGADOR 1")
    evaluar_tirada(tira1)
    decision(tira1, "JUGADOR 1", tabla1)
    print(tabla1)


# main
if __name__ == "__main__":
     main()
