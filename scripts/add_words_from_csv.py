import csv
from words.models import Word

line = 0 
with open('./scripts/5000.txt', newline='', encoding='latin-1') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])

        Word.objects.create(word=row[0],usage_order=line)
        line += 1


