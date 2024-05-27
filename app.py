import os




restaurantes = [
    {'nome':'Boi gordo', 'categoria':'Restaurante', 'ativo':False },
    {'nome':'Churras', 'categoria':'Marmitaria', 'ativo':False },
]



def chamar_nome_do_app():
    '''Essa função é responsavel por mostrar o nome do programa'''
    print('''
==================================================================================================================================================
=       ==============================================================================        ====================================================
=  ====  =============================================================================  ==========================================================
=  ====  =================  =========================================  ===============  ==========================================================
=  ===   ===   ====   ===    ===   ===  =  ==  =   ====   ===  = ===    ===   ========  ========  =  ==    ===  =   ====   ====   ====   ====   ==
=      ====  =  ==  =  ===  ===  =  ==  =  ==    =  ==  =  ==     ===  ===  =  =======      ====  =  ==  =  ==    =  ==  =  ==  =  ==  =  ==     =
=  ====  ==     ===  =====  ======  ==  =  ==  ==========  ==  =  ===  ===     =======  =========   ===  =  ==  =======     ===  =====  ====  =  =
=  ====  ==  =======  ====  ====    ==  =  ==  ========    ==  =  ===  ===  ==========  =========   ===    ===  =======  =======  =====  ===  =  =
=  ====  ==  =  ==  =  ===  ===  =  ==  =  ==  =======  =  ==  =  ===  ===  =  =======  ========  =  ==  =====  =======  =  ==  =  ==  =  ==  =  =
=  ====  ===   ====   ====   ===    ===    ==  ========    ==  =  ===   ===   ========        ==  =  ==  =====  ========   ====   ====   ====   ==
==================================================================================================================================================

    ''')
    
def finalizar():
    os.system('clear')
    chamar_nome_do_app()

def escolher_opcoes():
    '''Essa função é responsavel por exibir as opções disponiveis
    
    inputs:
    - Número da opção
    outputs:
    - executaer a opção escolhida
    '''
    
    print('1- cadastrar restaurante')
    print('2- listar restaurantes')
    print('3- ativar restaurante')
    print('4- sair do programa\n')

def cadastrar_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    inputs:
    - Nome do restaurante
    - Categoria
    outputs:
    - Adiciona um novo restaurante à lista de restaurantes
    '''
    finalizar();
    nome = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria: ')
    ativo = False 

    restaurantes.append({'nome': nome, 'categoria': categoria, 'ativo': ativo})
    main()

def listar_restaurantes():
    '''Essa função é responsavel por listar os restaurantes'''
    finalizar();
    
    print('restaurantes cadastrados\n')
    for restaurante in restaurantes:
        print(f'Nome: {restaurante["nome"]}, Categoria: {restaurante["categoria"]}, Ativo: {restaurante["ativo"]}\n')
    main()


def ativar_restaurante():
    '''Essa função é responsavel por ativar o restaurante
    
    inputs:
    - Nome do restaurante
    outputs:
    - Ativa o restaurante
    '''
    finalizar();
    for restaurante in restaurantes:
        print(f'o restaurante {restaurante["nome"]} está com o status ativo: {restaurante["ativo"]}\n')
    nome = input('Digite o nome do restaurante a ativar: ')

    for restaurante in restaurantes:
        if restaurante['nome'] == nome:
            if restaurante['ativo'] == False:
                restaurante['ativo'] = True
                print(f'Restaurante {nome} ativado com sucesso!')
                main()
            else: 
                restaurante['ativo'] = False
                print(f'O restaurante foi desativado\n')      
                main()
        
def finalizar_app():
    '''Essa função é responsavel por finalizar o app'''
    finalizar();
    print('finalizando app\n');

def nsei():

    try:
        opcao_digitada = int(input('Escolha uma opção: '))
        print('Você selecionou:', opcao_digitada, '\n')

        if opcao_digitada == 1:
            cadastrar_restaurante()
        elif opcao_digitada == 2:
            listar_restaurantes()
        elif opcao_digitada == 3:
            ativar_restaurante()
        elif opcao_digitada == 4:
            print('Você escolheu sair do programa\n')
        else:
            print('Opção inválida\n')
            

    except ValueError:
        print('Por favor, digite um número válido\n')
        

def main():
    '''Essa função é responsavel por executar todo o programa'''
    
    escolher_opcoes();
    nsei();

if __name__=="__main__":
    os.system('clear');
    chamar_nome_do_app();
    main()