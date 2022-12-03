from itertools import groupby

# Wanted to find a nicer solution
with open("input_1.txt", "r") as infile:
    lines = infile.readlines()

    # Part 1
    cals = max([
        sum([int(item.strip()) for item in group])
        for key, group in groupby(lines, lambda x: x != "\n")
        if key
    ])

    print(cals)

    # Part 2
    cals = [
        sum([int(item.strip()) for item in group])
        for key, group in groupby(lines, lambda x: x != "\n")
        if key
    ]
    cals.sort(reverse=True)
    print(sum(cals[:3]))

# The quick way
with open("input_1.txt", "r") as infile:
    lines = infile.readlines()

    current = 0
    cals = []
    for line in lines:
        if line == "\n":
            cals.append(current)
            current = 0
            continue

        current += int(line.strip())
    cals.sort(reverse=True)
    print(sum(cals[:3]))

# The overengineered way
class Party():
    def __init__(self):
        self.elves = []

    def add_elf(self, elf):
        self.elves.append(elf)
        return elf

    def get_party_calories(self):
        return [elf.inventory.get_total_calories() for elf in self.elves]

class Elf():
    def __init__(self):
        self.inventory = Inventory()

class Inventory():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_total_calories(self):
        calories = [item.calories for item in self.items]
        return sum(calories)

class Item():
    def __init__(self, calories):
        self.calories = calories

if __name__ == "__main__":
    # Start a party
    party = Party()

    # Add our initial Elf
    elf = party.add_elf(Elf())

    # Start adding items and Elves
    with open("input_1.txt", "r") as infile:
        lines = infile.readlines()
        for line in lines:
            if line == "\n":
                elf = party.add_elf(Elf())
                continue
            elf.inventory.add_item(Item(int(line.strip())))

    # Get the total calories for each Elf in the party
    calories = party.get_party_calories()

    # Get the largest
    print(max(calories))

    # Get the top 3
    calories.sort(reverse=True)
    print(sum(calories[:3]))
