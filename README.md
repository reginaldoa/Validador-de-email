# Validador de E-mails com Verificação SMTP

Este projeto consiste em um script Python que valida a existência de e-mails presentes em uma planilha Excel, verificando se o e-mail é válido através de SMTP. O script também lida com erros e salva os resultados de validação em um arquivo de texto.

## Descrição

O script lê uma lista de e-mails de um arquivo Excel e tenta verificar a validade de cada um, realizando as seguintes operações:

- **Leitura do arquivo Excel**: O script carrega os e-mails de uma coluna chamada "EMAIL".
- **Validação de e-mail**: Para cada e-mail, o script tenta validar o endereço usando a função `validate_email` com verificação SMTP.
- **Erro e controle**: Se o e-mail não puder ser verificado ou um erro ocorrer, ele registra a falha no arquivo de resultados e continua com o próximo e-mail.
- **Armazenamento dos resultados**: O script grava as informações sobre a validade de cada e-mail em um arquivo `.txt` chamado `arquivo.txt`.

## Como Funciona

1. O script começa lendo os e-mails da coluna `EMAIL` de uma planilha chamada `Pasta1.xlsx`.
2. Para cada e-mail, ele tenta verificar a validade usando o módulo `validate_email` com verificação SMTP.
3. Os resultados de cada verificação são impressos na tela e também gravados em um arquivo de texto.
4. Caso ocorra um erro (por exemplo, se o SMTP não puder ser verificado), o erro é registrado e o script tenta a verificação do próximo e-mail.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `DNS` (para realizar a verificação DNS)
- `validate_email` (para validar os e-mails)
- `pandas` (para ler o arquivo Excel)

Você pode instalar as dependências com o seguinte comando:

```bash
pip install dns validate_email pandas


Exemplo de saída:
email1@example.com, EMAIL EXISTE
email2@example.com, NAO
email3@example.com, NAO EXISTE/SMTP NAO PODE SER VERIFICADO
