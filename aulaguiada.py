import datetime

dia_de_nasc = date(day=2, year=1935, month=2)

calcular_dias_de_vida(dia_de_nasc)
def calcular_dias_de_vida(data):
    if data is None:
        error = 'opss'
        return error

    hoje = datetime.date.today
    dias_de_vida= hoje - data
