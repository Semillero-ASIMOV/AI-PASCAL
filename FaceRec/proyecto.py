import math
def metod1():
    print("Usuario si deseas abrir el menu de movimiento rectilineo presiona 1 \n  Si deseas abrir el  menu de caida libre presiona 2")
    varx=input()

    if(varx=="1"):
        print("ingresaste al menú de movimiento rectilineo: \n para distancia presiona 1 \n para posicion presiona 2 \n para velocidad presiona 3")
        vary=input()
        if(vary=="1"):
            print("ingresaste a distancia ")
            print("ingresa velocidad en m/s:")
            vel=float(input())
            print("ingresa tiempo en segundos :")
            tiem=float(input())
            print(str(r_dist(vel,tiem))+"  metros")
        elif(vary=="2"):
            print("ingresaste a posicion")
            print("ingresa velocidad en m/s:")
            vel=float(input())
            print("ingresa posicion inical en metros")
            pi=float(input())
            print("ingresa tiempo en segundos")
            tiem=float(input())
            print(str(r_pos(vel,pi,tiem))+"  en x ")
        elif(vary=="3"):
            print("ingresaste a velocidad")
            print("ingresa distancia en metros")
            dist=float(input())
            print("ingresa tiempo en segundos ")
            tiem=float(input())
            print(str(r_Vel(dist,tiem))+"  m/s")



    if(varx=="2"):
        print("ingresaste al menú de caida libre : \n para posicion final(altura) presiona 1 \n para velocidad presiona 2 ")
        vary=input()
        if(vary=="1"):
            print("ingresaste a altura")
            print("ingresa velocidad F en m/s:")
            vel=float(input())
            print(str(c_alt(vel))+ "  metros")
        elif(vary=="2"):
            print("ingresaste a velocidad")
            print("ingresa altura en m")
            alt=float(input())
            print(str(c_vel(alt))+" m/s")

    print("¿deseas realizar un nuevo calculo?, Si=3 , No =4")
    proc=input()
    if(proc=="3"):
        metod1()
    else:
        print("gracias por usar el software")


def r_Vel(dist, tiem):
    vel = dist / tiem
    return vel


def r_dist(vel, tiem):
    dist = vel * tiem
    return dist


def r_pos(vel, pi, tiem):
    pos = pi + (vel * tiem)
    return pos


def c_vel(alt):
    vel = math.isqrt(int((2 * (alt) * 9.8)))
    return vel


def c_alt(vel):
    tiemp = vel / 9.8
    alt = (9.8 * math.pow(tiemp, 2)) / 2
    return alt


metod1()




