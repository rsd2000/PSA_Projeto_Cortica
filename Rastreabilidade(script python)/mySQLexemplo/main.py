menu_options = {
    1: 'Listar Peças',
    2: 'Obter dados de uma peça',
    3: 'Inserir nova peça',
    4: 'Sair do programa'
}


def menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    return int(input('Escolha uma opção: '))


print('Bem-vindo ao gestor de peças de cortiça')

valid = True
while valid == True:
    option = menu()
    if option == 1:
        print(1)
    elif option == 2:
        print(2)
    elif option == 3:
        print(3)
    elif option == 4:
        print(4)
        valid = False

print("Adeus")
