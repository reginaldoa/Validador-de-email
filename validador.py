arquivos = open('arquivo.txt','w')

import DNS
from validate_email import validate_email
import pandas as pd

base = pd.read_excel("Pasta1.xlsx")

contar_erros = 0
contar_linha = 0


while contar_erros < 1000 :
     
    for poupadores in base["EMAIL"]:
      contar_linha += 1
      print(contar_linha)
      try: 
        valido = validate_email(poupadores, verify = True, smtp_timeout= 5.0)
        base = pd.read_excel("Pasta1.xlsx", skiprows= contar_linha)
        if valido == True:
          print(f"{poupadores}, EMAIL EXISTE",file=arquivos)
          print(f"{poupadores}, EMAIL EXISTE")
        else:    
          print(f"{poupadores}, NAO ",file=arquivos)
          print(f"{poupadores}, NAO ")
      except Exception as e :
          print(f"{poupadores}, NAO EXISTE/SMTP NAO PODE SER VERIFICADO",file=arquivos)
          print(f"{poupadores}, NAO EXISTE/SMTP NAO PODE SER VERIFICADO")
          base = base.drop(base.index[base.index == base.index[0]])
          contar_erros += 1
          print(f"JÃ DEU {contar_erros} ERROS")
          continue

arquivos.write()
arquivos.close()