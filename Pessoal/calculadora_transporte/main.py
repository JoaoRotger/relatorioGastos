import pandas as pd
import contaDias as cd

# Obtém os dias do mês
data = cd.getDate()
dias_do_mes = cd.dias_do_mes()

# Criação do DataFrame
tabela = pd.DataFrame({'Data': dias_do_mes, 'Motivo': 'Transporte Ida e Volta', 'Valor': 8.80})
tabela = tabela[['Data', 'Motivo', 'Valor']]
tabela = tabela.reset_index(drop=True)

# Imprime o DataFrame
print(tabela)

tabela.to_excel(f'Relatorio_de_Gastos_{data[1]}{data[2]}.xlsx', sheet_name=f'{data[1]}{data[2]}')