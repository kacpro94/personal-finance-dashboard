def loadCSV(self, file_path):
        try:
            dane = pd.read_csv(file_path, delimiter=';', index_col=False, skiprows=25)
            dane.columns = dane.columns.str.replace("#", "")
            dane = dane.drop('Rachunek', axis=1)
            dane = dane.iloc[:, :-1]
            dane['Kwota'] = dane['Kwota'].str.replace(" PLN", "")
            dane['Kwota'] = dane['Kwota'].str.replace(",", ".")
            dane['Kwota'] = dane['Kwota'].str.replace(" ", "").astype(float)
            return dane
        except:
            dane = pd.read_csv(file_path, encoding='cp1250', delimiter=';', index_col=False, skiprows=19)
            dane.columns = dane.columns.str.replace("#", "")
            dane = dane.drop(['Data księgowania','Tytuł','Nazwa banku','Szczegóły',
                              "Nr rachunku",'Nr transakcji','Waluta','Waluta','Waluta',
                              'Kwota płatności w walucie','Kwota blokady/zwolnienie blokady',
                              'Konto','Saldo po transakcji'], axis=1)
            dane = dane.rename(columns={'Data transakcji':'Data operacji',
                                        'Dane kontrahenta':"Opis operacji",
                                        'Kwota transakcji (waluta rachunku)':"Kwota"})
            dane = dane.iloc[:-1, 0:3]
            dane['Kategoria'] = ""
            dane["Opis operacji"] = "ING " + dane["Opis operacji"]
            dane['Kwota'] = dane['Kwota'].str.replace(" PLN", "")
            dane['Kwota'] = dane['Kwota'].str.replace(",", ".")
            dane['Kwota'] = dane['Kwota'].str.replace(" ", "").astype(float)
            dane['Kwota'] = dane['Kwota']/2
            dane = dane[["Data operacji","Opis operacji","Kategoria","Kwota"]]
            return dane
