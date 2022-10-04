def calc(accounts):
    totalValue = 0
    i = 0
    j = 0
    sum = 0
    while i < len(accounts):
        while j < len(accounts[i]):
            sum += accounts[i][j]
            j+=1
        accounts[i] = sum
        
        i += 1
        j = 0
        sum = 0
    totalValue = max(accounts)   

    print(accounts)
    
    return totalValue


def main():
    print(calc([[1,5],[7,3],[3,5]]))


if __name__ == "__main__":
    main()
