#program will read and display the info associated with the "Process" selected

import csv
import sys

results = False

if len(sys.argv) >= 2:
  search = sys.argv[1]
else:
  search = input("Which process are you looking for?\n")

def csv_search():
  with open("csv_test.csv") as raw_csv_data:
    csv_data = csv.DictReader(raw_csv_data)

    for row in csv_data:
      if row["Process"].find(search.upper()) != -1:
        print({row["Process"]: {"Controller": row["Controller"], "Backup": row["Backup"], "ENV": row["ENV"]}})
        results = True
        # break

    if not results:
      print(f"No results found for {search}")

csv_search()
# print(results)
# [print(dir(search))]