# calculation BMI

height = float (input("Введите Ваш рост(см): ")) 
weight = float(input("Введите Ваш вес(кг): "))  

BMI = weight / ((height / 100) * (height / 100)) 
print("Ваш индек массы тела: %.2f" % BMI)

step = '20 ' + '='  * int(BMI - 20) + '|' + int(50 - BMI) * '=' + ' 50' 
print(step)

