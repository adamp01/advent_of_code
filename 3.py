def chrToInt(char):
    if char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return ord(char) - ord('a') + 1

def main():
    with open("input_3.txt", "r") as infile:
        lines = infile.readlines()

        total = 0
        # Part 1
        for line in lines:
            items = len(line.strip())//2
            first = line[:items]
            second = line[items:]
            total += chrToInt(set.intersection(*map(set, [first, second])).pop())

        print(total)

        # Part 2
        group = []
        total = 0
        for line in lines:
            group.append(line.strip())
            if len(group) == 3:
                total += chrToInt(set.intersection(*map(set,group)).pop())
                group = []

        print(total)


if __name__ == "__main__":
    main()
