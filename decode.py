#Andre Hansen
#CS021-A
#This program encrypts and decrypts files provided by the user.
#----------------------------------------------------------------------------
def main():
    #try running program without any expections
    try:
        #open file, read each line, and remove newlines.
        infile = open('codes.txt', 'r')
        lines = infile.readlines()
        index = 0
        while index < len(lines):
            lines[index] = lines[index].rstrip('\n')
            index+=1
        #define keys list
        keys=[]
        #loop control variable
        x=0
        #loop to append only the keys from the file into the keys list.
        for i in lines:
            keys.append(lines[x][0])
            x+=1
        #define values list
        values=[]
        #loop control variable
        y=0
        #loop to append only the values from the file into the values list.
        for i in lines:
            values.append(lines[y][2])
            y+=1
        #define codes dictionary
        codes = {}
        index2 = 0
        #loop to create all dictionary imputs correctly.
        while index2 <len(keys):
            codes[keys[index2]]=values[index2]
            index2+=1
        #call decode funtion
        decode(codes)
    #exception handling
    except IOError:
        print("Something went wrong with opening the file")
    except:
        print("Something went wrong")
    finally:
        #close files
        infile.close()
def decode(codes):
    #Display choices and ask user to choose one.
    print("1 - Encrypt a file")
    print("2 - Decrypt a file")
    choice = input("Your choice?")
    #if choice equals 1 then user inputs an input and output file to write the data on
    if choice == '1':
        filein=input("Enter the name of the input file:")
        fileout=input("Enter the name of the output file:")
        infile = open(filein,'r')
        outfile = open(fileout,'w')
        #read lines of user file
        lines = infile.readlines()
        index=0
        #loop to search for each character on user file in the dictionary and write the encryption on the output file.
        for x in lines:
            for i in x:
                if i in codes:
                    outfile.write(codes[i])
                elif i == ' ':
                    outfile.write(' ')
                elif i == '\n':
                    outfile.write('\n')
        print("Writing encrypted data to",fileout)
    #if choice equals 2 then user provides a reading file only to be decrypted.
    elif choice == '2':
        infile=open(input("Enter the name of the input file:"),'r')
        lines=infile.readlines()
        print("The decrypted contents of the file are:")
        #Loop to display decrypted file
        for x in lines:
            for i in x:
                if i in codes:
                    print(codes[i],end='')
                elif i == ' ':
                    print(' ',end='')
                elif i == '\n':
                    print('\n',end='')
    #close files
    infile.close()
    outfile.close()
#call main
main()
