import random

# Tu implementacion va aqui
def tirar_dados(jug_n):
    tirada = []
    tirada += [random.randint(1, 6) for _ in range(5)]
    print(f"Jugador {jug_n} ha tirado: {tirada}")

    for n in range(2):

        respuesta = input("Querés tirar algun dado de nuevo? (s/n):")

        while respuesta.lower() not in ["s", "n"]:
            respuesta = input("Querés tirar algun dado de nuevo? (s/n):")

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
        
    return tirada 

def evaluar_tirada(tirada):
    tirada.sort()
    generala = False
    poker = False
    full = False
    escalera = False 
    nada = False
    if tirada[0] == tirada[4]:
        generala = True
        return generala
    if tirada[0] == tirada[3] or tirada[1] == tirada[4]:
        poker = True
        return poker
    elif (tirada[0] == tirada[2] and tirada[3] == tirada[4]) or (tirada[0] == tirada[1] and tirada[2] == tirada[4]):
        full = True
        return full
    elif tirada== [1,2,3,4,5] or tirada == [2,3,4,5,6]:
        escalera = True
        return escalera
    else:
        nada = True 
        return nada
    
def sumar_puntaje(tirada, jug_n):
    num = input("que numero queres sumar? (1-6)"):
    while num not in ["1", "2", "3", "4", "5", "6"]:
        num = input("que numero queres sumar? (1-6):")
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
            
            tabla[int(num)+3][1] = sumar_puntaje(tirada, jug_n) 

        return tabla
    
    elif opcion == "2":
        resultado = evaluar_tirada(tirada)
        print(f"Jugador {jug_n} ha obtenido: {resultado}")
        if
        return resultado
    
def main():
    # Aqui ejecutas tus soluciones
    #print(tirar_dados("JUGADOR 1"))
    tabla1 =[['generala', 0], ['poker', 0], ['full', 0], ['escalera', 0], ['puntos 1', 0], ['puntos 2', 0], ['puntos 3', 0], ['puntos 4', 0], ['puntos 5', 0], ['puntos 6', 0]]
    tabla2 =[['generala', 0], ['poker', 0], ['full', 0], ['escalera', 0], ['puntos 1', 0], ['puntos 2', 0], ['puntos 3', 0], ['puntos 4', 0], ['puntos 5', 0], ['puntos 6', 0]]




# main
if __name__ == "__main__":
     main()
