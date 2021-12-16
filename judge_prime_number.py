import math

n = 10511051

stop = math.ceil(n**0.5)

if n == 2 or n == 3 or n == 5:
    print(f'n is prime number.')
elif n % 2 == 0:
    print(f'n is not prime number.'+'\n'+\
              f'Devided by {2}.')
elif n % 3 == 0:
    print(f'n is not prime number.'+'\n'+\
              f'Devided by {3}.')
else:
    i = 1
    while True:
        if n % (6*i-1) == 0:
            print(f'n is not prime number.'+'\n'+\
                  f'Devided by {6*i-1}.')
            break
        elif n % (6*i+1) == 0:
            print(f'n is not prime number.'+'\n'+\
                  f'Devided by {6*i+1}.')
            break
        elif 6*i+1 > stop:
            print(f'n is prime number.')
            break
        i += 1
