import mysql.connector

config = {
    'user': 'Guhan',
    'password': 'Air@123456789#',
    'host': '54.81.251.156',  # Public IP address of the MySQL server
    'database':"car"
}

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
)
"""
sample_data = [
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Mike', 'Johnson', 'mike.johnson@example.com')
]

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(create_table_query)

    for data in sample_data:
        cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)", data)

    conn.commit()
    cursor.close()
    conn.close()
    print("Sample data inserted successfully.")

except mysql.connector.Error as err:
    print("Error:", err)
