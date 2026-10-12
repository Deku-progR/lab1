import os
import time


WHITE = '\x1B[47m'
BLUE = '\x1B[44m'
RESET = '\x1B[0m'
START = '\x1B[1G'
ERASE = '\x1B[2K'
RED = '\u001b[41m'

def draw_flag():
    pixel = '   '
    len = 10
    height = 6
    width = len // 5

    for i in range(height):
        if i < height // 3:
            print(f'{WHITE}{pixel * width}{BLUE}{pixel * width}{WHITE}{pixel * (len - width*2)}' + RESET)
        elif i < height * 2 // 3:
            print(f'{BLUE}{pixel * len}' + RESET)
        else:
            print(f'{WHITE}{pixel * width}{BLUE}{pixel * width}{WHITE}{pixel * (len - width*2)}' + RESET)


def draw_pattern():
    symbol = '*'
    gap = ' '
    diametr = 20
    radius = diametr // 2
    for i in range(radius + 1):
        if i <= radius // 2:
            print(gap * (radius - 2*i) + symbol * 4 * i + gap * 2 * (radius - 2 * i ) + symbol * 4 * i)
        elif i == radius // 2:
            print(symbol * 2 * diametr)
        else:
            print(gap * (2*i - radius) + symbol * (2 * diametr - 4 * i) + gap * 2 * (2*i - radius)  + symbol * (2 * diametr - 4 * i))


def move():
    vect = '-'
    for i in range(4):
        print(f'GO{vect * 2 * i}>>>{START}')
        time.sleep(0.5)
        os.system('cls')
    print('BOOM!!!')


def make_diagram():
    file = open('sequence.txt','r')
    '''
    Числа от 5 до 10 и числа от -5 до -10, остальные отбросить
    '''
    nice = []
    odd = []
    for i in file:
        if 5 < abs(float(i)) < 10: nice.append(float(i))
        else: odd.append(float(i))
    
    file.close()
    print(f'Nice numbers: [{RED}{' '*(len(nice)//5)}{RESET} {round(100*len(nice)/(len(nice)+len(odd)),2)}%]')
    print(f'Odd numbers: [{BLUE}{' '*(len(odd)//5)}{RESET} {round(100*len(odd)/(len(nice)+len(odd)),2)}%]')
#move()

make_diagram()

#draw_pattern()
#draw_flag()
