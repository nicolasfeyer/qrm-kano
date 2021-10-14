import csv
import json
from collections import Counter
from typing import List, Dict


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def get_category_by_answers(pos: int, neg: int):
    if pos == 1 and neg == 5:
        return "P"

    elif pos == neg == 5 or pos == neg == 1:
        return "D"

    elif pos == 1 and (neg in [2, 3, 4]):
        return 'A'

    elif neg == 5 and (pos in [2, 3, 4]):
        return "O"

    elif neg in [2, 3, 4] and pos in [2, 3, 4]:
        return "I"

    else:
        return "C"


def replace_with_value(answers: List[str], answer_options: Dict) -> List[int]:
    return [answer_options.get(item, item) for item in answers]


def print_res(res: Dict, category_letter: List[str], delimiter=";"):
    print("Sujet" + delimiter + delimiter.join(category_letter))
    for subject, res_ in res.items():
        print(subject + delimiter, end="")
        for c in category_letter:
            if c not in res_:
                print("0" + delimiter, end="")
            else:
                print(str(res_[c]) + delimiter, end="")

        print()


def main():
    # load answer options
    with open('answer_options.json') as json_file:
        answer_options = json.load(json_file)

    # load subjects
    with open("subjects.txt") as file:
        subjects = [line.rstrip() for line in file.readlines()]

    # Kano standard
    category_letter = ["A", "P", "O", "I", "C", "D"]

    with open('answers.tsv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t', quotechar='"')

        answers = list(map(list, zip(*list(csvreader))))  # transpose

        answers = answers[1:]  # remove header

        res = dict()

        for i, (pos, neg) in zip(range(len(list(pairwise(answers)))), pairwise(answers)):
            pos, neg = replace_with_value(pos[1:], answer_options), \
                       replace_with_value(neg[1:], answer_options)  # [1:] to ignore the question

            categories_count = dict(
                Counter([get_category_by_answers(p, n) for p, n in zip(pos, neg)]))  # count by category

            res[subjects[i]] = categories_count

        print_res(res, category_letter)


if __name__ == "__main__":
    main()
