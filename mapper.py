import sys

def read_input(file):
    yield file.split()

def main(s, separator='\t'):
    data = read_input(s)
    file = open('file1.txt', 'w')

    for words in data:
        for word in words:
            file.write('%s%s%d\n' % (word, separator, 1))
            print('%s%s%d' % (word, separator, 1))

    file.close()


s = "abc ddd hello abc yyy def hello"
if __name__ == "__main__":
    main(s)
