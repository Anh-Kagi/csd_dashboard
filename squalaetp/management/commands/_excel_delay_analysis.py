from utils.excel_format import ExcelFormat


class ExcelDelayAnalysis(ExcelFormat):
    """## Read data in Excel file for Delay Analysis ##"""

    DROP_COLS = ['ref_produit_commerciale', 'ref_produit_clarion', 'code_pdv', 'nom_pdv',
                 'date_daccord_de_la_demande', 'delai_prevu_sp', 'nom_equipe', 'n_commande_de_travaux']
    COLS_DATE = {'date_retour': "'%d/%m/%Y", 'date_de_cloture': "'%d/%m/%Y %H:%M:%S"}

    def __init__(self, file, sheet_index=0, columns=None):
        """
        Initialize ExcelDelayAnalysis class
        :param file:
            excel file to process
        :param sheet_index:
            Sheet index to be processed from excel file
        :param columns:
            Number of the last column to be processed
        """
        super().__init__(file, sheet_index, columns, skip_rows=8)
        self._columns_convert(digit=False)
        self.sheet.replace({"Oui": 1, "Non": 0}, inplace=True)
        self.sheet.drop(columns=self.DROP_COLS, inplace=True)
        self._date_converter(self.COLS_DATE)

    def xelon_table(self, file_number):
        """
        Extracting data for the Xelon table from the Database
        :param file_number:
            File number to search
        :return:
            Dictionnary that represents the data of file number to insert Xelon table
        """
        row_dict = {}
        row_index = self.sheet[self.sheet['n_de_dossier'] == file_number].index
        if list(row_index):
            row_dict = dict(self.sheet.loc[row_index[0]])
            row_dict = self.key_formatting(row_dict)
        return row_dict

    def table(self):
        """
        Extracting data for the table from the Database
        :return:
            list of dictionnaries that represents the data for table
        """
        data = []
        for line in range(self.nrows):
            row_dict = self.key_formatting(dict(self.sheet.loc[line].dropna()))
            data.append(row_dict)
        return data

    def key_formatting(self, data):
        data['ilot'] = self.basename
        data["numero_de_dossier"] = data["n_de_dossier"]
        del data["n_de_dossier"]
        return data