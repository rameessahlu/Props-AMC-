import pandas as pd
import xlrd
import click, sys


def read_excel_file(file_name):
    try:
        df = pd.read_excel(file_name)
        #print the column names
        #print(df.columns)

        #xls = pd.ExcelFile(file_name)
        #df = pd.read_excel(file_name, sheet_name=None)
    except FileNotFoundError:
        click.echo('Input file {} not found.'.format(file_name))
        sys.exit(1)
    except xlrd.biffh.XLRDError:
        click.echo('Unsupported file format.')
        sys.exit(1)
    return df
