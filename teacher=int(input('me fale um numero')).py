teacher=int(input('me fale um numero'))
studant=int(input('me fale outro numero'))
school=(input('me fale uma operação matematica(+ - * /)'))
if school == '+':
    print(teacher+studant)
elif school == '-':
    print(teacher-studant)
elif school == '*':
    print(teacher*studant)
elif school == '/':
    print(teacher/studant) 
else :
    print('essa tua operação, newtom ainda não descobriu')