from utils import *


def daily_statistics(path):
    returns = []
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
                returns.append(calculate_return(closes[0], closes[1]))
    average = sum(returns)/len(returns)
    return [average, max(returns), min(returns), sum([(r-average)**2 for r in returns])/len(returns)]


if __name__ == '__main__':
    with open("daily_return_statistics.csv", "w") as answer:
        answer.write("tickers,average_return,max_return,min_return,return_variance\n")
        for name in sorted(os.listdir(RAW)):
            contents = [name.split('.')[0], *[f"{r:.4f}" for r in daily_statistics(RAW + name)]]
            answer.write(','.join(contents) + '\n')
