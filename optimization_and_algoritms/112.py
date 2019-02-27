def main():
    lines = []
    line_len = 0
    push_ups = 0

    with open('INPUT.TXT', 'r') as f:
        line_len = int(f.readline().split()[0])
        while True:
            line = f.readline()
            if not line:
                break
            line = [int(x) for x in line.split()]

            for index in range(line_len):
                human_height = line[index]
                for x in range(index, line_len):
                    push_ups += 1 if human_height > line[x] else 0
                    

    with open('OUTPUT.TXT', 'w') as f:
    	f.write(str(push_ups))

if __name__ == '__main__':
    main()