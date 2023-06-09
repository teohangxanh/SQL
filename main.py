import sqlite3

conn = sqlite3.connect('SQLite_Python.db')

# Create a cursor
cur = conn.cursor()

# Create tables
cur.execute('''CREATE TABLE IF NOT EXISTS Manufacturers (
  Code INTEGER,
  Name VARCHAR(255) NOT NULL,
  PRIMARY KEY (Code))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Products (
  Code INTEGER,
  Name VARCHAR(255) NOT NULL ,
  Price DECIMAL NOT NULL ,
  Manufacturer INTEGER NOT NULL,
  PRIMARY KEY (Code), 
  FOREIGN KEY (Manufacturer) REFERENCES Manufacturers(Code))''')

# # Execute the SQL statements to insert the data
# cur.execute("INSERT INTO Manufacturers(Code,Name) VALUES(1,'Sony');")
# cur.execute("INSERT INTO Manufacturers(Code,Name) VALUES(2,'Creative Labs');")
# cur.execute("INSERT INTO Manufacturers(Code,Name) VALUES(3,'Hewlett-Packard');")
# cur.execute("INSERT INTO Manufacturers(Code,Name) VALUES(4,'Iomega');")
# cur.execute("INSERT INTO Manufacturers(Code,Name) VALUES(5,'Fujitsu');")
# cur.execute("INSERT INTO Manufacturers(Code,Name) VALUES(6,'Winchester');")
#
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(1,'Hard drive',240,5);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(2,'Memory',120,6);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(3,'ZIP drive',150,4);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(4,'Floppy disk',5,6);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(5,'Monitor',240,1);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(6,'DVD drive',180,2);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(7,'CD drive',90,2);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(8,'Printer',270,3);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(9,'Toner cartridge',66,3);")
# cur.execute("INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(10,'DVD burner',180,2);")

# Commit our command

# Query the database
# -- 1.1 Select the names of all the products in the store.
# -- 1.2 Select the names and the prices of all the products in the store.
# -- 1.3 Select the name of the products with a price less than or equal to $200.
# -- 1.4 Select all the products with a price between $60 and $120.
# -- 1.5 Select the name and price in cents (i.e., the price must be multiplied by 100).
# -- 1.6 Compute the average price of all the products.
# -- 1.7 Compute the average price of all products with manufacturer code equal to 2.
# -- 1.8 Compute the number of products with a price larger than or equal to $180.
# -- 1.9 Select the name and price of all products with a price larger than or equal to $180, and sort first by price (in descending order), and then by name (in ascending order).
# -- 1.10 Select all the data from the products, including all the data for each product's manufacturer.
# -- 1.11 Select the product name, price, and manufacturer name of all the products.
# -- 1.12 Select the average price of each manufacturer's products, showing only the manufacturer's code.
# -- 1.13 Select the average price of each manufacturer's products, showing the manufacturer's name.
# -- 1.14 Select the names of manufacturer whose products have an average price larger than or equal to $150.
# -- 1.15 Select the name and price of the cheapest product.
# -- 1.16 Select the name of each manufacturer along with the name and price of its most expensive product.
# -- 1.17 Add a new product: Loudspeakers, $70, manufacturer 2.
# -- 1.18 Update the name of product 8 to "Laser Printer".
# -- 1.19 Apply a 10% discount to all products.
# -- 1.20 Apply a 10% discount to all products with a price larger than or equal to $120.
cur.execute()
items = c.fetchall()
for item in items:
    print(*item, sep = '\t')

conn.commit()
# Close our connection
conn.close()
