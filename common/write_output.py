import xlrd
import pandas as pd

def write_to_excel(df, output_path):
    with pd.ExcelWriter(output_path) as writer:
        df.to_excel(writer, sheet_name='GeoCodeSheet1')
