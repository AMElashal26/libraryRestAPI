import pymysql
#conn = sqlite3.connect('books.sqlite')


conn = pymysql.connect(
    host='sql5.freesqldatabase.com',
    database='sql5695749',
    user='sql5695749',
    password='pDFv298reJ',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
sql_query = """CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
) """

#debug query below for primary key 
'''try:
    with connection.cursor() as cursor:
        # Drop the existing primary key
        cursor.execute("ALTER TABLE book DROP PRIMARY KEY;")
        
        # Modify the `id` column to be AUTO_INCREMENT PRIMARY KEY
        cursor.execute("ALTER TABLE book MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY;")
        
    # Commit the changes
    connection.commit()
    
    print("Primary key modified successfully.")
except pymysql.err.InternalError as e:
    print(f"An internal error occurred: {e}")
except pymysql.err.OperationalError as e:
    print(f"An operational error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    connection.close()'''



cursor.execute(sql_query) 
conn.close()