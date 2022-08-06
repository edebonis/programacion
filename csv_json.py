import csv

with open('/home/esteban/Descargas/imdb_top_1000.csv', newline='') as csvfile:
     dreader = csv.DictReader(csvfile)
     lreader = csv.reader(csvfile)
     
     for row in lreader:
         print(row)
