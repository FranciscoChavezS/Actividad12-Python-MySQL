import mysql.connector

bd = mysql.connector.connect(user='javier',password='gringo123',database='nopalito')

cursor = bd.cursor()

while True:
    print('1) Agregar usuario')
    print('2) Mostrar Usuarios')
    print('0) Salir')
    op = input()

    if op == '1':
        nombre = input('nombre: ')
        email = input('correo: ')
        sexo = input('sexo: ')
        edad = int(input('edad: '))
        direccion = input('direccion: ')

        consulta = "INSERT INTO usuario (nombre, email, sexo, edad, direccion)" \
                    "VALUES (%s , %s, %s, %s, %s)"
        cursor.execute(consulta, (nombre, email, sexo, edad, direccion))
        bd.commit()
        if cursor.rowcount:
            print('Se agregó usuario')
        else:
            print('Error')

    elif op == '2':
        consulta = "SELECT * FROM usuario"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print('id: ', row[0])
            print('nombre: ', row[1])
            print('correo: ', row[2])
            print('sexo: ',row[3])
            print('edad: ', row[4])
            print('dirección: ',row[5])
    elif op == '0':
        break
