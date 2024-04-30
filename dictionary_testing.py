def count_uniq(str):
    dict = {}
    count = 0

    for s in str:
        count[s] = count.get(s, 0) + 1
    max_count = max(count.values())

    return count


def main():
    print(count_uniq("111224446"))


if __name__ == "__main__":
    main()
