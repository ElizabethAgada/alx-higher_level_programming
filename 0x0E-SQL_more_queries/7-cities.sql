-- Creates a database hbtn_0d_usa and a table cities in the database if not exists on my MySQL server.
-- creates database
CREATE IF NOT EXISTS hbtn_0d_usa;
-- use the created database
USE hbtn_0d_usa;
-- creates table
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id);

