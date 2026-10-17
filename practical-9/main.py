'''Write a program to read a file and
a. Print the total number of characters, words and lines in the file.
b. Calculate the frequency of each character in the file. Use a variable of dictionary type
to maintain the count.
c. Print the words in reverse order.
d. Copy even lines of the file to a file named ‘File1’ and odd lines to another file named
‘File2’.
'''

#a
def func_a():
    with open("practical-9\\text.txt","r") as fh:
        text = fh.read()
        print("Total number of characters in the file are:",len(text))
        words = text.split(" ")
        print("Total number of words in the file are:",len(words))
        fh.seek(0)
        lines = fh.readlines()
        print("Total number of lines in the file are:",len(lines))
    
#b
def func_b():
    char_dict = {}
    with open("practical-9\\text.txt","r") as fh:
        text = fh.read()
        for i in text:
            if i not in char_dict:
                char_dict[i] = 1
            else:
                char_dict[i] += 1

        print(char_dict)


#c
def func_c():
    with open("practical-9\\text.txt","r") as fh:
        text = fh.read()
        rev = text[::-1]
        print(rev)


#d
def func_d():
    with open("practical-9\\text.txt","r") as fh:
        lines = fh.readlines()
        for i in range(len(lines)):
            if i%2 == 0:
                with open("practical-9\\even_text.txt","a") as fh_e:
                    fh_e.write(lines[i])
            else:
                with open("practical-9\\odd_text.txt","a") as fh_o:
                    fh_o.write(lines[i])

func_a()

func_b()

func_c()

func_d()