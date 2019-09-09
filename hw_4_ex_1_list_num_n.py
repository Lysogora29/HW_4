try:
    num_n = [int(i) for i in input('Enter number: ')] 
    suma = sum(num_n)
    suma = str(suma)
    suma_1 = list(suma)
    suma_up = [int(i) for i in suma_1]
    sm = sum(suma_up)

    print('Sum of number =', sm)
except:
    print('Enter only numbers')





