from __future__ import unicode_literals
from xlwt import Workbook
import io
from xlrd import XLRDError
import pandas as pd
import unicodedata
import re
import os


class ExcelFormat:
    """## Base class for formatting Excel files ##"""

    def __init__(self, file, sheet_index, columns, skip_rows=None):
        """
        Initialize ExcelFormat class
        :param file:
            Excel file path
        :param sheet_index:
            Sheet index to be processed from excel file
        :param columns:
            Number of the last column to be processed
        :param skip_rows:
            Rows to skip at the beginning (0-indexed)
        """
        self.basename = os.path.basename(file[:file.find('.')])
        try:
            df = pd.read_excel(file, sheet_index, skiprows=skip_rows)
        except XLRDError:
            df = self._excel_decode(file, skip_rows)
        self.sheet = df.dropna(how='all')
        self.nrows = self.sheet.shape[0]
        self.columns = list(self.sheet.columns[:columns])

    def read_all(self):
        """
        Formatting data from the excel file
        :return:
            list of dictionaries that represents the data in the sheet
        """
        data = []
        for line in range(self.nrows):
            try:
                row = list(self.sheet.loc[line, self.columns])  # get the data in the ith row
                row_dict = dict(zip(self.columns, row))
                data.append(row_dict)
                self.sheet.row_values()
            except KeyError as err:
                print("KeyError pour la ligne : {}".format(err))
        return data

    def _date_converter(self, columns):
        """
        Converting columns to datetime
        :param columns:
            list of columns to convert
        """
        for col_date, col_format in columns.items():
            self.sheet[col_date] = pd.to_datetime(self.sheet[col_date], errors='coerce', format=col_format, utc=True)

    def _columns_convert(self, digit=True):
        """
        Convert the names of the columns to be used by the database
        :param columns:
            List of column names
        :param digit:
            Remove digits from the column names
        :return:
            list of modified column names
        """
        new_columns = {}
        for column in self.columns:
            name = unicodedata.normalize('NFKD', column).encode('ASCII', 'ignore').decode('utf8').lower()
            name = re.sub(r"[^\w\s]+", "", name)
            if not digit:
                name = ''.join(i for i in name if not i.isdigit())
            name = re.sub(r"[\s]+", "_", name)
            new_columns[column] = name
        self.sheet.rename(columns=new_columns, inplace=True)
        self.columns = list(self.sheet.columns)

    def _excel_decode(self, file, skip_rows):
        """
        Fix badly formatted excel files
        :param filename:
            Excel file path
        :param skip_rows:
            Rows to skip at the beginning (0-indexed)
        :return:
            Temporary Excel file in the 'tmp' directory
        """
        file1 = io.open(file, 'r', encoding='latin3')
        data = file1.readlines()

        # Creating a workbook object
        xldoc = Workbook()
        # Adding a sheet to the workbook object
        sheet = xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)
        # Iterating and saving the data to sheet
        for i, row in enumerate(data):
            # Two things are done here
            # Removeing the '\n' which comes while reading the file using io.open
            # Getting the values after splitting using '\t'
            for j, val in enumerate(row.replace('\n', '').split('\t')):
                sheet.write(i, j, val)

        # Saving the file as an excel file
        xldoc.save('/tmp/{}_reformat.xls'.format(self.basename))
        df = pd.read_excel("/tmp/{}_reformat.xls".format(self.basename), sheet_name="Sheet1", skiprows=skip_rows)
        dataframe = df.drop(df[(df['N° de dossier'].isnull()) | (df['N° de dossier'] == 'N° de dossier')].index)
        dataframe.reset_index(drop=True, inplace=True)
        print("File : {}.xls - Row number : {}".format(self.basename, dataframe.shape[0]))
        return dataframe