# -----------------------------------------
# Calculadora Binária Gaudéria - tchê!
# Feita com amor, chimarrão e uns 8 bits
# -----------------------------------------

class ErroDaCalculadoraBinaria(Exception):
    pass

def cuida_entrada(bin_str: str) -> None:
    # Valida se a entrada é string, tem 8 bits e só tem 0 ou 1
    if not isinstance(bin_str, str):
        raise Exception("valor invalido")

    if len(bin_str) != 8:
        raise Exception("tamanho da entrada invalido")

    if any(c not in ('0', '1') for c in bin_str):
        raise Exception("valor invalido")

def cuida_operacao(op: str) -> None:
    # Valida se operação é permitida: +, - ou x
    if op not in ('+', '-', 'x'):
        raise Exception("valor invalido")

def vira_bits(bin_str: str) -> list[int]:
    # Converte string binária em lista de bits inteiros
    return [int(b) for b in bin_str]

def bits_pra_str(bits: list[int]) -> str:
    # Converte lista de bits em string binária
    return ''.join(str(b) for b in bits)

def soma_che(pila1: list[int], pila2: list[int]) -> list[int]:
    # Soma binária de 8 bits com detecção de overflow
    resultado = [0] * 8
    leva = 0

    for i in range(7, -1, -1):
        total = pila1[i] + pila2[i] + leva
        resultado[i] = total % 2
        leva = total // 2

    # Verifica overflow em complemento de dois
    if (pila1[0] == pila2[0]) and (resultado[0] != pila1[0]):
        raise Exception("overflow")

    return resultado

def faz_complemento(bits: list[int]) -> list[int]:
    # Faz complemento de dois (inverte bits e soma 1)
    invertido = [1 - bit for bit in bits]
    umzinho = [0] * 7 + [1]
    return soma_che(invertido, umzinho)

def subtrai_che(pila1: list[int], pila2: list[int]) -> list[int]:
    # Subtrai pila2 de pila1 usando complemento de dois
    complemento_b = faz_complemento(pila2)
    return soma_che(pila1, complemento_b)

def multiplica_pila(p1: list[int], p2: list[int]) -> list[int]:
    # Multiplica dois números binários de 8 bits sem converter para inteiro,
    # usando soma repetida e controle de sinal e overflow

    # Pega o sinal dos operandos (bit mais significativo)
    sinal1 = p1[0]
    sinal2 = p2[0]

    # Função que retorna o valor absoluto em bits
    def valor_abs(bits):
        if bits[0] == 1:
            return faz_complemento(bits)
        return bits.copy()

    abs1 = valor_abs(p1)
    abs2 = valor_abs(p2)

    resultado = [0] * 8  # Inicializa resultado com zero

    # Faz a multiplicação por soma repetida simulando deslocamento
    for i in range(7, -1, -1):
        if abs2[i] == 1:
            # Desloca abs1 para a esquerda conforme o bit de abs2
            desloc = 7 - i
            temp = abs1.copy()

            # Simula deslocamento à esquerda: remove bits do começo e adiciona zeros no fim
            for _ in range(desloc):
                temp.pop(0)
                temp.append(0)

            # Soma o valor temporário ao resultado
            resultado = soma_che(resultado, temp)

    # Ajusta o sinal do resultado conforme os sinais dos operandos
    if sinal1 != sinal2:
        resultado = faz_complemento(resultado)

    return resultado

def calcular(n1: str, n2: str, operacao: str) -> str:
    """
    Função principal da calculadora gaudéria:
    recebe dois números binários de 8 bits e a operação (+, -, x),
    retorna o resultado também em binário de 8 bits.
    """
    cuida_entrada(n1)
    cuida_entrada(n2)
    cuida_operacao(operacao)

    a = vira_bits(n1)
    b = vira_bits(n2)

    if operacao == '+':
        resultado = soma_che(a, b)
    elif operacao == '-':
        resultado = subtrai_che(a, b)
    else:
        resultado = multiplica_pila(a, b)

    return bits_pra_str(resultado)


# Exemplo de uso gauchesco
if __name__ == "__main__":
    print("=== Calculadora Binária Gaudéria (8 bits) ===")
    print("Digite 'sair' pra dar no pé, tchê.\n")

    while True:
        try:
            n1 = input("Manda o primeiro número binário (8 bits), vivente: ").strip()
            if n1.lower() == 'sair':
                break

            n2 = input("Agora o segundo, mas cuida: tem que ser 8 bits! ").strip()
            if n2.lower() == 'sair':
                break

            op = input("Qual operação quer fazer? (+, -, x): ").strip()
            if op.lower() == 'sair':
                break

            res = calcular(n1, n2, op)
            print(f"Olha aí o resultado, tchê: {res}\n")

        except Exception as e:
            print(f"Bah, deu ruim: {e}\n")
