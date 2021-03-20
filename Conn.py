import sqlite3

# Create database
# conn = sqlite3.connect(':memory')
conn = sqlite3.connect('customer.db')

# Create table 
conn = sqlite3.connect('customer.db')
c = conn.cursor()
c.execute("""CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")
conn.commit()
conn.close()


# FUNCTIONS
# Query the DB and Return All Records
def show_all():
	# Create connection
	conn = sqlite3.connect('customer.db')
	# Create a cursor
	c = conn.cursor()
	# Query
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()
	for item in items:
		print(item)	
	# Commit our command
	conn.commit()
	# Close our connection
	conn.close()
	
# Add a new record to the table
def add_one(first,last,email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)",(first, last, email))
	conn.commit()
	conn.close()
	
# Delete record from table
def delete_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE FROM customers WHERE rowid = (?)", id)
	conn.commit()
	conn.close()

# Add many records to table
def add_many(list):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
	conn.commit()
	conn.close()

# Lookup with Where
def email_lookup(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT * FROM customers WHERE email = (?)", (email,))
	items = c.fetchall() 
	for item in items:
		print(item)	
	conn.commit()
	conn.close()
