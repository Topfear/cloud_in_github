"""
На прямой дощечке вбиты гвоздики. 
Любые два гвоздика можно соединить ниточкой. 
Требуется соединить некоторые пары гвоздиков ниточками так, 
чтобы к каждому гвоздику была привязана хотя бы одна ниточка, 
а суммарная длина всех ниточек была минимальна.

В первой строке входного файла INPUT.TXT записано число N 
- количество гвоздиков (2 ≤ N ≤ 100). В следующей строке 
записано N чисел - координаты всех гвоздиков 
(неотрицательные целые числа, не превосходящие 10000).


В выходной файл OUTPUT.TXT нужно вывести единственное число
 - минимальную суммарную длину всех ниточек.
"""

def main():

    with open('INPUT.TXT', 'r') as f:
        nails_count = int(f.readline())
        nails_position = list(map(lambda x: [int(x), False], f.readline().split()))

    fibers = 0

    nails_position.sort()

    # Соединим первого и следущего
    fibers += nails_position[1][0] - nails_position[0][0]
    nails_position[1][1] = True
    nails_position[0][1] = True

    # Соединим последнего и предыдущего, если необходимо
    if not nails_position[-1][1]:
        fibers += nails_position[-1][0] - nails_position[-2][0]
        nails_position[-1][1] = True
        nails_position[-2][1] = True


    for index, nail in enumerate(nails_position):
        if nail[1]:
            continue
        
        _prev, _next = nails_position[index-1], nails_position[index+1]
        to_prev, to_next = nail[0] - _prev[0], _next[0] - nail[0]

        if to_prev < to_next:
            fibers += to_prev
        else:
            fibers += to_next
            _next[1] = True

        nail[1] = True


    with open('OUTPUT.TXT', 'w') as f:
    	f.write(str(fibers))

if __name__ == '__main__':
    main()