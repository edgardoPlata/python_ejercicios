# [Con la librería de Holidays crear un algoritmo que al recibir una fecha,hora y company id 

# Determinar la disponibilidad de un colaborador tomando en cuenta los paises donde banco lafise tiene presencia:

# Si es un día laboral.

# Si es un día feriado.

# Jornada laboral de lunes a viernes de 8am a 5pm y de sábado de 8am y 12pm ,  si la hora no está en ese rango, el colaborador no estará disponible.

# Validar los campos de entrada.]

import holidays
from datetime import datetime

#Paises 
countries_with_holidays = ['NI', 'CR', 'PR', 'HN', 'GT', 'PA']

# Función para validar si una fecha es un día laboral (lunes a viernes)
def is_weekday(date):
    return date.weekday() < 5  # 0 a 4 corresponden a lunes a viernes

# Función para validar si una hora está dentro del rango de jornada laboral
def is_working_hour(time):
    return time >= datetime.strptime('08:00', '%H:%M').time() and \
           time <= datetime.strptime('17:00', '%H:%M').time() or \
           time >= datetime.strptime('08:00', '%H:%M').time() and \
           time <= datetime.strptime('12:00', '%H:%M').time()

# Función principal para determinar la disponibilidad del colaborador
def check_collaborator_availability(date_str, time_str, company_id):
    try:
        # Validar campos de entrada
        date = datetime.strptime(date_str, '%Y-%m-%d')
        time_obj = datetime.strptime(time_str, '%H:%M').time()
        
        # Validar si es un día laboral y hora dentro del rango de jornada laboral
        if is_weekday(date) and is_working_hour(time_obj):
            # Validar si es un día feriado en alguno de los países
            for country in countries_with_holidays:
                if date in holidays.CountryHoliday(country, years=date.year):
                    return f"El colaborador con company id {company_id} no está disponible debido a que es un día feriado en el país {country}."
            return f"El colaborador con company id {company_id} está disponible para trabajar en la fecha {date_str} a las {time_str}."
        else:
            return f"El colaborador con company id {company_id} no está disponible debido a que es un día no laboral o la hora está fuera del rango de jornada laboral."
    except ValueError:
        return "Error: Fecha u hora ingresada en formato incorrecto."

# Ejemplo de uso

fecha = input("Ingrese Date: ")
hora = input("Hora: ")
company_id = input("StarUP: ")

resultado = check_collaborator_availability(fecha, hora, company_id)
print(resultado)
