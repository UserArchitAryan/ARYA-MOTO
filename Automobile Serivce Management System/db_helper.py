import mysql.connector
from datetime import datetime

# Simple DB helper for ARYA-MOTO - uses mysql.connector

DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="sudosu",
    database="sysrec",
    port=3306,
)


def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        return conn, cursor
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
        return None, None


def ensure_tables():
    conn, cursor = connect_db()
    if not conn:
        return
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rec (
            CUSTOMER_ID INT AUTO_INCREMENT PRIMARY KEY,
            CUSTOMER_NAME VARCHAR(255),
            AGE VARCHAR(10),
            EMAIL VARCHAR(255) UNIQUE,
            PHONE VARCHAR(50),
            ADDRESS TEXT,
            PASSWORD VARCHAR(255)
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            VEHICLE_ID INT AUTO_INCREMENT PRIMARY KEY,
            CUSTOMER_ID INT,
            BRAND VARCHAR(100),
            MODEL VARCHAR(100),
            YEAR VARCHAR(10),
            FOREIGN KEY (CUSTOMER_ID) REFERENCES rec(CUSTOMER_ID)
                ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            SERVICE_ID INT AUTO_INCREMENT PRIMARY KEY,
            CUSTOMER_ID INT,
            VEHICLE_ID INT,
            SERVICE_DESC TEXT,
            SERVICE_DATE DATETIME,
            FOREIGN KEY (CUSTOMER_ID) REFERENCES rec(CUSTOMER_ID) ON DELETE CASCADE,
            FOREIGN KEY (VEHICLE_ID) REFERENCES vehicles(VEHICLE_ID) ON DELETE CASCADE
        ) ENGINE=InnoDB;
        """)
        conn.commit()
    except mysql.connector.Error as err:
        print("Error ensuring tables:", err)
    finally:
        cursor.close()
        conn.close()


def insert_user(name, age, email, phone, address, password):
    conn, cursor = connect_db()
    if not conn:
        return None
    try:
        query = """
        INSERT INTO rec (CUSTOMER_NAME, AGE, EMAIL, PHONE, ADDRESS, PASSWORD)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, age, email, phone, address, password))
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print("Failed to insert user:", err)
        return None
    finally:
        cursor.close()
        conn.close()


def get_user_by_email_password(email, password):
    conn, cursor = connect_db()
    if not conn:
        return None
    try:
        query = "SELECT * FROM rec WHERE EMAIL = %s AND PASSWORD = %s"
        cursor.execute(query, (email, password))
        row = cursor.fetchone()
        return row
    except mysql.connector.Error as err:
        print("Failed to query user:", err)
        return None
    finally:
        cursor.close()
        conn.close()


def get_user_by_name_password(name, password):
    """Authenticate by CUSTOMER_NAME and PASSWORD (convenience for tests)."""
    conn, cursor = connect_db()
    if not conn:
        return None
    try:
        query = "SELECT * FROM rec WHERE CUSTOMER_NAME = %s AND PASSWORD = %s"
        cursor.execute(query, (name, password))
        row = cursor.fetchone()
        return row
    except mysql.connector.Error as err:
        print("Failed to query user by name:", err)
        return None
    finally:
        cursor.close()
        conn.close()


def insert_vehicle(customer_id, brand, model, year):
    conn, cursor = connect_db()
    if not conn:
        return None
    try:
        query = "INSERT INTO vehicles (CUSTOMER_ID, BRAND, MODEL, YEAR) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (customer_id, brand, model, year))
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print("Failed to insert vehicle:", err)
        return None
    finally:
        cursor.close()
        conn.close()


def get_vehicles_for_customer(customer_id):
    conn, cursor = connect_db()
    if not conn:
        return []
    try:
        query = "SELECT * FROM vehicles WHERE CUSTOMER_ID = %s"
        cursor.execute(query, (customer_id,))
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print("Failed to fetch vehicles:", err)
        return []
    finally:
        cursor.close()
        conn.close()


def insert_service(customer_id, vehicle_id, service_desc, service_date=None):
    conn, cursor = connect_db()
    if not conn:
        return None
    try:
        if service_date is None:
            service_date = datetime.now()
        query = "INSERT INTO services (CUSTOMER_ID, VEHICLE_ID, SERVICE_DESC, SERVICE_DATE) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (customer_id, vehicle_id, service_desc, service_date))
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print("Failed to insert service:", err)
        return None
    finally:
        cursor.close()
        conn.close()


def get_services_for_customer(customer_id):
    conn, cursor = connect_db()
    if not conn:
        return []
    try:
        query = "SELECT s.*, v.BRAND, v.MODEL FROM services s LEFT JOIN vehicles v ON s.VEHICLE_ID = v.VEHICLE_ID WHERE s.CUSTOMER_ID = %s ORDER BY s.SERVICE_DATE DESC"
        cursor.execute(query, (customer_id,))
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print("Failed to fetch services:", err)
        return []
    finally:
        cursor.close()
        conn.close()
