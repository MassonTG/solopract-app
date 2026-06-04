CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    description TEXT DEFAULT ''
);

INSERT INTO products (name, price, description) VALUES
    ('Laptop', 25999.99, 'MacBook Pro 14"'),
    ('Phone', 15499.00, 'iPhone 15 Pro'),
    ('Headphones', 2999.50, 'AirPods Pro 2');