# 💳 Sistema Bancário em Python

Este projeto foi desenvolvido como parte de um desafio proposto pela [Digital Innovation One (DIO)](https://www.dio.me/). A proposta é criar um sistema bancário simples com operações de **depósito**, **saque** e **extrato**, utilizando a linguagem Python.

## 📌 Funcionalidades

- **Depósito**
  - Permite depósitos de valores positivos.
  - Cada operação é registrada para consulta no extrato.

- **Saque**
  - Limite de **3 saques diários**.
  - Valor máximo por saque: **R$ 500,00**.
  - Saques só são permitidos se houver saldo suficiente.

- **Extrato**
  - Lista todas as movimentações realizadas (depósitos e saques).
  - Exibe o saldo atual.
  - Caso não haja movimentações, exibe mensagem apropriada.
  - Valores formatados no padrão: `R$ xxx.xx`.

## 🛠️ Tecnologias Utilizadas

- Python 3.13.5

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/RuanRodriguesEsteves/dio-sistema-bancario-python.git
