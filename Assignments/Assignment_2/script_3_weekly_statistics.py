import os

DIR = "data/api/"


def is_continues(date_0, date_1):
    leap_years = (2020, 2016, 2012, 2008, 2004, 2000, 1996, 1992, 1988, 1984, 1980, 1976, 1972, 1968, 1964, 1960)
    y1, m1, d1 = map(int, date_0.split('-'))
    y2, m2, d2 = map(int, date_1.split('-'))
    if d1 + 1 == d2:
        return True
    if m1 in (1, 3, 5, 7, 8, 10, 12) and d1 == 31 and d2 == 1:
        return True
    if m1 in (4, 6, 9, 10) and d1 == 30 and d2 == 1:
        return True
    if m1 == 2 and y1 in leap_years and d1 == 29 and d2 == 1:
        return True
    if m1 == 2 and y1 not in leap_years and d1 == 28 and d2 == 1:
        return True
    return False


def calculate_return(week_0, week_1):
    close_i = week_0[-1][-3]
    close_f = week_1[-1][-3]
    return 100 * (close_f - close_i) / close_i


def calculate_returns(path):
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
                returns.append(calculate_return(weeks[0], weeks[1]))

    average = sum(returns) / len(returns)
    return [average, max(returns), min(returns), sum([(r - average) ** 2 for r in returns]) / len(returns)]


if __name__ == '__main__':
    with open("weekly_return_statistics.csv", "w") as answer:
        answer.write("tickers,average_return,max_return,min_return,return_variance\n")
        for name in sorted(os.listdir(DIR)):
            contents = [name.split('.')[0], *[f"{r:.4f}" for r in calculate_returns(DIR+name)]]
            answer.write(','.join(contents) + '\n')
