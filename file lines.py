import os.path

def main():
    file_name = input('Enter file name: ')
    if not os.path.isfile(file_name):
        print(file_name, 'does not exist in this directory.')
    else:
        file = open(file_name, 'r')
        line = file.readline()
        line_number = 0

        while line:
            line_number += 1
            print(format(line_number, '4d'), ': ',
                  line.strip(), sep='')
            line = file.readline()
        print('Found', line_number, 'lines.')
        print('Value of line that caused loop to stop:', line)
        file.close()
main()