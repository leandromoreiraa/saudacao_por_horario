hora = input("Que Horas São?: ")

if int(hora) == 0 or int(hora) <= 11:
    print('Bom Dia')
elif int(hora) == 12 or int(hora) <= 17:
    print('Boa Tarde')
else:
    print('Boa Noite')