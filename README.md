# 🌐 Conversor de IP em binário

Aplicação simples em **Python** que converte um endereço **IPv4** no
formato decimal (ex: `127.0.0.1`) para sua representação **binária**.

Este projeto foi desenvolvido com fins de **estudo e prática de
programação em Python**, trabalhando com manipulação de strings, listas,
conversões numéricas e lógica de programação.

------------------------------------------------------------------------

# 📌 Funcionalidades

-   Recebe um endereço **IPv4** digitado pelo usuário
-   Separa os **octetos** do endereço IP
-   Converte cada octeto para **binário**
-   Garante que cada octeto possua **8 bits**
-   Exibe o endereço IP convertido

### Exemplo

Entrada:

    127.0.0.1

Saída:

    01111111.00000000.00000000.00000001

------------------------------------------------------------------------

# 🧠 Como funciona

Um endereço **IPv4** possui **4 octetos**, separados por ponto:

    192.168.1.10

Cada octeto varia entre:

    0 até 255

O programa executa os seguintes passos:

1.  Recebe o IP digitado pelo usuário
2.  Divide o endereço utilizando `split('.')`
3.  Converte cada octeto para **inteiro**
4.  Converte o número para **binário**
5.  Completa os bits com zeros à esquerda até **8 bits**
6.  Junta os octetos novamente com `"."`

------------------------------------------------------------------------

# 🛠 Tecnologias utilizadas

-   Python 3
-   Manipulação de strings
-   Estruturas de repetição (`for`)
-   Conversão de números (`bin()`)
-   Listas

------------------------------------------------------------------------

# 📂 Estrutura do Projeto

    ip-to-binary-converter
    │
    ├── main.py
    └── README.md

------------------------------------------------------------------------

# ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório

``` bash
git clone https://github.com/seu-usuario/ip-to-binary-converter.git
```

### 2️⃣ Acessar a pasta

``` bash
cd ip-to-binary-converter
```

### 3️⃣ Executar o programa

``` bash
python main.py
```

------------------------------------------------------------------------

# 💻 Exemplo de código

``` python
ip = input("Digite um endereço IP: ")

octetos = ip.split(".")

resultado = []

for o in octetos:
    numero = int(o)
    binario = bin(numero)[2:].zfill(8)
    resultado.append(binario)

ip_binario = ".".join(resultado)

print("IP em binário:", ip_binario)
```

------------------------------------------------------------------------

# 🚀 Possíveis melhorias futuras

-   Validação de endereço IP
-   Tratamento de erros (`try/except`)
-   Conversão **binário → IP**
-   Interface gráfica com **Tkinter**
-   Interface web com **Flask**

------------------------------------------------------------------------

# 👨‍💻 Autor

**Héber R. D'Elia Neto**

Projeto criado para fins de **aprendizado em Python e lógica de
programação**.

⭐ Se este projeto foi útil para você, considere dar uma estrela no
repositório!
