def main():
    lines = []
    line_len = 0
    push_ups = 0

    with open('INPUT.TXT', 'r') as f:
        line_len, rows = list(map(lambda x: int(x), f.readline().split()[:2]))
        for row in range(rows):
            line = f.readline()
            line = [int(x) for x in line.split()]

            memory = [0 for x in range(line_len)]
            for index in range(line_len):
                human_height = line[index]
                push_ups += sum(memory[human_height:])
                memory[human_height - 1] = 1
                    

    with open('OUTPUT.TXT', 'w') as f:
    	f.write(str(push_ups))

if __name__ == '__main__':
    main()