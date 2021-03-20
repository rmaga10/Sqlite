import sqlite3

# Query the DB and Return All Records
def show_all():
	# Criar conexão
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
