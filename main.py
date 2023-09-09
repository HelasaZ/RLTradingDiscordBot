from selenium import webdriver
import time
import csv
from datetime import date
import pandas as pd


def start():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.set_window_size(1024, 768)

    driver.get("https://rl.insider.gg/pc/fennec")
    time.sleep(1)
    accept = driver.find_element_by_class_name("qc-cmp2-summary-buttons")
    accept.click()
    price = driver.find_element_by_id("itemSummaryPrice")
    name = driver.find_element_by_id("itemSummaryName")
    day = date.today()
    current_time = day.strftime("%d/%m/%Y")
    a = [[current_time, name.text, price.text]]
    with open("item.csv", "a", newline='\n') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(a)
    print(name.text, price.text)
    time.sleep(1)
    a = ["https://rl.insider.gg/fr/pc/zomba/white", "https://rl.insider.gg/fr/pc/octane/crimson",
         "https://rl.insider.gg/fr/pc/mainframe", "https://rl.insider.gg/fr/pc/interstellar"]
    n = -1
    while n != 3:
        n += 1
        driver.get(a[n])
        time.sleep(1)
        price1 = driver.find_element_by_id("itemSummaryPrice")
        name1 = driver.find_element_by_id("itemSummaryName")
        b = [[current_time, name1.text, price1.text]]
        with open("item.csv", "a", newline='\n') as file:
            csv_writerr = csv.writer(file)
            csv_writerr.writerows(b)
        print(name1.text, price1.text)


class Read:

    def __init__(self):
        df = pd.read_csv('item.csv', sep='[,-]', engine='python')
        Fennec = df[(df['Name'] == 'Fennec')]

        for ind, row in Fennec.iterrows():
            Fennec = ((row['Pricemax'] - 1100) / 1100) * 100
        self.Fennec = round(Fennec)
        Zomba = df[(df['Name'] == 'Zomba (Blanc titane)')]

        for ind, row in Zomba.iterrows():
            Zomba = ((row['Pricemax'] - 3400) / 3400) * 100
        self.Zomba = round(Zomba)
        Octane = df[(df['Name'] == 'Octane (Pourpre)')]

        for ind, row in Octane.iterrows():
            Octane = ((row['Pricemax'] - 3400) / 3400) * 100
        self.Octane = round(Octane)
        Mainframe = df[(df['Name'] == 'Ordinateur central')]

        for ind, row in Mainframe.iterrows():
            Mainframe = ((row['Pricemax'] - 1900) / 1900) * 100
        self.Mainframe = round(Mainframe)
        Interstellar = df[(df['Name'] == 'Interstellar')]

        for ind, row in Interstellar.iterrows():
            Interstellar = ((row['Pricemax'] - 1900) / 1900) * 100
        self.Interstellar = round(Interstellar)

        if Mainframe >= 0:
            self.mtext = "Le prix d'ordinateur central a augmenté ! C'est le moment de le vendre  mais pas de l'acheter! Il a un pourcentage de {}% " .format(round(Mainframe))
        else:
            self.mtext = "Le prix d'ordinateur central a baissé ! C'est le moment de le l'acheter  mais pas de le vendre! Il a un pourcentage de {}% " .format(round(Mainframe))

        if Fennec >= 0:
            self.ftext = "Le prix de la Fennec a augmenté ! C'est le moment de le vendre mais pas de l'acheter! Il a un pourcentage de {}% " .format(round(Fennec))

        else:
            self.ftext = "Le prix de la Fennec a baissé ! C'est le moment de le l'acheter mais pas de le vendre! Il a un pourcentage de {}% " .format(round(Fennec))

        if Zomba >= 0:
            self.ztext = "Le prix des Zombas TW a augmenté ! C'est le moment de le vendre mais pas de l'acheter! Il a un pourcentage de {}% " .format(round(Zomba))
        else:
            self.ztext = "Le prix des Zombas TW a baissé ! C'est le moment de le l'acheter mais pas de le vendre! Il a un pourcentage de {}% " .format(round(Zomba))
        if Octane >= 0:
            self.otext = "Le prix de la Octane Poupre a augmenté ! C'est le moment de le vendre mais pas de l'acheter! Il a un pourcentage de {}%"  .format(round(Octane))

        else:
            self.otext = "Le prix de la Octane Poupre a baissé ! C'est le moment de le l'acheter mais pas de le vendre! Il a un pourcentage de {}%  ".format(round(Octane))

        if Interstellar >= 0:
            self.itext = "Le prix d'interstellar a augmenté ! C'est le moment de le vendre mais pas de l'acheter! Il a un pourcentage de {}%  ".format(round(Interstellar))
        else:
            self.itext = "Le prix d'Interstellar a baissé ! C'est le moment de le l'acheter mais pas de le vendre! Il a un pourcentage de {}% " .format(round(Interstellar))

    def get_Fennec(self):
        return self.Fennec

    def get_Zomba(self):
        return self.Zomba

    def get_Octane(self):
        return self.Octane

    def get_Mainframe(self):
        return self.Mainframe

    def get_Interstellar(self):
        return self.Interstellar

    def get_mtext(self):
        return self.mtext

    def get_ftext(self):
        return self.ftext

    def get_ztext(self):
        return self.ztext

    def get_otext(self):
        return self.otext

    def get_itext(self):
        return self.itext



    # de = df.tail(5)
    # df.drop([0, 1, 2, 3, 4], 0, inplace=True)
    # print(df.head(5))
    # df['Pricemin'] = df['Pricemin'].astype(int)
    # df['Pricemax'] = df['Pricemax'].astype(int)
    # for m in df.itertuples():
    # Interstellare = df['Pricemax'].astype(int)
    # s = pd.Dataframe([m.rename(None)])
    # print(type(s))
    # row = next(df.iterrows())[Mainframe]
    # print(row)
    # m = ((Mainframe['Pricemax']) - (Mainframetwo['Pricemax']) / (Mainframe['Pricemax']))
    # print(Interstellar.tail(3)[['Day', 'Name', 'Pricemax']]) Interface graphqiue : cliquer sur fennec, pour voir lesp rix
    # print(df['Price'].Fennec)