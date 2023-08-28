def validar_cedula_nicaragua(cedula):
    # Verificar que la cédula tenga 14 caracteres (13 números + 1 letra)
    if len(cedula) != 14:
        return "cedula no comleta"
    
    # Extraer la parte numérica de la cédula (los primeros 13 caracteres)
    cedula_numerica = cedula[:-1]
    
    # Verificar que la parte numérica sea un número
    if not cedula_numerica.isdigit():
        return False
    
    # Extraer la letra de la cédula (el último carácter)
    letra = cedula[-1].upper()
    
    # Definir la cadena de letras válidas
    cadena_valida = "ABCDEFGHJKLMNPQRSTUVWXY"
    
    # Calcular el residuo
    residuo = int(cedula_numerica) % 23
    
    # Obtener la letra correspondiente al residuo
    letra_calculada = cadena_valida[residuo]
    
    # Comparar la letra calculada con la letra de la cédula
    return letra == letra_calculada

# Solicitar cédula al usuario
cedula = input("Ingrese el número de cédula nicaragüense: ")

# Validar y mostrar el resultado
if validar_cedula_nicaragua(cedula):
    print("CÉDULA VALIDA")
else:
    print("CÉDULA INVALIDA")