#program will read and display the info associated with the "Process" selected

import csv
import sys

#search = parameters given either through arguments on file call or input
if len(sys.argv) >= 2:
  search = sys.argv[1:]
else:
  search = input("Which process are you looking for?\n").split(" ")

def csv_search(search):

  #for each item in search; open csv, find results, & print results
  for item in search:
    results = False
    
    with open("csv_test.csv") as raw_csv_data:
      csv_data = csv.DictReader(raw_csv_data)
      
      for row in csv_data:
        if item.upper() in row["Process"]:
          print({row["Process"]: {"Controller": row["Controller"], "Backup": row["Backup"], "ENV": row["ENV"]}})
          results = True

    if not results:
      print(f"No results found for {item}")

#runs main function
csv_search(search)