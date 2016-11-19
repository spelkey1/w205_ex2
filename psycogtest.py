import psycopg2
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("INSERT INTO test (word,count) VALUES (%s, %s)", ("e", 1))
conn.commit()

cur.execute("INSERT INTO test (word,count) VALUES (%s, %s)", ("f", 1))
conn.commit()

cur.execute("INSERT INTO test (word,count) VALUES (%s, %s)", ("g", 1))
conn.commit()

cur.execute("INSERT INTO test (word,count) VALUES (%s, %s)", ("h", 1))
conn.commit()

cur.execute("UPDATE test SET count=%s WHERE word=%s", (20,"Steve"))
conn.commit()

cur.execute("SELECT word, count from test")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()
