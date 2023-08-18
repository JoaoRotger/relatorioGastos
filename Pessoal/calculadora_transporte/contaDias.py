import datetime

def getDate():
    dataAgora = datetime.datetime.now()
    year = int(datetime.datetime.strftime(dataAgora, '%Y'))
    month = int(datetime.datetime.strftime(dataAgora, '%m'))
    day = int(datetime.datetime.strftime(dataAgora, '%d'))
    return day, month, year

def getMonthStr():
    month = getDate()
    return {
        'Janeiro'   : 1,
        'Fevereiro' : 2,
        'Março'     : 3,
        'Abril'     : 4,
        'Maio'      : 5,
        'Junho'     : 6,
        'Julho'     : 7,
        'Agosto'    : 8,
        'Setembro'  : 9,
        'Outubro'   : 10,
        'Novembro'  : 11,
        'Dezembro'  : 12
    }.get(month[1])

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


mes = getMonthStr()
print(mes)