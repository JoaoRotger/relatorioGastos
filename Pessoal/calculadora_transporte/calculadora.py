import requests
import json
import datetime
from urllib3 import disable_warnings
import calendar

disable_warnings()

dataAtual = datetime.datetime.today().strftime('%d/%m/%Y')
mesAtual = datetime.datetime.today().strftime('%m/%Y')
aa = int(datetime.datetime.today().strftime('%Y'))
mm = int(datetime.datetime.today().strftime('%m'))
print(mesAtual)
print(calendar.month(aa, mm))