import pandas as pd

from datetime import datetime


def csv_reader(filename):

    # load data from csv file
    df = pd.read_csv(filename)
    # columns: cdatetime | address | district | beat | grid | crimedescr | ucr_ncic_code | latitude | longitude

    # modify datetime format
    df.cdatetime = df.cdatetime.apply(lambda x : datetime.strptime(x, '%m/%d/%y %H:%M').strftime('%Y/%m/%d %H:%M:%S'))

    return df