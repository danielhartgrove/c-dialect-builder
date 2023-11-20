import sys
import os

keywords_dict = {
    'auto': None, 
    'double': "double_ting",
    'int': "number_ting",
    'struct': None,
    'break': "ching",
    'else': None, 
    'long': "long_ting", 
    'switch': "switcheroo",
    'case': None,
    'enum': None, 
    'register': None,
    'typedef': None,
    'char': None,
    'extern': None,
    'return': "buss_me", 
    'union': None,
    'continue': "go_on_bruv", 
    '+': "calculation_ting",
    'for': None, 
    'signed': None, 
    'void': "nuffin",
    'do': "aight_boom", 
    'if': None, 
    'static': "frozen", 
    'while': None,
    'default': "standard", 
    'goto': None, 
    'sizeof': "howbig?", 
    'volatile': "dangerous",
    'const': None, 
    'float': None, 
    'short': "likkle", 
    'unsigned': None,
    'try':"fuck_around",
    'catch':"find_out",
    'printf':"waffle",
    'true':"ongod",
    'false':"cap"
}

file_extension = ".road"

filename = sys.argv[1]
print("Filename: ", filename)
if(filename.endswith(file_extension) == False):
    print("ERROR: Invalid File Type")
else:
    try:
        i = open(filename, "r")   
    except:
        print("ERROR: File Does Not Exist")
    i = open(filename, "r")                        #input
    o = open(filename.replace(file_extension, "") + ".c", "w") #output
    print("SUCCESS: Parsing...")

    swapped_dict = {value: key for key, value in keywords_dict.items() if value is not None}
    lines = i.readlines()
    for line in lines:
        newline = line
        for keyword in swapped_dict:
            newline = newline.replace(keyword, swapped_dict[keyword])
        o.write(newline)
    i.close()
    o.close()
    print("SUCCESS: Parsed")
    print("SUCCESS: Compiling...")
    
    try:
        string = "gcc " + (filename.replace(file_extension, "") + ".c") + " -o " + filename.replace(file_extension, "")
        print(string)
        os.system(string)
        print("SUCCESS: Compiled")
    except:
        print("ERROR: Post-intermediary compilation failed")
