# csv_reader

Purpose built program to read from a specific csv file and return either the number of processes in the file (read_csv.py) or the controller attributed to the specific process (controller_search.py). 

## How to use read_csv.py

Run the program with CLI argument(s):

```
python3 read_csv.py 101 NGO200
```

...or without, in which case you'll be prompted to provide the process(es) to search for:

```
python3 read_csv.py 
Which process are you looking for?
101 NGO200
```

Results, or lack of results, will be printed to the console:

```
{'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}
No results found for NGO200
```
<br>

## How to use controller_search.py

Run the program with *one* CLI argument:

```
python3 controller_search.py tony
```

...or without, in which case you'll be prompted to provide the controller to search for:

```
python3 controller_search.py 
Which controller are you looking for?
tony
```

Results, or lack of results, will be printed to the console:

```
{'Tony': ['NGO101', 'NGO399'], 'Total Processes': 2}
```
Searching for string **all** will return all controllers in the csv file and their respective total processes:

```
Katie (Total=1): ['NGO542']
Tony (Total=2): ['NGO101', 'NGO399']
Bob (Total=1): ['NGO500']
```

