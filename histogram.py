"""Takes one argument in the form positive_integer,higher_integer
Queries the tweetwordcount table in the tcount postgres database.
Returns words with counts betweeen these values (inclusive)"""
import sys
import psycopg2

#user entered the correct number of arguments
if len(sys.argv) == 2:

    #validate arguments as positive integers in increasing order
    ########################################################################
    #splits argument into list on comma
    argument = sys.argv[1]
    argument = argument.split(',')

    #exits if argument does not include exactly one comma
    if len(argument) != 2:
        print "\nIntegers in argument must be separated by a comma. Try again"
        sys.exit(0)

    #exits if argument does not contain only positive integers
    for integer in argument:
        if integer.isdigit() == False or integer == "0":
            print "\n", integer, "is not a positive integer"
            print "Please only enter positive integers. Try again"
            sys.exit(0)

    #converts arguments to integers in new list
    input_range = []
    for integer in argument:
        input_range.append(int(integer))

    #checks to make sure the integers are in increasing order
    if input_range[0] > input_range[1]:
        print "\nYour integer range is out of order"
        print "Please use the following format <positive_integer>,<higher_integer>"
        sys.exit(0)
    ###########################################################################

    conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT word, count from tweetwordcount order by word asc")
    records = cur.fetchall()
    no_results = 1
    for record in records:
        if (record[1] >= input_range[0]) and (record[1] <= input_range[1]):
            print record
	    if no_results == 1:
	        no_results = 0
    
    if no_results == 1:
	print "No words matched your query! Try again with a different range."		

    conn.commit()

    conn.close()
        
#user enterered zero arguments
elif len(sys.argv) == 1:
    print "\nYou entered no arguments"
    print "This function takes one argument in the format <positive_integer>,<higher_integer>"

#user entered more than one argument
else:
    print "\nYou entered more than one argument"
    print "This function takes one argument in the format <positive_integer>,<higher_integer>"
