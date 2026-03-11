# Aplicação em Python para cálculo de endereços IP's em sistema binário

ip = input("Digite um endereço IP: ")

octetos = ip.split(".")

resultado = []

for o in octetos:
    numero = int(o)
    binario = bin(numero)[2:].zfill(8)
    resultado.append(binario)

ip_binario = ".".join(resultado)

print("IP em binário:", ip_binario)