def f_sublinhado(p):
    s = ""
    for i in range(len(p)):
        s += "_"
    return s

def f_imprimirSublinhado(s):
    for i in range(len(s)):
        print(s[i],end=" ")
    print()
    
def main():
    continuar = True
    palavra = input().upper()
    jogadas = 0
    erros = 0
    letras_erradas = ""
    segredo = ""
    for i in range(len(palavra)):
        segredo += "_"
    sublinhado = f_sublinhado(palavra)
    f_imprimirSublinhado(sublinhado)
    while (continuar == True and erros<6):
        jogadas += 1
        letra = input().upper()
        errou = True
        s2 = ""
        for i in range(len(palavra)):
            if (palavra[i] == letra):
                s2 += letra
                errou = False
            elif (segredo[i] == "_"):
                s2 += "_"
            else:
                s2 += segredo[i]
        segredo = s2
        if (errou==True):
            erros += 1
            letras_erradas += letra
        f_imprimirSublinhado(s2)
        print(letras_erradas)
        print()
        if (s2 == palavra):
            continuar = False
            print(f'Parabéns, você ganhou com {jogadas} jogadas')
        if (erros==6):
            print(f'Que pena, você não acertou a palavra {palavra}')

if __name__ == "__main__":
    main()