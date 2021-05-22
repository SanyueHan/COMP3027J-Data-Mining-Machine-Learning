from utils import *


def average_returns(path):
    total = 0
    count = 0
    with open(path, "r") as history:
        closes = []
        for line in history:
            try:
                close = float(line.split(',')[4])
            except ValueError:
                continue
            closes.append(close)
            if len(closes) == 3:
                closes.pop(0)
            if len(closes) == 2:
                total += calculate_return(closes[0], closes[1])
                count += 1
    average = total / count
    return [average for _ in range(5)] + [(((100+average)/100)**5-1)*100]


if __name__ == '__main__':
    with open("pretest_answer_1.csv", "w") as answer:
        answer.write("tickers,return_day_1,return_day_2,return_day_3,return_day_4,return_day_5,return_week\n")
        for name in sorted(os.listdir(RAW)):
            contents = [name.split('.')[0], *[f"{r:.2f}" for r in average_returns(RAW + name)]]
            answer.write(','.join(contents) + '\n')
