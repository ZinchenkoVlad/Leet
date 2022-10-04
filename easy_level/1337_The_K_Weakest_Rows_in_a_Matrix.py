
def kWeakestRows(mat, k):
    list = {}

    for i in range(0, len(mat)):
        list[i] = sum(mat[i])
    list=sorted(list, key=list.get)

    return list[:k]


def main():
    print(kWeakestRows(
        [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]],

        3

        ))


if __name__ == "__main__":
    main()
