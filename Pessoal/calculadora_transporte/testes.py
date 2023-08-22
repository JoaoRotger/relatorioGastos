from datetime import datetime, timedelta

def dias_do_mes(ano, mes):
    primeiro_dia = datetime(ano, mes, 1)
    proximo_mes = primeiro_dia.replace(day=28) + timedelta(days=4)
    ultimo_dia = proximo_mes - timedelta(days=proximo_mes.day)
    
    dias = []
    dia_atual = primeiro_dia
    while dia_atual <= ultimo_dia:
        dias.append(dia_atual)
        dia_atual += timedelta(days=1)
    
    return dias

def obter_nome_dia_semana(numero_dia_semana):
    diasUteis = []
    nomes_dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    #diasUteis.append({nomes_dias[numero_dia_semana] : })
    #print(diasUteis)
    return nomes_dias[numero_dia_semana]

ano = 2023
mes = 9
lista_dias = dias_do_mes(ano, mes)
print(lista_dias)
lista = {}
for dia in lista_dias:
    #print(dia)
    #print(dia.weekday())
    nome_dia_semana = obter_nome_dia_semana(dia.weekday())
    #print(f"{dia.strftime('%d/%m/%Y')} - {nome_dia_semana}")
