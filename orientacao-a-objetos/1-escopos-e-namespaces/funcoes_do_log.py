# Este arquivo consiste no módulo "funcoes_do_log"

nome_de_usuario = 'Dani'

def imprimir_no_log(texto, nivel='info'):
    if nivel == 'info':
        print(f'[INFO] {texto}')
    elif nivel == 'alerta':
        print(f'[ALERTA] {texto}')
    elif nivel == 'erro':
        print(f'[Erro] {texto}')
    else:
        print(f'[ERRO] nível "{nível}" não é válido!')