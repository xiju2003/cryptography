

ciphertext = ""


def Scanf():
   
    global ciphertext

    ciphertext = input("请输入密文:")

    ciphertext.lower()

def friedman(ciphLen):

    for i in range(ciphLen):

        alphabet = {}

        countnum = 0

        text = ciphertext[i::ciphLen] #取出密钥此密钥分量对应的密文部分
        
        for i in text:

            alphabet[i] = 0


        for i in text:

            alphabet[i] += 1
        
        for i in alphabet:

            countnum += alphabet[i] * (alphabet[i] - 1)

        coincidence = float(countnum)/(len(text)*(len(text)-1))

        print (coincidence)


def main():

    Scanf()  #接收程序输入

    for i in range(20):

        friedman(i)
        
        print("------------------------------")




if "__main__" == __name__ :

    main()
