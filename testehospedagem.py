import os

QuartosDisp = 50

while True:
    os.system ('cls')
    print("* "*20)
    print("Estrela do Mar - Hotel")
    print("* "*20)
    print("\n-----Menu-----\n")
    print("Op 1 - Escolher quartos")
    print("Op 2 - Sair do sistema")
    
    try:
        opcao = int(input("\nInforme sua opção: "))
    except ValueError:
        print("\nERRO! Insira um número!")
        os.system('pause')
        continue
    if opcao < 1 or opcao > 2:
        print("\nERRO! Valor inválido!")
        os.system('pause')
        continue

    if opcao == 1:
        print("\n*** Escolher quartos ***")
        try:
            Dia = int(input("\nInsira a quantidade de dias: "))
        except ValueError:
            print("\nERRO! Insira um número!")
            os.system('pause')
            continue

        if Dia > 30:
            print("\nERRO! Número de dias excedido!.")
            os.system('pause')
            continue

        if Dia < 1:
            print("\nERRO! Valor inválido!")
            os.system('pause')
            continue

        try:
            SuiteIndv = int(input("\nQuantidade de Suites Individuais (1 cama de solteiro): "))
            if SuiteIndv > QuartosDisp:
                print("\nERRO! Número desejado maior do que a quantidade de quartos disponíveis!")
                os.system('pause')
                continue

            elif SuiteIndv < 0:
                print("\nERRO! Valor inválido")
                os.system('pause')
                continue
            else:
                QuartosDisp -= SuiteIndv

            SuiteDuplo = int(input("\nQuantidade de Suites Duplas (1 cama de casal): "))
            if SuiteDuplo > QuartosDisp:
                print("\nERRO! Número desejado maior do que a quantidade de quartos disponíveis!")
            
            elif SuiteDuplo < 0:
                print("\nERRO! Valor inválido")
                os.system('pause')
                continue

            else:
                QuartosDisp -= SuiteDuplo
                
            QuartoFamiliar = int(input("\nQuantidade de Quartos Familiares (6 camas de solteiro): "))
            if QuartoFamiliar > QuartosDisp:
                print("\nERRO! Número desejado maior do que a quantidade de quartos disponíveis!")
                
            elif QuartoFamiliar < 0:
                print("\nERRO! Valor inválido")
                os.system('pause')
                continue
            else:
                QuartosDisp -= QuartoFamiliar
                

        except ValueError:
            print("\nERRO! Insira um número!")
            os.system('pause')
            continue

        if SuiteIndv + SuiteDuplo + QuartoFamiliar == 0:
            print("Inválido.")
            os.system('pause')
            continue
        
        if SuiteIndv + SuiteDuplo + QuartoFamiliar > 10:
            print("\nERRO! Você não pode alugar mais de 10 quartos!")
            os.system('pause')
            continue

        elif SuiteIndv + SuiteDuplo + QuartoFamiliar == 0:
            print("\nERRO! Valor inválido!")
            os.system('pause')
            continue

        vl = SuiteIndv * Dia * 180 + SuiteDuplo * Dia * 300 +  QuartoFamiliar * Dia *  500
        os.system('cls')

        print("\nVocê escolheu:")
        if SuiteIndv > 0:
            print(f"\n{SuiteIndv} Suites Individuais")

        if SuiteDuplo > 0:
            print(f"{SuiteDuplo} Suites Duplas")

        if QuartoFamiliar > 0:
            print(f"{QuartoFamiliar} Quartos Familiares")
            
        print(f"\nValor total: {vl:.2f} reais.")
        #print(f"{QuartosDisp}")
        print(f"Dias: {Dia}")        
        os.system('pause')

    elif opcao == 2:
        print("\nVocê escolheu sair.")
        break
    os.system('pause')