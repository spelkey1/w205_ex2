MIDS w205 Exercise 2
Real Time Data Processing Using Apache Storm
Steve Pelkey

Instructions to run Storm Streamparse application that streams tweets, parses, counts word frequency, and stores tuples in a postgres database.

1) Create AWS instance using UCB MIDS W205 EX2-FULL AMI, download and install postgres
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh

2) Create a postgres database called 'tcount'
create database tcount;

3) Create a table titled 'tweetwordcount' with two columns (word, count) to store Twitter data from Storm
create table "Tweetwordcount"(word text primary key not null, count int not null);

4) Ensure psycopg2 and tweepy are installed for python
pip install psycopg2
pip install tweepy

5) Navigate to the Storm streamparse project folder called 'stweet_stuff_baby' and run.
cd stweet_stuff_baby
sparse run

6) Let application run for as long as you please

7) Two serving scripts are available to query the postgres database:
a) finalresults.py takes a word as an argument and returns the total number of word occurrences in stream. 
If you don't provide an argument, all words in stream will be returned.
python finalresults.py word
python finalresults.py

b) histogram.py returns the number of words that have counts in an inclusive range of integers.
Takes one argument in the form of two positive integers separated by a colon.
python histogram.py 3,5