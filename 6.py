from collections import deque

def main():
    with open("input_6.txt", "r") as infile:
        buffer = infile.read().strip()
        unq = deque()

        # Part 1
        for i in range(len(buffer)):
            unq.append(buffer[i])
            if len(unq) == 4 and len(set(unq)) == 4:
                print(i + 1)
                break
            if len(unq) == 4:
                unq.popleft()

        # Part 2
        unq = deque()
        for i in range(len(buffer)):
            unq.append(buffer[i])
            if len(unq) == 14 and len(set(unq)) == 14:
                print(i + 1)
                break
            if len(unq) == 14:
                unq.popleft()


if __name__ == "__main__":
    main()
