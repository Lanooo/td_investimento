while True:
    print ("--------------------------------")
    print ("  Seja bem-vindo(a) ao My Bank  ")
    print ("   SIMULADOR DE INVESTIMENTO    ")
    print ("--------------------------------") 

    print ("Títulos disponíveis:")
    print ("1 - Tesouro Prefixado 2024")
    print ("2 - Tesouro Prefixado 2026")

    titulo = str(input("Qual título você gostaria de fazer uma simulação? (1 ou 2): "))

    vi = int(input("Qual valor gostaria de investir agora? "))
    vm = int(input("Quanto gostaria de investir mensalmente se quiser? "))

    if titulo == '1':
        vti = (vm * 32) + vi

        vb = vti + (vti * 0.1656236)
        ir = vb * 0.023415
        v_ir = vb - ir
        b3 = vb * 0.003
        vl = v_ir - b3
        a = 32

    else:
        vti = (vm * 50) + vi

        vb = vti + (vti * 0.2799)
        ir = vb * 0.03402
        v_ir = vb - ir
        b3 = vb * 0.0045
        vl = v_ir - b3
        a = 50

    print ("--------------------------")
    print ("  RESULTADO DA SIMULAÇÃO  ")
    print ("--------------------------")
    print (f"Valor incial: {vi}R$")
    print (f"Aportes de: {vm}R$ por {a} meses")
    print (f"Valor total investido: {vti}R$")
    print ("---------------------------")
    print (f"Valor bruto: {vb}R$")
    print (f"I.R.: {ir}")
    print (f"B3: {b3}")
    print (f"Valor líquido: {vl}R$")
    print ("---------------------------")

    opcao = str(input("Deseja realizar outra simulação? (s ou n)"))

    if opcao == 'n':
        break

print ("Programa encerrado")

