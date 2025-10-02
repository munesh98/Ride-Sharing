from sys import argv

def main():
    ARGUMENT_INDEX = 2
    VALUE_SELECTED = 1

    if len(argv) != ARGUMENT_INDEX :
        raise Exception("File path not entered")
    file_path = argv[VALUE_SELECTED] 
    f = open(file_path, 'r')
    Lines = f.readlines()
    return Lines

READING_INPUT_FILE_INSTANCE = "__main__"
if __name__ == READING_INPUT_FILE_INSTANCE:
    main()