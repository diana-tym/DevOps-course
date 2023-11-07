import sys

def read_input(file):
    # for line in file:
        # split the line into words
    yield file.split()

def main(s, separator='\t'):
    # input comes from STDIN (standard input)
    # data = read_input(sys.stdin)
    data = read_input(s)
    file = open('file1.txt', 'w')

    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            file.write('%s%s%d\n' % (word, separator, 1))
            print('%s%s%d' % (word, separator, 1))

    file.close()


s = "abc ddd hello abc yyy def hello"
if __name__ == "__main__":
    main(s)
