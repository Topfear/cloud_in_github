# В первой строке входного файла INPUT.TXT записано количество платформ n (1 ≤ n ≤ 30000). Вторая строка содержит n натуральных чисел, не превосходящих 30000 – высоты, на которых располагаются платформы.
# В выходной файл OUTPUT.TXT запишите единственное число – минимальное количество энергии, которую должен потратить игрок на преодоление платформ (конечно же в предположении, что cheat-коды использовать нельзя).


def main():
	count_platforms = 1
	with open('INPUT.TXT', 'r') as f:
		count_platforms = int(f.readline())
		platforms = list(map(lambda x: int(x), f.readline().split()[:count_platforms]))

	energy_used = [0 for x in range(count_platforms)]

	if count_platforms > 1:		
		energy_used[0] = 0
		energy_used[1] = abs(platforms[1] - platforms[0])

		for x in range(2, count_platforms):
			energy_used[x] = min(energy_used[x - 1] + abs(platforms[x - 1] -platforms[x]),
								 energy_used[x - 2] + 3 * abs(platforms[x - 2] - platforms[x]))

	with open('OUTPUT.TXT', 'w') as f:
		f.write(str(energy_used[-1]))

if __name__ == '__main__':
	main()