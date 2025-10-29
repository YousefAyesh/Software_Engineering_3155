import pymysql
from api.dependencies.config import conf

# Test: Connect without specifying database and list all databases
try:
    connection = pymysql.connect(
        host=conf.host,
        user=conf.user,
        password=conf.password,
        port=conf.port
    )
    print("✅ Connected to MySQL server!")

    # Now try to see all databases
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES;")
    databases = cursor.fetchall()
    print("\nAvailable databases:")
    for db in databases:
        print(f"  - {db[0]}")

    connection.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")