import mysql.connector
from mysql.connector import errorcode
from datetime import datetime, date

# Opções do menu
menu_options = {
    1: 'Listar Peças',
    2: 'Obter dados de uma peça',
    3: 'Inserir nova peça',
    4: 'Sair do programa'
}


# Mostrar menu
def menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    print('')
    return int(input('Escolha uma opção: '))


try:
    # Faz ligação à basedados
    cnx = mysql.connector.connect(user='root',
                              host='localhost',
                              database='cortica')
    mycursor = cnx.cursor()
    print('Ligação MySql OK')
    print('Bem-vindo ao gestor de peças de cortiça')

    valid = True
    # Enquanto a variável valid for True, ou seja, enquanto o utlizador não escolher a opção 4
    while valid == True:
        option = menu()
        if option == 1:
            # Listar todas as peças
            mycursor.execute("SELECT * FROM peca")

            myresult = mycursor.fetchall()

            for x in myresult:
                print("ID peça: ", x[0])
                print("Nr. Defeitos: ", x[1])
                print("Data de Inspeção", x[2])
                print('')

        elif option == 2:
            # Pesquisar peça
            id_peca = int(input("Insira o id da peça: "))
            mycursor.execute("SELECT * FROM peca WHERE id=" + str(id_peca))
            myresult = mycursor.fetchall()

            print("ID peça: ", myresult[0][0])
            print("Nr. Defeitos: ", myresult[0][1])
            print("Data de Inspeção", myresult[0][2])
            print('')

        elif option == 3:
            # Inserir nova peça
            n_defeitos = int(input("Insira o nr de defeitos da peça: "))
            #inspection_date = datetime.now()
            dia = int(input("Insira o dia da inspeção: "))
            mes = int(input("Insira o mês da inspeção: "))
            ano = int(input("Insira o ano da inspeção: "))
            hora = int(input("Insira a hora da inspeção: "))
            minutos = int(input("Insira os minutos da inspeção: "))
            segundos = 0
            # Criar o objeto datetime
            date = datetime(year=ano, month=mes, day=dia, hour=hora, minute=minutos, second=segundos)
            # Formata o objeto datetime para o formato string
            formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
            print(formatted_date)

            mycursor.execute('INSERT INTO peca (ndefeitos, inspection) VALUES (%s, %s)', (n_defeitos, formatted_date))
            cnx.commit()
            print('Registo inserido...')

        elif option == 4:
            # Sair do programa
            valid = False

    print('Adeus')

    print('Fim leitura base de dados...')


except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()