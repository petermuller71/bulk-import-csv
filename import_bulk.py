import csv, sqlite3, time

start = time.time()

# create SQLITE file and create table
conn = sqlite3.connect("pc.sqlite")
curs = conn.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS PCFC (id INTEGER, type TEXT, term TEXT);")

# function to import csv and do bulk insert
def import_csv( csvfile ):
    to_db = []

    i = 0

    # important configuration ii:
    # ii is now set at 5. So 5 csv-rows are read and inserted
    # on my computer *3000 lines* gives fastest result
    # so... for huge csv files... change ii to other number
    ii = 5

    reader = csv.reader(open(csvfile, 'r'), delimiter='|')
    for row in reader:
        to_db = to_db + [(row[0], row[1], row[2])]
        i += 1

        # if ii is reached -> do bulk insert
        if i == ii:
            curs.executemany("INSERT INTO PCFC VALUES(?, ?, ?)", to_db)
            conn.commit()
            to_db = []
            i = 0

    # do last bulk insert if to_db is not empty
    if len(to_db) != 0:
        curs.executemany("INSERT INTO PCFC VALUES(?, ?, ?)", to_db)
        conn.commit()
        
    # end of function import_csv


# do the job...
csvfile = "PC.txt"
import_csv(csvfile)
print (csvfile + " done")


end = time.time()
print (end - start)
