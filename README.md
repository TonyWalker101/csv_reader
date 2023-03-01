# csv_reader

Purpose built program to read from a specific csv file and return either the number of processes in the file (read_csv.py) or the controller attributed to the specific process (controller_search.py). 

## How to use read_csv.py

Run the program with CLI argument(s):

```
  python3 read_csv.py NGO101 NGO200
```

...or without, in which case you'll be prompted to provide the process(es) to search for:

```
  python3 read_csv.py 
  Which process are you looking for?
  NGO101 NGO200
```

Results, or lack of results, will be printed to the console:

```
{'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}
No results found for 200
```
## How to use controller_search.py

Run the program with 1 CLI argument:

```
  python3 controller_search.py tony
```

...or without, in which case you'll be prompted to provide the process(es) to search for:

```
  python3 controller_search.py 
  Which controller are you looking for?
  NGO101 NGO200
```

Results, or lack of results, will be printed to the console:

```
{'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}
No results found for 200
```


