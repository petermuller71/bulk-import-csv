bulk-import-csv
===============

bulk import large CSV into SQL(ite) 

This code can be used to read a CSV file and import the contents in a database (in this example sqlite).

The example csv file has 3 columns and | as a seperator

CSV rows are inserted by blocks of ii rows.
In the example ii is set to 5
On my machine 3000 was fastest.
So ii should be changed to 3000

1 milion rows can be inserted in 30 sec.
(icore 7, ssd's and 16G memory)

