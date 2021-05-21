import os
import random

DIR = "data/api/"
MAX = "2021-04-30"
MIN = "2021-04-23"
PAIRS = [
    ("2021-04-26", "2021-04-23"),
    ("2021-04-27", "2021-04-26"),
    ("2021-04-28", "2021-04-27"),
    ("2021-04-29", "2021-04-28"),
    ("2021-04-30", "2021-04-29"),
    ("2021-04-30", "2021-04-23"),
]


def calculate_return(tup_final, tup_init):
    close_final = float(tup_final[-1])
    close_init = float(tup_init[-1])
    return 100 * (close_final - close_init) / close_init


def calculate_returns(path):
    d = {}
    with open(path, "r") as history:
        for line in history:
            row = line[:-1].split(',')
            if MIN <= row[0] <= MAX:
                d[row[0]] = tuple(row[1:-2])

    return [calculate_return(d[p[0]], d[p[1]]) for p in PAIRS]


def disturb(return_list):
    fade = 0.999
    noise = 0
    return [r*fade+(random.random()-0.5)*noise for r in return_list]


if __name__ == '__main__':
    with open("pretest_answer_0.csv", "w") as answer:
        answer.write("tickers,return_day_1,return_day_2,return_day_3,return_day_4,return_day_5,return_week\n")
        for name in sorted(os.listdir(DIR)):
            contents = [name.split('.')[0], *[f"{r:.2f}" for r in disturb(calculate_returns(DIR+name))]]
            answer.write(','.join(contents) + '\n')
