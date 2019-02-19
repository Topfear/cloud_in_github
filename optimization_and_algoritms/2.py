# В единственной строке входного файла INPUT.TXT записано единственное целое число N, не превышающее по абсолютной величине 104.
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел, расположенных между 1 и N включительно.


def main():
	with open('INPUT.TXT', 'r') as f:
		v = int(f.readline())

	a = v
	b = 2

	if v > 0:
		a = 1
		b = v + 1

	with open('OUTPUT.TXT', 'w') as f:
		f.write(str(sum([x for x in range(a, b)])))

if __name__ == '__main__':
	main()