

cant_partidas = 0
cant_victorias1 = 0
cant_victorias2 = 0
print("¡Bienvenido al Piedra, Papel o Tijeras!")
nombre1 = input ("¿Cómo se llamará el jugador 1?: ")
nombre2 = input ("¿Cómo se llamará el jugador 2?: ")

while cant_partidas < 5:
    print("¿Qué eliges?, ", nombre1, ", ¿Piedra, papel o tijeras?: ") 
    jugador1 = input(" ")
    print("¿Qué eliges?, ", nombre2, ", ¿Piedra, papel o tijeras?: ") 
    jugador2 = input(" ")
    if jugador1 == jugador2:
        print("¡Ha sido un empate!")
    elif(jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijeras" and jugador2 == "papel"): 
        print("Ha ganado:", nombre1)
        cant_victorias1 += 1
    else: 
        print("Ha ganado:", nombre2)
        cant_victorias2 += 1
    cant_partidas +=1
    if cant_partidas >= 5:
        print("El juego ha terminado")
    if cant_victorias1 >= 3:
        print(nombre1," ha ganado el juego")
        break
    if cant_victorias2 >= 3:
        print(nombre2," ha ganado el juego")
        break
    





    
         

   
# AGREGAR TURNOS