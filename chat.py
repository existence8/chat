#75格式改寫練習

#讀檔
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


#轉化
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        
        if person: #理解成如果person有值，才…
            new.append(person + ': '+ line)
    return new

 #寫入
def write(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    print(lines)
    lines = convert(lines)
    print(lines)
    write('output.txt', lines)

main()

