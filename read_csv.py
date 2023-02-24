#program will read and display the info associated with the "Process" selected

import csv
import sys


if len(sys.argv) >= 2:
  search = sys.argv[1:]
else:
  search = input("Which process are you looking for?\n").split(" ")

def csv_search(search):
  with open("csv_test.csv") as raw_csv_data:
    csv_data = csv.DictReader(raw_csv_data)

    for item in search:
      results = False
      for row in csv_data:
        if item.upper() in row["Process"]:
          print({row["Process"]: {"Controller": row["Controller"], "Backup": row["Backup"], "ENV": row["ENV"]}})
          results = True
          # break

      if not results:
        print(f"No results found for {item}")

csv_search(search)
# print(results)
# [print(dir(search))]