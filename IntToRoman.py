romanVocab = [
    "I",
    "V",
    "X",
    "L",
    "C", 
    "D", 
    "M"
]

romanVocabNum = [
    1,  
    5,  
    10, 
    50, 
    100,
    500,
    1000
]

def intToRoman(num: int) -> str:
    if(num>= 4000):
        return "\nERROR num is bigger then 3999\n"

    list = []
    resultList = []
    # do our list in propriate way
    list = [int(x) for x in str(num)]
    
    list.reverse()
    y = len(list)-1
    while y >= 0:
        list[y] = int(str(list[y]) + str('0' * y))
        y-=1
    list.reverse()


    i = 0
    while i < len(list):
        if (list[i] in romanVocabNum):
            # if num exist in list
            resultList.append(romanVocab[romanVocabNum.index(list[i])])
        else:
            # if num = vocab[i+1] - vocab[i]
            for k in range(0, 5, 2):
                for l in range(k+1, k+3, 1):
                    if(list[i] == romanVocabNum[l] - romanVocabNum[k]):
                        resultList.append(str(romanVocab[k]) + str(romanVocab[l]))
                    else:
                        for x in range (1, 4, 1):
                            if(list[i] == romanVocabNum[l] + romanVocabNum[k]*x):
                                resultList.append(str(romanVocab[l]) + str(romanVocab[k])*x)
            for k in range(0, 7, 2):
                for x in range (1, 3, 1):
                            if(list[i] == romanVocabNum[k] + romanVocabNum[k]*x):
                                resultList.append(str(romanVocab[k]) + str(romanVocab[k])*x)
        i+=1
    print(list)
    print(num)
    #return ''.join(resultList)
    
    return resultList



def main():
    print(intToRoman(1994))


if __name__ == "__main__":
    main()
