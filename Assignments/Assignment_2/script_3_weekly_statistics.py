from utils import *


def weekly_statistics(path):
    returns = []
    with open(path, "r") as history:
        weeks = []
        week = []
        last = None
        for line in history:
            try:
                row = line.split(',')
                data = tuple(map(float, row[1:]))
                date = row[0]
            except ValueError:
                continue
            if not week or is_continues(last, date):
                week.append(data)
                last = date
            else:
                weeks.append(week),
                week = []
            if len(weeks) == 3:
                weeks.pop(0)
            if len(weeks) == 2:
                returns.append(calculate_return(weeks[0][-1][-3], weeks[1][-1][-3]))

    average = sum(returns) / len(returns)
    return [average, max(returns), min(returns), sum([(r - average) ** 2 for r in returns]) / len(returns)]


if __name__ == '__main__':
    with open("weekly_return_statistics.csv", "w") as answer:
        answer.write("tickers,average_return,max_return,min_return,return_variance\n")
        for name in sorted(os.listdir(DIR)):
            contents = [name.split('.')[0], *[f"{r:.4f}" for r in weekly_statistics(DIR + name)]]
            answer.write(','.join(contents) + '\n')
