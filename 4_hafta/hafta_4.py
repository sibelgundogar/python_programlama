#CSV DOSYALARIYLA ÇALIŞMA OKUMA VE YAZMA
import csv
with open('iris.data', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print (row)
print("--------------------------------------------------")



#yeni bir csv dosyası oluşturur ve verileri içine yazar
baslik = ["sicaklik", "nem", "basinc"]
veri = [[30,75.5,10], [32.3,5,50,3], [10.7,7,50,89]]
with open('sensor_veri.csv',
          'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)
print("--------------------------------------------------")


#pandas indirdik
import pandas as pd
veri = pd.read_csv("iris.data")

print(veri.head())
print (veri.columns)
"""  print (veri[3:5])
3 den 5 e kadar olanları getirir """
veri = veri.sort_values(by='sepal_length')
print(veri.head())

toplam_veri = veri["sepal_length"].sum()
ortalama_veri = veri["sepal_length"].mean()
ortanca_veri = veri["sepal_length"].median()
print("Sum: ", toplam_veri, "\nMean: ", ortalama_veri , "\nMedian: ", ortanca_veri)
print("--------------------------------------------------")



#SQLITE İLE ÇALIŞMA
import sqlite3
con = sqlite3.connect("a.vt")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS kitap "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayin_evi TEXT, "
               "sayfa_sayisi INT)")
con.commit()
con.close()

print("okey")
