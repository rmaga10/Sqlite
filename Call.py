import database

# Lookup email record
database.email_lookup("Remymeow@up.com")

# Delete One record
database.delete_one('4')

# Add record
database.add_one("Rafael","Magalhaes","rafa.maga10@gmail.com")

# Adds Many records
lista = [
	("Remy","Lacroix","Remymeow@up.com"),
	("Lexi","Belle","Omglexi@up.com")		
	]
database.add_many(lista)

# Show All records
database.show_all()
