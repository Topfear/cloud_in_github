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
        nails_position = list(map(lambda x: int(x), f.readline().split()))

    fibers = 0

    nails_position.sort()

    d = list(0 for x in range(nails_count))
    d[0] = 0
    d[1] = nails_position[1] - nails_position[0]
    for i in range(2, nails_count - 2):
        d[i] = min(nails_position[i-1], nails_position[i+1])

    print(d)
    print(nails_position)


    with open('OUTPUT.TXT', 'w') as f:
    	f.write(str(d[-1]))

if __name__ == '__main__':
    main()