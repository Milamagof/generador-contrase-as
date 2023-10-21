import string
import random

#establece la longitud de la contraseña
longitud = int(input("Ingrese el tamaño de la contraseña: "))

#genera los caracteres para usar en la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

#genera aleatoreamente la contraseña con la longitud específica
contraseña = "".join(random.choice (caracteres) for i in range(longitud))

#imprime la contraseña
print("La contraseña generada es: " + contraseña)