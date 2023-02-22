#program will read and display the info associated with the "Process" selected

import csv
import sys

results = []

if len(sys.argv) >= 2:
  search = sys.argv[1]
else:
  search = input("Which process are you looking for?\n")

with open("csv_test.csv") as csv_test:
  data = csv.DictReader(csv_test)

  for row in data:
    if row["Process"].find(search.upper()) != -1:
      print({row["Process"]: {"Controller": row["Controller"], "Email": row["Email"]}})
      results.append({row["Process"]: {"Controller": row["Controller"], "Email": row["Email"]}})
      # break

  if not results:
    print(f"No results found for {search}")

# print(results)
# [print(dir(search))]