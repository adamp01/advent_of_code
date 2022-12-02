def determine_result(theirs, result):
    # If X, lose
    # If Y, draw
    # If Z, win
    score = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1
        },
    }

    result_score = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    return score[theirs][result] + result_score[result]


def main():
    with open("input_2.txt", "r") as infile:
        lines = infile.readlines()

        total = 0
        for line in lines:
            plays = line.strip().split(" ")
            total += determine_result(plays[0], plays[1])

        print(total)


if __name__ == "__main__":
    main()
    