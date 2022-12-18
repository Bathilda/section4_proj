
import psycopg2

conn = psycopg2.connect(
    host="queenie.db.elephantsql.com",
    database="viqrzrqs",
    user="viqrzrqs",
    password="53-znZ3K1toPF74fnJAwAw4HWPb_fcx4")
print(conn)
cur = conn.cursor()
cur.execute("""CREATE TABLE test_table6 (
				name VARCHAR(32),
				age INT);
			""")
cur.execute("INSERT INTO test_table (name, age) VALUES ('spongebob', 12);")
name = 'banana'
age = 13
cur.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)",(name,age))
cur.execute("INSERT INTO test_table (name, age) VALUES ('patrick', 13);")
conn.commit()
breakpoint()
