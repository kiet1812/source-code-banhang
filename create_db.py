import sqlite3

database = sqlite3.connect("database.db")
cursor = database.cursor()
cursor.executescript("""
    -- Create Users table
CREATE TABLE Users (
    id INT PRIMARY KEY,
    fullname VARCHAR(100),
    address VARCHAR(100),
    phone_numbers VARCHAR(20),
    rank VARCHAR(20)
);

-- Insert 40 sample rows into Users
INSERT INTO Users (id, fullname, address, phone_numbers, rank) VALUES
(1, 'Alfreds Futterkiste', 'Berlin', '030-0074321', 'VIP'),
(2, 'Ana Trujillo', 'México D.F.', '555-232-1123', 'Member'),
(3, 'Antonio Moreno', 'México D.F.', '555-321-7645', 'Premium'),
(4, 'Thomas Hardy', 'London', '171-555-7788', 'VIP'),
(5, 'Christina Berglund', 'Luleå', '0921-12 34 65', 'Member'),
(6, 'Hanna Moos', 'Mannheim', '0621-08460', 'Premium'),
(7, 'Frédérique Citeaux', 'Strasbourg', '88.60.15.31', 'VIP'),
(8, 'Martín Sommer', 'Madrid', '91-555-22-82', 'Member'),
(9, 'Laurence Lebihan', 'Marseille', '91-555-33-44', 'Premium'),
(10, 'Elizabeth Lincoln', 'Tsawassen', '604-555-4729', 'VIP'),
(11, 'Victoria Ashworth', 'London', '171-555-1212', 'Member'),
(12, 'Patricio Simpson', 'Buenos Aires', '54-223-4567', 'VIP'),
(13, 'Francisco Chang', 'México D.F.', '555-666-7788', 'Member'),
(14, 'Yang Wang', 'Bern', '031-555-3456', 'Premium'),
(15, 'Pedro Afonso', 'Sao Paulo', '11-333-2222', 'VIP'),
(16, 'Elizabeth Brown', 'London', '171-555-8765', 'Premium'),
(17, 'Sven Ottlieb', 'Berlin', '030-1234567', 'Member'),
(18, 'Janine Labrune', 'Nantes', '40.67.88.88', 'VIP'),
(19, 'Ann Devon', 'London', '171-555-9988', 'Member'),
(20, 'Roland Mendel', 'Graz', '316-555-1234', 'Premium'),
(21, 'Aria Cruz', 'Lisbon', '351-1-1234567', 'VIP'),
(22, 'Diego Roel', 'Madrid', '91-123-4567', 'Member'),
(23, 'Lino Rodriguez', 'Barcelona', '93-555-4321', 'Premium'),
(24, 'Eduardo Saavedra', 'Sevilla', '95-555-6543', 'Member'),
(25, 'John Steel', 'London', '171-555-1122', 'VIP'),
(26, 'Georg Pipps', 'Salzburg', '662-555-9876', 'Member'),
(27, 'Isabel de Castro', 'Lisbon', '351-1-7654321', 'Premium'),
(28, 'Yoshi Tannamuri', 'Tokyo', '03-1234-5678', 'VIP'),
(29, 'Giovanni Rovelli', 'Bergamo', '035-123456', 'Member'),
(30, 'Catherine Dewey', 'Bruxelles', '02-555-7890', 'Premium'),
(31, 'Marie Bertrand', 'Paris', '01-2345-6789', 'VIP'),
(32, 'Helvetius Varga', 'Budapest', '1-555-3333', 'Member'),
(33, 'Paolo Accorti', 'Torino', '011-1234567', 'Premium'),
(34, 'Zbyszek Piestrzeniewicz', 'Warsaw', '22-555-9988', 'Member'),
(35, 'Carlos González', 'Madrid', '91-777-8888', 'VIP'),
(36, 'André Fonseca', 'Lisbon', '351-1-5559999', 'Premium'),
(37, 'Miguel Angel', 'Mexico City', '555-888-1212', 'Member'),
(38, 'Pascual Bueno', 'Barcelona', '93-111-2222', 'VIP'),
(39, 'Anabela Domingues', 'Lisbon', '351-1-7894561', 'Premium'),
(40, 'Stéphane Caron', 'Lille', '03-555-6677', 'Member');

-- Create Products table
CREATE TABLE Products (
    id INT PRIMARY KEY,
    nameProducts VARCHAR(100),
    price DECIMAL(10,2)
);

-- Insert 40 sample rows into Products
INSERT INTO Products (id, nameProducts, price) VALUES
(1, 'Chai', 18.00),
(2, 'Chang', 19.00),
(3, 'Aniseed Syrup', 10.00),
(4, 'Chef Anton''s Cajun Seasoning', 22.00),
(5, 'Chef Anton''s Gumbo Mix', 21.35),
(6, 'Grandma''s Boysenberry Spread', 25.00),
(7, 'Uncle Bob''s Organic Dried Pears', 30.00),
(8, 'Northwoods Cranberry Sauce', 40.00),
(9, 'Mishi Kobe Niku', 97.00),
(10, 'Ikura', 31.00),
(11, 'Queso Cabrales', 21.00),
(12, 'Queso Manchego La Pastora', 38.00),
(13, 'Konbu', 6.00),
(14, 'Tofu', 23.25),
(15, 'Genen Shouyu', 15.50),
(16, 'Pavlova', 17.45),
(17, 'Alice Mutton', 39.00),
(18, 'Carnarvon Tigers', 62.50),
(19, 'Teatime Chocolate Biscuits', 9.20),
(20, 'Sir Rodney''s Marmalade', 81.00),
(21, 'Sir Rodney''s Scones', 10.00),
(22, 'Gustaf''s Knäckebröd', 21.00),
(23, 'Tunnbröd', 9.00),
(24, 'Guaraná Fantástica', 4.50),
(25, 'NuNuCa Nuß-Nougat-Creme', 14.00),
(26, 'Gumbär Gummibärchen', 31.23),
(27, 'Schoggi Schokolade', 43.90),
(28, 'Rössle Sauerkraut', 45.60),
(29, 'Thüringer Rostbratwurst', 123.79),
(30, 'Nord-Ost Matjeshering', 25.89),
(31, 'Gorgonzola Telino', 12.50),
(32, 'Mascarpone Fabioli', 32.00),
(33, 'Geitost', 2.50),
(34, 'Sasquatch Ale', 14.00),
(35, 'Steeleye Stout', 18.00),
(36, 'Inlagd Sill', 19.00),
(37, 'Gravad lax', 26.00),
(38, 'Côte de Blaye', 263.50),
(39, 'Chartreuse verte', 18.00),
(40, 'Boston Crab Meat', 18.40);

""")