import os

def isenglish(message):
    message = message.upper()
    message = message.split()
    
    
    file = open('dictionary.txt','r')
    diction = file.read()
    diction = diction.split()
    count = 0
    for word in message:
        if word in diction:
            count+=1
    rating = count/len(message)
    return rating
    
            
def main():
    print ('blank')

if __name__ == '__main__':
    main()
