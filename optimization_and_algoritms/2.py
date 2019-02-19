# В единственной строке входного файла INPUT.TXT записано единственное целое число N, не превышающее по абсолютной величине 104.
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел, расположенных между 1 и N включительно.


def main():
	input_value = None
	with open('INPUT.TXT', 'r') as f:
		input_value = int(f.readline())

	with open('OUTPUT.TXT', 'w') as f:
		f.write(str(sum([x for x in range(1, input_value + 1)])))


if __name__ == '__main__':
	main()