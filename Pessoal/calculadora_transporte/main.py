from math import ceil
import contaDias
import calendar
import openpyxl as xl
from openpyxl.utils import get_column_letter

dataAtual = contaDias.getDate()
quntDias = contaDias.quantDias(dataAtual[1], dataAtual[2])
month = calendar.month(dataAtual[2], dataAtual[1])

def dinheiroGasto():
    passagem = 4.40
    total = quntDias * passagem
    total = ceil(total)
    return total

total = dinheiroGasto()

planilha = xl.Workbook()

# Seleciona a active Sheet
ws1 = planilha.active
# Rename it
ws1.title = 'my test'

# Escreve alguns dados
for col in range(1,5):
    for row in range(1,6):
        letter = get_column_letter(col)
        ws1[letter + str(row)] = letter + str(row)

# Cria nova sheet
ws2 = planilha.create_sheet(title="Ok")
ws2["C1"] = "OK"# Salva arquivo (Se não colocar o caminho complete, ele salva
# na mesma pasta do scritp.
planilha.save('Text.xlsx')