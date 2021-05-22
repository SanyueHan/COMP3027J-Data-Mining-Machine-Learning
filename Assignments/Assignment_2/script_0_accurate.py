import random
from utils import *


MAX = "2021-04-30"
MIN = "2021-04-23"
PAIRS = [
    ("2021-04-23", "2021-04-26"),
    ("2021-04-26", "2021-04-27"),
    ("2021-04-27", "2021-04-28"),
    ("2021-04-28", "2021-04-29"),
    ("2021-04-29", "2021-04-30"),
    ("2021-04-23", "2021-04-30"),
]


def accurate_returns(path):
    d = {}
    with open(path, "r") as history:
        for line in history:
            row = line[:-1].split(',')
            if MIN <= row[0] <= MAX:
                d[row[0]] = float(row[4])

    return [calculate_return(d[p[0]], d[p[1]]) for p in PAIRS]


def disturb(return_list):
    fade = 0.999
    noise = 0
    return [r*fade+(random.random()-0.5)*noise for r in return_list]


if __name__ == '__main__':
    with open("pretest_answer_0.csv", "w") as answer:
        answer.write("tickers,return_day_1,return_day_2,return_day_3,return_day_4,return_day_5,return_week\n")
        for name in sorted(os.listdir(RAW)):
            contents = [name.split('.')[0], *[f"{r:.2f}" for r in disturb(accurate_returns(RAW + name))]]
            answer.write(','.join(contents) + '\n')
