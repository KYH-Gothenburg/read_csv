import re

def read_csv(filename, sep=',', header=True):
    with open(filename, encoding='utf-8') as in_file:
        if header:
            header_line = in_file.readline()
            header_line = header_line.strip()
            header_line = re.split(f'{sep}(?=(?:[^"]*\"[^"]*\")*[^"]*$)', header_line)
        lines = []
        for line in in_file:
            line = line.strip()
            line = re.split(f'{sep}(?=(?:[^"]*\"[^"]*\")*[^"]*$)', line)
            line = [item if '"' not in item else item.replace('"', '') for item in line]
            lines.append(line)

        if header:
            return [{header: line[i] for i, header in enumerate(header_line)} for line in lines]
        else:
            return lines


def main():
    result = read_csv('test.csv', sep=';', header=False)
    print()


if __name__ == '__main__':
    main()
