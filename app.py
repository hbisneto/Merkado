import codecs
from datetime import datetime
# Importa o arquivo bd dentro do mesmo diretório da aplicação
import bd

AGORA = datetime.now()
DATA_ATUAL = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
HORA_ATUAL = AGORA.strftime("%H:%M:%S")
strike = "-" * 80

def exibir_menu():
    print("\nItens disponíveis para compra:")
    for opcao, (item, preco) in bd.mercado.items():
        print(f"{opcao}. {item}: R${preco:.2f}")

def calcular_total(itens_comprados):
    total = 0
    for opcao in itens_comprados:
        if opcao in bd.mercado:
            total += bd.mercado[opcao][1]
        else:
            print(f"Opção '{opcao}' não encontrada.")
    return total

def nota_fiscal():
    total_compra = calcular_total(itens_comprados)
    dado = f"""Nome do mercado
Rua Da Qualidade, 12345
CEP: 12.345-678 - JD. Da Qualidade - Cidade - UF
CNPJ: 01.234.567/890-09  IE: 123.456.789.098
{DATA_ATUAL}   {HORA_ATUAL}       Caixa: 01       C00: 123456
                    COMPROVANTE NÃO FISCAL     
                01: NFC-e/CF-e       (0123)
    Loja: 23             PDV: 012            OP: 12345  
{strike}  
                    NOME DO MERCADO S.A
                CNPJ: 01.234.567/890-09  IE: 123.456.789.098
                    Rua Da Qualidade, 12345
                JD. Da Qualidade - Cidade, CEP: 12.345-678
{strike}
                    EXTRATO No. 123456
                CUPOM FISCAL ELETRÔNICO SAT
{strike}
DESC|VL UN R$
{strike}
"""
    
    dado_total = f"""{strike}
TOTAL: {total_compra:.2f}
{strike}
                    OBSERVAÇÕES DO CONTRIBUINTE
                Valor aproximado dos tributos do item
            Valor aproximado dos tributos deste cupom 
            (conforme lei federal 12.741/2012) (R$ 0,00)
{strike}
"""
    with codecs.open(f'NotaFiscal.txt', "w", encoding='utf-8') as custom_file:
        custom_file.write(dado)
    
    for i in itens_comprados:
        with codecs.open(f'NotaFiscal.txt', "a", encoding='utf-8') as custom_file:
            custom_file.write(f'{bd.mercado[i][0]}: R$ {bd.mercado[i][1]}\n')
    
    with codecs.open(f'NotaFiscal.txt', "a", encoding='utf-8') as custom_file:
        custom_file.write(dado_total)

itens_comprados = []
while True:
    exibir_menu()
    escolha = int(input("\nDigite o número do item que deseja comprar (ou '0' para finalizar): "))
    if escolha == 0:
        nota_fiscal()
        break
    itens_comprados.append(escolha)

total_compra = calcular_total(itens_comprados)
print("="*80)
print("TOTAL DA COMPRA")
print("="*80)
print(f">> Total da compra: R${total_compra:.2f}")
print("="*80)
