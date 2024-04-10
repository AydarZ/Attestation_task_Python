import pandas as pd


def print_date():
    df = pd.read_csv('notes.csv', sep = ',')
    date_1 = input('Введите начальную дату в формате ГГГГ-ММ-ДД: ')
    date_2 = input('Введите конечную дату в формате ГГГГ-ММ-ДД: ')
    print(df[(df['Date']>=date_1)&(df['Date']<=date_2)])