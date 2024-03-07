-- creates a unique table states inside the database hbtn-0d_usa if it does not exist
-- creates database
CREATE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
-- creates the table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
