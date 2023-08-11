opcao = ["Deposito", "Saque", "Extrato"]
valorAtual = 0
i = 1
a = 1
while i == 1:
    print(
        """
        Selecione a opção desejada    [0] Deposito ;  [1] Saque  ;  [2] Extrato """
   )
    percorrer = int(input())
    if percorrer > len(opcao):
        print("Erro")
    else:
        while a >= 1:
            if percorrer == 0:
                print("Digite o valor deseja depositar: ")
                valorDeposito = int(input())
                valorAtual = valorAtual + valorDeposito
                print("Tem disponíel agora: R$ " , valorAtual)
                break
            if percorrer == 1:
                print("Digite o valor deseja sacar: ")
                valorSaque = int(input())
                if valorSaque <= valorAtual:
                    valorAtual -= valorSaque
                    print("Saque realizado com sucesso!")
                else:
                    print("Erro, valor não disponível. Por favor consulte seu saldo!")
                break                    
            if percorrer == 2:
                print("Seu saldo é de: R$ ", valorAtual)
                break                
            else:
                print("Opção não disponível. Por favor recomeçe a operação!")
                break  
        a += 1



# print (valorAtual)


# print ("Você selecionou: 1" + opcao[percorrer])


# percorrer=[input()]
# print(percorrer)


""""
valor = 0 #poucas variáveis

Qtsaque = 3
saque = 0
# i = 1 
# while i !=  0       
#i++


# for   i = 3 
if opcao == 1:
    print("Digite o valor deseja depositar")
    valor = int(input())
    if valor > 0:
        print("Deposito realizado com sucesso valor de %d" % valor)
    else:
        print("Digite um valor, antes de fazer deposito")
elif opcao > 3:
    print("numero invalido")

print(valor)

if opcao == 2:
    
    while Qtsaque > 0:
        print("Quanto deseja sacar ")
        saque = int(input())
        if saque <= valor:
            valor -= saque
            print("Você realizou saque de %d" % saque and " e possui %d saques restantes." % Qtsaque)
        else:
            print("Saldo insuficiente")
            Qtsaque+=1
        Qtsaque-=1
"""
