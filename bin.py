def bin_to_str(binario):
    binario = str(binario)
    caractere = ''
    string = ''
    tamanho = len(binario)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tamanho:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''  # 0x101100110
        k += 1
    return string


def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

def codificador():
    text = str(input("Entre com um texto: "))
    binary = str_to_bin(text)
    print()
    print(binary)

def decodificador():
    binary = str(input("Entre com um binario: "))
    text = bin_to_str(binary)
    print()
    print(text)

def main():
    print("Codificador/Decodificador de binarios!")
    print("""
[ 1 ] = Texto -> Binário
[ 2 ] = Binário -> Texto
    """)
    aux = input("Sua escolha: ")

    if aux == "1":
        print("Aguarde...")
        print()
        codificador()

    elif aux == "2":
        print("Aguarde...")
        print()
        decodificador()

    else:
        print("Escolha Inexistente! Voltando ao menu")
        main()

main()
