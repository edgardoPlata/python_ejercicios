import datetime
import holidays


   
    # Función para validar si una fecha es válida
def es_fecha_valida(fecha_str):
        try:
            datetime.datetime.strptime(fecha_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    # Función para validar si una hora es válida
def es_hora_valida(hora_str):
        try:
            datetime.datetime.strptime(hora_str, '%H:%M')
            return True
        except ValueError:
            return False

    # Función para verificar la disponibilidad del colaborador
def verificar_disponibilidad(fecha, hora, pais, nombre_str):
        # Validar fecha y hora
        if not es_fecha_valida(fecha) or not es_hora_valida(hora):
            return "Fecha u hora inválida"
        
        # Definir los países donde Banco Lafise tiene presencia
        paises_con_presencia = ['NI', 'CR', 'PR', 'HN', 'GT', 'PA']
        
        # Verificar si el país es válido
        if pais not in paises_con_presencia:
            return "El país seleccionado no es válido"

        # Crear un objeto de la clase Holidays para el país seleccionado
        objeto_feriados = getattr(holidays, pais)()

        # Convertir la fecha de texto a objeto datetime
        fecha_obj = datetime.datetime.strptime(fecha, '%Y-%m-%d')
        
        # Verificar si el día es laboral (lunes a viernes)
        if fecha_obj.weekday() >= 5:
            return f"No es un día laboral en {nombre_str}"
        
        # Verificar si es un día feriado
        if fecha_obj in objeto_feriados:
            motivo_feriado = objeto_feriados.get(fecha_obj)
            return f"No es laboral en {nombre_str} debido a {motivo_feriado}"
        
        # Definir rangos de horas laborales
        hora_inicio = datetime.datetime.strptime("08:00", '%H:%M').time()
        hora_fin_semana = datetime.datetime.strptime("12:00", '%H:%M').time()
        hora_fin_semana_laboral = datetime.datetime.strptime("17:00", '%H:%M').time()
        
        hora_obj = datetime.datetime.strptime(hora, '%H:%M').time()
        
        # Verificar disponibilidad basada en horario laboral
        if (fecha_obj.weekday() < 5 and (hora_obj < hora_inicio or hora_obj > hora_fin_semana_laboral)) or \
        (fecha_obj.weekday() == 5 and (hora_obj < hora_inicio or hora_obj > hora_fin_semana)):
            return f"El colaborador de {nombre_str} no estará disponible en ese horario"
        
        return f"El colaborador de {nombre_str} está disponible en ese horario"

    # Solicitar entrada de usuario

nombre_compania = input("Nombre de la compañía: ")
fecha_entrada = input("Ingrese la fecha (YYYY-MM-DD): ")
hora_entrada = input("Ingrese la hora (HH:MM): ")
pais_entrada = input("Ingrese el país (NI, CR, PR, HN, GT, PA): ")

        # Obtener y mostrar el resultado
resultado = verificar_disponibilidad(fecha_entrada, hora_entrada, pais_entrada, nombre_compania)
print(resultado)
    
