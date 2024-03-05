import argparse

parser = argparse.ArgumentParser(description="Encrypts given text either from stdin or as a file")
parser.add_argument("-f", "--file", action="store_true", help="toggle encoding a file")
parser.add_argument("TEXT", help="Plain text or name of file to encode")

args = parser.parse_args()

if args.file:
    # open a file and encode it 
    file = open(args.TEXT, "r+")
    print(file.read())
    file.write(file.read() + "\n hello world!")
    pass
    print(file.read())
    ## encode
    pass
else:
    # encode the file and print it to stdout
    print(args.TEXT)
    pass
