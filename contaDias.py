import datetime
from datetime import timedelta

def getDate():
    dataAgora = datetime.datetime.now()
    year = int(datetime.datetime.strftime(dataAgora, '%Y'))
    month = int(datetime.datetime.strftime(dataAgora, '%m'))
    day = int(datetime.datetime.strftime(dataAgora, '%d'))
    return day, month, year

def getMonthStr():
    month = getDate()
    return {
        1 : 'Janeiro',
        2 : 'Fevereiro',
        3 : 'Março',
        4 : 'Abril',
        5 : 'Maio',
        6 : 'Junho',
        7 : 'Julho',
        8 : 'Agosto',
        9 : 'Setembro',
        10 : 'Outubro',
        11 : 'Novembro',
        12 : 'Dezembro'
    }.get(month[1])

def dias_do_mes():
    data = getDate()
    ano = data[2]
    mes = data[1]
    primeiro_dia = datetime.datetime(ano, mes, 1)
    proximo_mes = primeiro_dia.replace(day=28) + timedelta(days=4)
    ultimo_dia = proximo_mes - timedelta(days=proximo_mes.day)
    
    dias = []
    dia_atual = primeiro_dia
    while dia_atual <= ultimo_dia:
        if dia_atual.weekday() < 5:  # Verifica se não é sábado (5) ou domingo (6)
            dias.append(dia_atual.strftime('%d/%m/%Y'))
        dia_atual += timedelta(days=1)
    
    return dias

def obter_nome_dia_semana(numero_dia_semana):
    nomes_dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return nomes_dias[numero_dia_semana]

def is_weekday(date):
    # Retorna True se a data é um dia útil (segunda a sexta-feira), False caso contrário
    return date.weekday() < 5

def count_weekdays_in_month(year, month):
    # Retorna o número de dias úteis em um determinado mês
    first_day = datetime.date(year, month, 1)
    last_day = datetime.date(year, month, 28) + datetime.timedelta(days=4)  # Adiciona 4 dias para garantir que inclua o último dia
    
    count = 0
    current_day = first_day
    while current_day <= last_day:
        if is_weekday(current_day):
            count += 1
        current_day += datetime.timedelta(days=1)
    
    return count

def quantDias(month, year):
    if 1 <= month <= 12:
        weekdays_count = count_weekdays_in_month(year, month)
        return weekdays_count
    else:
        print("Mês inválido. Digite um número entre 1 e 12.")
