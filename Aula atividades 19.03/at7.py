n1 = int(input("Informe um número de 0 a 99: "))

if n1 >= 0 and n1 <= 99:
    dez = n1 // 10
    unid = n1 - dez * 10
    print("A dezena é: ", dez)
    print("A unidade é: ", unid)