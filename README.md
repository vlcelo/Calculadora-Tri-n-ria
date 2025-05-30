# Calculadora "Tri"nária
Calculadora Binária Gaudéria (8 bits): Projeto de Arquitetura de Computadores com alma gaudéria  Este repositório contém a Calculadora Binária Gaudéria, uma calculadora simples para operações aritméticas em números binários de 8 bits (1 byte), feita em Python com sotaque e charme gaúcho!

## 🧠 Sobre

A **Calculadora Binária Gaudéria** realiza operações básicas entre números binários de 8 bits (1 byte), incluindo:

- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`x`)

Os números são representados em **complemento de dois**, como é padrão em sistemas digitais. Toda a lógica de cálculo é feita **manualmente, bit a bit**, sem conversões para decimal.

---

## ⚙️ Requisitos

- Python 3.8+
- Nenhuma dependência externa

---

## 📥 Como usar

A função principal para uso em outros scripts é:

calcular(n1: str, n2: str, operacao: str) -> str
Parâmetros:
n1: string binária de 8 bits (ex: "00000001")

n2: string binária de 8 bits (ex: "00000010")

operacao: string com um dos valores: "+", "-" ou "x"

Retorno:
Uma string binária de 8 bits com o resultado da operação

Exceções:
"overflow": quando o valor excede o intervalo permitido (-128 a 127)

"valor invalido": entrada contém caracteres inválidos ou operação desconhecida

"tamanho da entrada invalido": entrada com número diferente de 8 bits
