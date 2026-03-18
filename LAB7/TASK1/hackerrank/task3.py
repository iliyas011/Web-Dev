

def split_and_join(line):
    for i in line:
        if i == ' ':
            line = line.replace(i, '-')
            return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)