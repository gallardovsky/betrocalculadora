import math as m

# hasta el momento solo estan definidas las ecuaciones ya despejadas para cada
# caso en las ecuaciones de movimiento rectilinio en la horizontal, habria que
# establecer una forma de agregar caida libre de forma que las graficas salgan
# adecuadas para ese tipo de movimiento, adicional verificar como agregar el
# movimiento en 2D (parabolico)

# Funciones para la ec(1) que corresponde a:
# vFinal - vInicial = acceleration*time

def eC1_vFinal(acceleration, vInicial, time):
    vFinal = acceleration*time - vInicial
    return vFinal

def eC1_vInicial(acceleration, vFinal, time):
    vInicial = vFinal - a*time
    return vInicial

def eC1_acceleration(vInicial, vFinal, time):
    acceleration = (vFinal - vInicial)/time
    return acceleration

def eC1_time(acceleration, vInicial, vFinal):
    time = (vFinal - vInicial)/acceleration
    return time

# Funciones para la ec(2) que corresponde a:
# xFinal - xInicial = (1/2)*acceleration*time**2 + vInicial*time
# (notese que en las funciones siguiente puse (0.5) en vez de (1/2)
# esto debido a que (1/2) regresa un entero para que regrese un flotante
# tendria que ser (1.0/2) o (1/2.0) que abarca mas espacio)

def eC2_xFinal(acceleration, vInicial, time, xInicial):
    xFinal = (0.5)*acceleration*time**2 + vInicial*time + xInicial
    return xFinal

def eC2_xInicial(acceleration, vInicial, time, xFinal):
    xInicial = xFinal - (0.5)*acceleration*time**2 - vInicial*time
    return xInicial

def eC2_vInicial(acceleration, xFinal, xInicial, time):
    vInicial = (xFinal - xInicial - (0.5)*acceleration*time**2)/time
    return vInicial

def eC2_acceleration(xFinal, xInicial, vInicial, time):
    acceleration = 2*(xFinal - xInicial - vInicial*time)/time**2
    return acceleration

def eC2_time(acceleration, vInicial, xFinal, xInicial):
    time1 = (-vInicial + m.sqrt(vInicial**2 - 4*(0.5)*acceleration*(xInicial - xFinal)))/acceleration
    time2 = (-vInicial - m.sqrt(vInicial**2 - 4*(0.5)*acceleration*(xInicial - xFinal)))/acceleration
    return time1, time2

# Funciones para la ec(3) que corresponde a:
# 2(xFinal - xInicial) = (vFinal - vInicial)*time

def eC3_time(xFinal, xInicial, vFinal, vInicial):
    time = 2*(xFinal - xInicial)/(vFinal - vInicial)
    return time

def eC3_xFinal(xInicial, vFinal, vInicial, time):
    xFinal = (vFinal - vInicial)*t/(0.5) + xInicial
    return xFinal

def eC3_xInicial(xFinal, vFinal, vInicial, time):
    xInicial = xFinal - (vFinal - vInicial)*t/(0.5)
    return xInicial

def eC3_vFinal(xFinal, xInicial, vInicial, time):
    vFinal = 2*(xFinal - xInicial)/time - vInicial
    return vFinal

def eC3_vInicial(xFinal, xInicial, vFinal, time):
    vInicial = 2*(xFinal - xInicial)/time - vFinal
    return vInicial

# Funciones para la ec(3) que corresponde a:
# 2*acceleration*(xFinal - xInicial) = vFinal**2 - vInicial**2

def eC4_acceleration(xFinal, xInicial, vFinal, vInicial):
    acceleration = (0.5)*(vFinal**2 - vInicial**2)/(xFinal - xInicial)
    return acceleration

def eC4_xFinal(acceleration, xInicial, vFinal, vInicial):
    xFinal = (0.5)*(vFinal**2 - vInicial**2)/acceleration + xInicial
    return xFinal

def eC4_xInicial(acceleration, xFinal, vFinal, vInicial):
    xInicial = xFinal - (0.5)*(vFinal**2 - vInicial**2)/acceleration
    return xInicial

def eC4_vFinal(acceleration, xFinal, xIncial, vInicial):
    vFinal = m.sqrt(2*acceleration*(xFinal - xInicial) - vInicial**2)
    return vFinal

def eC4_vInicial(acceleration, xFinal, xIncial, vFinal):
    vInicial = m.sqrt(vFinal**2 - 2*acceleration*(xFinal - xInicial))
    return vInicial
