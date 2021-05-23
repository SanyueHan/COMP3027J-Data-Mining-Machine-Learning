from utils import *


LEN = 5


def read_weeks(path):
    """
    split days in to week list
    remove header and Adj Close
    """
    with open(path, "r") as history:
        weeks = []
        week = []
        last = None
        for line in history:
            try:
                row = line.split(',')
                row.pop(5)
                date = row.pop(0)
                data = tuple(map(float, row))
            except ValueError:
                continue
            if not week or is_continues(last, date):
                week.append(data)
                last = date
            else:
                weeks.append(week),
                week = []
    return weeks


def clean_weeks(week_list):
    """
    remove zero values
    raise error if empty entry found
    """
    return [week for week in week_list if valid_week(week)]


def valid_week(week):
    if len(week) == 0:
        raise ValueError
    return all(valid_day(day) for day in week)


def valid_day(day):
    if len(day) == 0:
        raise ValueError
    return all(day)


def calculate_returns(valid_list):
    """
    convert absolute price data to returns,
    """
    returns = []
    for i in range(len(valid_list)-1):
        close_i = valid_list[i][-1][-3]
        close_f = valid_list[i+1][-1][-3]
        returns.append(calculate_return(close_i, close_f))
    return returns


def create_dataset(path, return_list):
    with open(path, "w") as file:
        file.write(','.join([f"{i}_week_before" for i in range(LEN, 0, -1)] + ["target"]) + '\n')
        for i in range(LEN, len(return_list)):
            file.write(','.join(str(return_list[i-j]) for j in range(LEN, -1, -1)) + '\n')


def main():
    for name in sorted(os.listdir(RAW)):
        week_list = read_weeks(RAW + name)
        valid_list = clean_weeks(week_list)
        return_list = calculate_returns(valid_list)
        create_dataset(PRE + name, return_list)


if __name__ == "__main__":
    main()









