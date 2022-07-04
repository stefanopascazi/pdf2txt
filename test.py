import textract
import sys
import getopt


def myfunc(argv):
    arg_input = ""
    arg_encoding = ""
    arg_method = ""
    arg_help = "{0} -i <input> -e <encoding default utf-8> -m <method default none>".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hi:e:m:", ["help", "input=", 
        "encoding=", "method="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            arg_input = arg
        elif opt in ("-e", "--encoding"):
            arg_encoding = arg
        elif opt in ("-m", "--method"):
            arg_method = arg

    if arg_input == "" :
        print( "Argument input is required" )
        return

    if arg_encoding == "" :
        arg_encoding = 'utf-8'

    if arg_method == "" :
        text = textract.process(arg_input, encoding=arg_encoding)
    else :
        text = textract.process(arg_input, encoding=arg_encoding, method=arg_method)

    
    print( text.decode(arg_encoding) )


if __name__ == "__main__":
    myfunc(sys.argv)