def main():
    dict = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'L': 9,
        'M': 10,
        'N': 11,
        'O': 12,
        'P': 13,
        'Q': 14,
        'R': 15,
        'S': 16,
        'T': 17,
        'U': 18,
        'V': 19,
        'Z': 20
    }
    dictReverse={}
    for key in dict:
        dictReverse[dict[key]]= key
    print(dict)
    print(dictReverse)
    crypt(dict)
    decrypt(dictReverse)


def crypt(dict):
    # alphabet dict

    #dichiarazione variabili
    key="ITIDELPOZZO"
    mex="CIAO"
    keyCrypted=[]
    cryptedMex=[]
    sumMexKey= []

    #crypt key
    for c in key:
        keyCrypted.append(str(dict.get(c)))
    print(keyCrypted)

    #crypt mex
    for i in mex:
        cryptedMex.append(str(dict.get(i)))
    print(cryptedMex)

    #mex + key
    for a in range(0,len(cryptedMex)):
        sumMexKey.append(str(int(keyCrypted[a])+ int(cryptedMex[a]) % 21))
    print(sumMexKey)


def decrypt(dict):
    mexdec=[]
    for a in range(0,len(sumMexKey)):
        mexdec.append(str(int(keyCrypted[a])+ int(cryptedMex[a]) % 21))
    print(mexdec)


if __name__ == '__main__':
    main()