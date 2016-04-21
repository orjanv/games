from random import *

name = input('Hva heter du? ')
print("Hei %s,\nJeg tenker på et tall mellom 0 og 100.\nKlarer du å gjette det på bare seks forsøk?" % name)
guess = input('Hva gjetter du?: ')
min = 0
max = 100
attempts = 1
number = randint(min,max)

while int(guess) != number or attempts < 7:
    if attempts == 6:
        print("Du har prøvd for mange ganger, tallet var: %s" % number)
        break
    if attempts == 5:
        print('Bare ett forsøk igjen nå..')
    if int(guess) < number:
        guess = input('For lavt, prøv igjen: ')
    if int(guess) > number:
        guess = input('For høyt, prøv igjen: ')
    if int(guess) > max or int(guess) < min:
        guess = input('Tallet skal være mellom %s and %s, prøv igjen: ' % min, max)
    if int(guess) == number:
        print('\nRiktig, bra jobbet!')
        break
    attempts += 1

