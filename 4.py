def main():
    with open("input_4.txt", "r") as infile:
        lines = infile.readlines()

        total = 0
        total_2 = 0
        # Part 1
        for line in lines:
            items = line.strip().split(',')
            a = items[0].split('-')
            b = items[1].split('-')
            set1 = set(range(int(a[0]), int(a[1]) + 1))
            set2 = set(range(int(b[0]), int(b[1]) + 1))
            intersect = set1 & set2
            if (len(intersect) == len(set1)) or (len(intersect) == len(set2)):
                total += 1

        # Part 2
            if len(intersect) != 0:
                total_2 += 1

        print(total)
        print(total_2)


if __name__ == "__main__":
    main()
