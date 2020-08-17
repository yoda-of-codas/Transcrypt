import math
import os

def encryptMessage(key, message):
    count = 0
    
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return (''.join(ciphertext))

def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) -len(message)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns -1 and row >= numOfRows -numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

#message = 'm  mrybio asnok sweatnl e'
#for key in range(1,len(message)+1):
 #   print('using key #'+str(key),decryptMessage(key,message))
    
def inputs():
    filename = input('Enter the file location: ')
    i = -1
    c=''
    while i>-(len(filename)+1):
        if filename[i]=='/':
            a,loc,index = filename[i+1:],filename[0:i+1],-1
            if '.' not in filename:
                newfile = a + 'encrypted'
                extension=''
            while index>-(len(a)+1):
                if a[index]=='.':
                    b,extension = a[0:index],a[index:]
                    newfile = b + 'encrypted'
                    break
                index-=1
            break
        i-=1
        
    outputname = loc+newfile+extension        
    if os.path.exists(filename):
        file = open(filename,'r')
        message = file.read()
        key = input('Enter the encryption key')
        output = encryptMessage(key,message)
        ofo = open(outputname,'w')
        ofo.write(output)
        ofo.close()
    else:
        print('Path or file is invalid')
        input()



if __name__ == '__main__':
    inputs()
