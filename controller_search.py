#program will read and display the "Controllers" column from the csv file
import csv
import sys

results = {}
name = ""
processes_list = []

if len(sys.argv) >= 2:
  search = " ".join(name for name in sys.argv[1:]).lower().title()
else:
  search = input("Which controller are you looking for?\n").lower().title()

if not search == "All":
  with open("csv_test.csv") as raw_csv_data:
    csv_data = csv.DictReader(raw_csv_data)

    for row in csv_data:
      if row["Controller"].lower().title().find(search) != -1:
        name = row["Controller"]
        processes_list.append(row["Process"])
        # break
    
    results[name] = processes_list
    results["Total Processes"] = len(processes_list)

    if results[name]:
      print(results)
    else:
      print(f"No processes found for {search}")
else:
  with open("csv_test.csv") as raw_csv_data:
    csv_data = csv.DictReader(raw_csv_data)

    for row in csv_data:
      if row["Controller"] not in results:
        results[row["Controller"]] = []
        results[row["Controller"]].append(row["Process"])
      else:
       results[row["Controller"]].append(row["Process"])
    
    for controller, processes in results.items():
      print(f"{controller} (Total={len(processes)}): {processes}")

# print(results)
# [print(dir(search))]