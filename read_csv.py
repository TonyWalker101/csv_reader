#program will read and display the info associated with the "Process" selected

import csv
import sys

#search = parameters given either through arguments on file call or input
if len(sys.argv) >= 2:
  search = sys.argv[1:]
else:
  search = input("Which process are you looking for?\n").split(" ")

def process_search(item, row, answer):
  if item.upper() in row["Process"]:
    print({row["Process"]: {"Controller": row["Controller"], "Backup": row["Backup"], "ENV": row["ENV"]}})
    answer += {row["Process"]: {"Controller": row["Controller"], "Backup": row["Backup"], "ENV": row["ENV"]}} + "\n"
    return True
  return False

def csv_search(search):
  # answer = ""

  #for each item in search; open csv, find results, & print results
  for item in search:
    results = False
    
    with open("csv_test.csv") as raw_csv_data:
      csv_data = csv.DictReader(raw_csv_data)
      
      #loop instead of .get() as .csv may have variations of the search item (ex: 100A, 100B for search item = 100)
      for row in csv_data:
        if item.upper() in row["Process"]:
          print({row["Process"]: {"Controller": row["Controller"], "Backup": row["Backup"], "ENV": row["ENV"]}})
          results = True

    if not results:
      print(f"No results found for {item}")
      # answer += f"No results found for {search}" + "\n"
  
  return f"No results found for {item}"

#runs main function
csv_search(search)