-- Step 1: Create necessary tables in the data warehouse


-- written by Channabasav Angadi

-- here i used dummy (means not used any key_id or any credeentials because of security issue in the production it can be replaced)

-- Create a table to store sales data here i used columns as per my convenience
CREATE TABLE sales (
    sale_id INT,
    product_id INT,
    market_id INT,
    price DECIMAL(10,2),
    quantity INT
);

-- Create a table to store market data  i used columns as per my convenience
CREATE TABLE markets (
    market_id INT,
    market_name VARCHAR(50),
    location VARCHAR(50)
);

-- Step 2: Load data into the data warehouse tables

-- Load sales data into the sales table
COPY sales FROM 's3://your-bucket/sales-data.csv'
    ACCESS_KEY_ID 'your-access-key'
    SECRET_ACCESS_KEY 'your-secret-access-key'
    CSV;

-- Load market data into the markets table
COPY markets FROM 's3://your-bucket/markets-data.csv'
    ACCESS_KEY_ID 'your-access-key'
    SECRET_ACCESS_KEY 'your-secret-access-key'
    CSV;

-- Step 3: Analyze pricing and market data

-- Determine average price by market
SELECT market_name, AVG(price) AS average_price
FROM sales s
JOIN markets m ON s.market_id = m.market_id
GROUP BY market_name;

-- Identify markets with higher-priced items
SELECT market_name
FROM sales s
JOIN markets m ON s.market_id = m.market_id
WHERE price > (SELECT AVG(price) FROM sales)
GROUP BY market_name;

-- Step 4: Analyze inventory allocation based on location

-- Determine inventory allocation by location
SELECT location, COUNT(DISTINCT product_id) AS inventory_allocation
FROM sales s
JOIN markets m ON s.market_id = m.market_id
GROUP BY location;


--Thank You
--Regards
--Channabasav Angadi
--9343406062