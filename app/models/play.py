import csv


def z(ticker):
    ticker_list = []
    with open('tickers.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            ticker_list.append(i[1])
    print(ticker_list)
    if ticker in ticker_list:
        print('in')
    else:
        print('not in')


z('FB')
