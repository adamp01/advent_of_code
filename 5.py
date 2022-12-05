import re
from collections import deque
from copy import deepcopy


def learned():
    with open("input_5.txt", "r") as infile:
        crates, instructions = infile.read().split("\n\n")
        stacks = []

        for line in crates.splitlines():
            for row, idx in enumerate(range(1, len(line), 4)):
                if len(stacks) <= row:
                    stacks.append(deque())
                if line[idx] != " ":
                    stacks[row].append(line[idx])

        stacks_2 = deepcopy(stacks)
        # Part 1
        for instruct in instructions.splitlines():
            i, j, k = map(int, re.findall("\d+", instruct))
            for _ in range(i):
                stacks[k - 1].appendleft(stacks[j - 1].popleft())

        # Part 2 
        for instruct in instructions.splitlines():
            i, j, k = map(int, re.findall("\d+", instruct))
            tmp = deque()
            for _ in range(i):
                tmp.appendleft(stacks_2[j - 1].popleft())
            stacks_2[k - 1].extendleft(tmp)

        print(("").join([x[0] for x in stacks]))
        print(("").join([x[0] for x in stacks_2]))
                

def first():
    with open("input_5.txt", "r") as infile:
        crates = ['','','','','','','','','']
        instruct = []
        switch = False
        for line in infile:
            if line == "\n":
                switch = True
                continue
            if switch:
                instruct.append(line.strip())
            else:
                if '1' in line:
                    continue
                for i, idx in enumerate(range(1, len(line.rstrip("\n")), 4)):
                    if line[idx] != " ":
                        crates[i] += line[idx]

        crates_2 = deepcopy(crates)
        # Part 1
        for row in instruct:
            i, j, k = map(int, re.findall("\d+", row))
            # Moving i crates from row[1] to row[2]
            for _ in range(i):
                crates[k - 1] = crates[j - 1][0] + crates[k - 1]
                crates[j - 1] = crates[j - 1][1:]

        # Part 2
        for row in instruct:
            i, j, k = map(int, re.findall("\d+", row))
            crates_2[k - 1] = crates_2[j - 1][:i] + crates_2[k - 1]
            crates_2[j - 1] = crates_2[j - 1][i:]

        print(("").join([x[0] for x in crates]))
        print(("").join([x[0] for x in crates_2]))

if __name__ == "__main__":
    first()
    learned()
    