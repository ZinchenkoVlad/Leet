romanVocab = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def romanToInt(s: str) -> int:
    i = 0
    totalValue = 0
    lenS = len(s)
    while i < lenS:

        value1 = romanVocab[s[i]]
        if 0 < i+1 < lenS:
            value2 = romanVocab[s[i+1]]
            if value2 > value1:
                value1 = value2 - value1
                i += 1
        totalValue += value1
        i += 1
    return totalValue


def main():
    print(romanToInt("MCMXCIV"))


if __name__ == "__main__":
    main()
