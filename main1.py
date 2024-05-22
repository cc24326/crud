import pyodbc

def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('|                                                             |')
    print('| Versão 1.0 de 12/abril/2024                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom==agd[meio][0]:
            return [True,meio]
        elif nom<agd[meio][0]:
            final=meio-1
        else: # nom>agd[meio][0]
            inicio=meio+1
            
    return [False,inicio]
    
def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')
    return True
def procurar(agd):
    while True:
        nome=input('Digite um Nome já registrado: ')
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        if achou:
            print('Aniversario:',agd[posicao][1])
            print('Endereco...:',agd[posicao][2])
            print('Telefone...:',agd[posicao][3])
            print('Celular....:',agd[posicao][4])
            print('e-mail.....:',agd[posicao][5])
            break
        if not achou:
            print("Digite um nome que já foi registrado!")
def atualizar (agd):
    opcao=0
    while opcao!= 6:
        nome=input("Qual contato deseja atualizar: ")
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        if achou:
            while True:
                try: 
                    print('1) Aniversario:',agd[posicao][1])
                    print('2) Endereco...:',agd[posicao][2])
                    print('3) Telefone...:',agd[posicao][3])
                    print('4) Celular....:',agd[posicao][4])
                    print('5) e-mail.....:',agd[posicao][5])
                    print("6) Finalizar atualizações do contato!")
                    opcao = int(input("Digite o valor do elemento a ser alterado: "))
                    if opcao <= 0 or opcao >= 7:
                        print("Digite um valor valido!")
                    if opcao == 6:
                        break
                except ValueError:
                    print("Digite um numero inteiro maior que zero e menor ou igual à seis! ")
                if opcao == 1:
                    agd[posicao][1]=input('Aniversário: ')
                elif opcao == 2:
                    agd[posicao][2]=input('Endereco...:')
                elif opcao == 3:
                    agd[posicao][3]=input('Telefone...: ')
                elif opcao == 4:
                    agd[posicao][4]=input('Celular....:')
                elif opcao == 5:
                    agd[posicao][5]=input('e-mail.....: ')
        if opcao == 6:            
            break
        if not achou:   
            print("Digite um nome já registrado!")
            break
def listar (agd):
    posicao=0
    while posicao<len(agd):
        print ("Nome: ",agd[posicao][0])
        print ("aniversário: ",agd[posicao][1])
        print ("endereço: ",agd[posicao][2])
        print ("telefone: ",agd[posicao][3])
        print ("celular: ",agd[posicao][4])
        print ("e-mail: ",agd[posicao][5])
        print()
        posicao+=1
    if len(agd)==0:
        print("Não há dados cadastrados!")
        
    input("Aperte enter para continuar")
def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA! Programa feito por: Leonardo Tamarozzi/Ra: 24326, Vinicius Pavanni/Ra:24337, João Guilherme Zanirato/Ra: 24321')












