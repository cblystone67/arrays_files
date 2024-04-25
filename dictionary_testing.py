def count_uniq(str):
    dict = {}
    for s in str:
        if s not in dict:
            dict[s] = 1
        elif s in dict:
            dict[s] += 1

    count = max(dict.values())

    return count


def main():
    print(count_uniq("111224446"))


if __name__ == "__main__":
    main()
