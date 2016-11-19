"""takes one word as argument, and lists its count in tweetwordcount table in tcount postgres database
if no arguments are given, will list entries in tables in alphabetical order with their count"""
import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount order by word asc")
records = cur.fetchall()

# if user enters in an argument
if len(sys.argv) == 2:
    selected_word = sys.argv[1]
    
    for record in records:
        if record[0] == selected_word:
            print "Total number of occurences of", record[0],":",record[1]
	    break
    else:
	print selected_word, "was not found! Try another word."

# if user does not enter in an argument
elif len(sys.argv) == 1:
    for record in records:
        print record, "\n"

# if more than one argument is entered
else:
    print "This function does not take more than one argument! Try again", "\n"
    print "Number of arguments =", len(sys.argv), "Arguments =",sys.argv
conn.commit()
conn.close()
