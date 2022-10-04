def calc(num):
    i = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        i += 1
    return i


def main():
    print(calc(14))


if __name__ == "__main__":
    main()
