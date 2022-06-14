from __future__ import print_function
import json

def validacion_input(input_data, allowed, limit):
    if len(input_data) > limit:
        return True
    elif any(x not in allowed for x in input_data):
        return True
    else:
        return False
    
def Talana_Kombat_JRPG():
    # Posibles movimientos: (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, (P)Puño, (K)Patada

    # Input Player 1
    movimientos_p1 = []
    golpes_p1 = []
    hp_p1 = 6
    accion_p1 = ""
    allowed_characters_m=['W', 'w', 'S', 's', 'A', 'a', 'D', 'd', '']
    allowed_characters_g=['P', 'p', 'K', 'k', '']
    
    
    # Input
    print("Ingrese movimientos para Tonyn")
    for i in range(1, 6):
        print("Posibles movimientos: (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, (Enter)Saltar seleccion")
        #Validar Input
        while True:
            input_mov_p1 = input("Ingrese movimiento {0} (Maximo 5 movimientos por turno) : ".format(i))
            
            if validacion_input(input_mov_p1, allowed_characters_m, 5):
                print("Se deben ingresar como maximo 5 movimientos y solamente los siguientes caracteres: (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, (Enter)Saltar seleccion")
                #better try again... Return to the start of the loop
                continue
            else:
                #we're ready to exit the loop.
                break
        
        # Agregar movimiento a lista
        movimientos_p1.append(input_mov_p1.upper())
        print(movimientos_p1)
    
    print("Ingrese golpes para Tonyn")
    for i in range(1, 6):
        print("Posibles movimientos: (P)Puño, (K)Patada, (Enter)Saltar seleccion")
        #Validar Input
        while True:
            input_gol_p1 = input("Ingrese golpes {0} (Maximo 1 movimiento por turno) : ".format(i))
            
            if validacion_input(input_gol_p1, allowed_characters_g, 1):
                print("Se debe ingresar como maximo 1 movimiento y solamente los siguientes caracteres: (P)Puño, (K)Patada, (Enter)Saltar seleccion")
                #better try again... Return to the start of the loop
                continue
            else:
                #we're ready to exit the loop.
                break
        
        # Agregar movimiento a lista
        golpes_p1.append(input_gol_p1.upper())
        print(golpes_p1)
        
    
    # Input Player 2
    movimientos_p2 = []
    golpes_p2 = []
    accion_p2 = ""
    hp_p2 = 6
    
    #Input
    print("Ingrese movimientos para Arnaldor")
    for i in range(1, 6):
        print("Posibles movimientos: (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, (Enter)Saltar seleccion")
        #Validar Input
        while True:
            input_mov_p2 = input("Ingrese movimiento {0} (Maximo 5 movimientos por turno) : ".format(i))
            
            if validacion_input(input_mov_p2, allowed_characters_m, 5):
                print("Se deben ingresar como maximo 5 movimientos y solamente los siguientes caracteres: (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha, (Enter)Saltar seleccion")
                #better try again... Return to the start of the loop
                continue
            else:
                #we're ready to exit the loop.
                break
        
        # Agregar movimiento a lista
        movimientos_p2.append(input_mov_p2.upper())
        print(movimientos_p2)
        
    print("Ingrese golpes para Arnaldor")
    for i in range(1, 6):
        print("Posibles movimientos: (P)Puño, (K)Patada, (Enter)Saltar seleccion")
        #Validar Input
        while True:
            input_gol_p2 = input("Ingrese golpes {0} (Maximo 1 movimiento por turno) : ".format(i))
            
            if validacion_input(input_gol_p2, allowed_characters_g, 1):
                print("Se debe ingresar como maximo 1 movimiento y solamente los siguientes caracteres: (P)Puño, (K)Patada, (Enter)Saltar seleccion")
                #better try again... Return to the start of the loop
                continue
            else:
                #we're ready to exit the loop.
                break
        
        # Agregar movimiento a lista
        golpes_p2.append(input_gol_p2.upper())
        print(golpes_p2)
    
    # Combate
    # Crear Json
    combat = {"player1": {"movimientos": movimientos_p1, "golpes": golpes_p1}, "player2": {"movimientos": movimientos_p2, "golpes": golpes_p2}}
    
    data = json.dumps(combat)
    loaded_data = json.loads(data)
    
    largo_movimientos = len(loaded_data['player1']['movimientos'])
    
    counter = 1
    
    for m in range(largo_movimientos):
            turno_p1 = False
            daño_p1 = 0
            daño_p2 = 0
            # Revisar largo de movimiento + golpe
            #Player 1
            moveset_p1 = loaded_data['player1']['movimientos'][m] + loaded_data['player1']['golpes'][m]
            moveset_largo_p1 = len(moveset_p1)
            mov_largo_p1 = len(loaded_data['player1']['movimientos'][m])
            gol_largo_p1 = len(loaded_data['player1']['golpes'][m])
            #print(moveset_p1, moveset_largo_p1)
            
            #Player 2
            moveset_p2 = loaded_data['player2']['movimientos'][m] + loaded_data['player2']['golpes'][m]
            moveset_largo_p2 = len(moveset_p2)
            mov_largo_p2 = len(loaded_data['player2']['movimientos'][m])
            gol_largo_p2 = len(loaded_data['player2']['golpes'][m])
            #print(moveset_p2, moveset_largo_p2)
            
            # Revisar ataque especial
            #Player 1
            # DSD + P: Taladoken(3), SD + K: Remuyuken(2), P o K: Puño o Patada(1)
            if moveset_p1[-4:] == "DSDP":
                accion_p1 = "Ataca con Taladoken"
                daño_p1 = 3
            elif moveset_p1[-3:] == "SDK":
                accion_p1 = "Conecta un Remuyuken"
                daño_p1 = 2
            elif moveset_p1[-1:] == "P" and moveset_p1[-4:] != "DSDP":
                accion_p1 = "Realiza un Puñetazo"
                daño_p1 = 1
            elif moveset_p1[-1:] == "K" and moveset_p1[-3:] != "SDK":
                accion_p1 = "Realiza una Patada"
                daño_p1 = 1
            else:
                accion_p1 = "Avanza hacia el oponente"
                daño_p1 = 0
                
            #print(accion_p1)
                
            #Player 2
            #SA + K: Remuyuken(3), ASA + P: Taladoken(2), P o K: Puño o Patada(1)
            if moveset_p2[-3:] == "SAK":
                accion_p2 = "Ataca con Remuyuken"
                daño_p2 = 3
            elif moveset_p2[-4:] == "ASAP":
                accion_p2 = "Conecta un Taladoken"
                daño_p2 = 2
            elif moveset_p2[-1:] == "P" and moveset_p2[-4:] != "ASAP":
                accion_p2 = "Realiza un Puñetazo"
                daño_p2 = 1
            elif moveset_p2[-1:] == "K" and moveset_p2[-3:] != "SAK":
                accion_p2 = "Realiza una Patada"
                daño_p2 = 1
            else:
                accion_p2 = "Avanza hacia el oponente"
                daño_p2 = 0
            
            #print(accion_p2)    
            
            # Revisar turnos y daño
            if moveset_largo_p1 < moveset_largo_p2:
                turno_p1 = True
            elif moveset_largo_p1 == moveset_largo_p2:
                if mov_largo_p1 < mov_largo_p2:
                    turno_p1 = True
                elif mov_largo_p1 == mov_largo_p2:
                    if gol_largo_p1 < gol_largo_p2:
                        turno_p1 = True
                    elif gol_largo_p1 == gol_largo_p2:
                        turno_p1 = True
                        
            #print(turno_p1)
            
            # Combate
            if turno_p1:
                if hp_p1 > 0:
                    print("Turno {} de player 1".format(counter))
                    counter = counter + 1
                    hp_p2 = hp_p2 - daño_p1
                    print("Tonyn {}, genera un daño de {} y deja a Arnaldor con {} de vida".format(accion_p1, daño_p1, hp_p2))
                else:
                    print("Tonyn ha sido derrotado")
                
                if hp_p2 > 0:
                    print("Turno {} de player 2".format(counter))
                    counter = counter + 1
                    hp_p1 = hp_p1 - daño_p2
                    print("Arnaldor {}, genera un daño de {} y deja a Tonyn con {} de vida".format(accion_p2, daño_p2, hp_p1))
                else:
                    print("Arnaldor ha sido derrotado")
                
                # Revisión de daño
                if hp_p1 <= 0:
                    print("Arnaldor es el ganador!")
                    break
                elif hp_p2 <= 0:
                    print("Tonyn es el ganador!")
                    break  

            else:
                if hp_p2 > 0:
                    print("Turno {} de player 2".format(counter))
                    counter = counter + 1
                    hp_p1 = hp_p1 - daño_p2
                    print("Arnaldor {}, genera un daño de {} y deja a Tonyn con {} de vida".format(accion_p2, daño_p2, hp_p1))
                else:
                    print("Arnaldor ha sido derrotado")
                
                if hp_p1 > 0:
                    print("Turno {} de player 1".format(counter))
                    counter = counter + 1
                    hp_p2 = hp_p2 - daño_p1
                    print("Tonyn {}, genera un daño de {} y deja a Arnaldor con {} de vida".format(accion_p1, daño_p1, hp_p2))
                else:
                    print("Tonyn ha sido derrotado")
                
                # Revisión de daño
                if hp_p1 <= 0:
                    print("Arnaldor es el ganador!")
                    break
                elif hp_p2 <= 0:
                    print("Tonyn es el ganador!")
                    break
                
                    
    print("Fin de combate")
    
    
Talana_Kombat_JRPG()
    
    