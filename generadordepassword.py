
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
simbolos = "@#$%&/\?¡*!¿()^[]+-¨´`-_|°¬"

Usar_para = lower_case + upper_case + number + simbolos
Longitud_para_pasar = 8

#el .join convierte una lista en una cadena formada por los elementos de la lista separados por comas
contraseña = "".join(random.sample(Usar_para, Longitud_para_pasar))

#el sample devuelve una lista de n elementos extraidos sin repetición
print("tu contraseña generada es: ", contraseña)