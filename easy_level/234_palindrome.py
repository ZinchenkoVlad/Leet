def isPalindrome(head):
    return head == head[::-1]


def main():
    print(isPalindrome([1,2,3,1]))


if __name__ == "__main__":
    main()
