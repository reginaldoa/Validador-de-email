import smtplib
import dns.resolver
import pandas as pd
import socket

# Configurações
arquivo_saida = 'arquivo.txt'
arquivo_excel = 'Pasta1.xlsx'
contar_erros = 0

# Ler lista de emails
base = pd.read_excel(arquivo_excel)

# Abrir arquivo de saída
with open(arquivo_saida, 'w', encoding='utf-8') as f_saida:

    for contar_linha, email in enumerate(base["EMAIL"], start=1):
        print(contar_linha, email)

        try:
            # Separar domínio
            dominio = email.split('@')[1]

            # Verificar se domínio tem MX
            try:
                registros_mx = dns.resolver.resolve(dominio, 'MX')
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                f_saida.write(f"{email}, DOMÍNIO SEM MX\n")
                print(f"{email}, DOMÍNIO SEM MX")
                continue

            # Pegar o servidor MX principal
            servidor_mx = str(sorted(registros_mx, key=lambda r: r.preference)[0].exchange)

            # Conectar via SMTP
            try:
                servidor = smtplib.SMTP(timeout=10)
                servidor.connect(servidor_mx)
                servidor.helo()  # Identificação
                servidor.mail('teste@seudominio.com')  # Remetente fictício
                codigo, resposta = servidor.rcpt(email)
                servidor.quit()

                if codigo == 250:
                    f_saida.write(f"{email}, EMAIL EXISTE\n")
                    print(f"{email}, EMAIL EXISTE")
                else:
                    f_saida.write(f"{email}, NAO EXISTE/SMTP NAO CONFIRMOU\n")
                    print(f"{email}, NAO EXISTE/SMTP NAO CONFIRMOU")

            except (smtplib.SMTPServerDisconnected, smtplib.SMTPConnectError, socket.timeout):
                contar_erros += 1
                f_saida.write(f"{email}, ERRO AO CONECTAR SMTP\n")
                print(f"{email}, ERRO AO CONECTAR SMTP")
                print(f"JÁ DEU {contar_erros} ERROS")

        except Exception as e:
            contar_erros += 1
            f_saida.write(f"{email}, ERRO AO VALIDAR: {e}\n")
            print(f"{email}, ERRO AO VALIDAR: {e}")
            print(f"JÁ DEU {contar_erros} ERROS")
