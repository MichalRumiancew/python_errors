import sys


def get_filename():
    if len(sys.argv) >= 3:
        #filename = sys.argv[1]
        #return filename
        imput1 = int(sys.argv[1])
        imput2 = int(sys.argv[1])
        return imput1 + imput2
    else:
        print("[ WARNING ] You should run this program by calling: python parser.py filename")
        return ""

def rsd_from_file_to_list(filename):
    #otwieranie pliku
    #with open(filename)
    with open("input.txt","r_+") as file_to_read:
        print(file_to_read.())

def main():
    filename = get_filename()

    if len(filename) == 0:
        return
    
    print(f"File to parse: {filename}")
    
if __name__ == "__main__":
    main()