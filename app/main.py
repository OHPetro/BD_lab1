# import time
import psycopg2
# import pandas as pd




# # Database connection details
# db_name = 'DB_lab_1'
# db_user = 'postgres'
# db_pass = '2509'
# # db_host = 'localhost'
# db_host = 'db'
# db_port = '5433'


# print("before pd.read_csv('./files/Odata2021File.csv', delimiter = ';', encoding='utf8', nrows=1)")
# df = pd.read_csv('./files/Odata2021File.csv', delimiter = ';', encoding='utf8', nrows=1)
# print(df)
# df = df.astype(str)

# # Table name and column names
# table_name = 'data'
# col_names_data = df.columns.tolist()

# # Unique constraint columns
# unique_col = 'OUTID' # Unique constraint

# def drop_table(conn):
#     cur = conn.cursor()
#     drop_table_query = f"DROP TABLE IF EXISTS data" 
#     cur.execute(drop_table_query)  
#     conn.commit()

# def create_table(conn):
#     """Create table if not exists"""
#     cur = conn.cursor()


#     table_columns = ', '.join(f"{col} TEXT" for col in col_names_data)
#     create_table_query = f"CREATE TABLE IF NOT EXISTS data ({table_columns})" + ";"

#     cur.execute(create_table_query)  
#     conn.commit()

# def add_unique_constraint(conn):
#     """Add unique constraint to table"""
#     cur = conn.cursor()
#     cur.execute(f"ALTER TABLE {table_name} ADD CONSTRAINT unique_constraint UNIQUE ({unique_col})")
#     conn.commit()

# def insert_data(conn, filename):
#     """Insert data from CSV file into table"""
#     filename = '../files/' + filename
#     i = 0 #
#     cur = conn.cursor()
#     col_names = None
#     batch_size = 200
#     try:
#         for chunk in pd.read_csv(filename, delimiter=';', encoding='utf8', chunksize=batch_size):
#             chunk = chunk.astype(str)
#             if col_names is None:
#                 col_names = chunk.columns.tolist()
#             rows = chunk.values.tolist()
#             cur.executemany("INSERT INTO data ({}) VALUES ({}) ON CONFLICT DO NOTHING".format(
#                 ', '.join(col_names), ', '.join(['%s']*len(col_names))), rows)
#             i = i + batch_size #
#             if i > 1000:
#                 break
#             print(str(i) + " rows inserted")
#             conn.commit()
#     except psycopg2.Error as e:
#         conn.rollback()
#         print("Error:", e)
#     finally:
#         cur.close()


# def write_sql_query_to_csv(query, csv_filename, conn):

#     # Execute SQL query and read results into pandas DataFrame
#     df = pd.read_sql(query, conn)

#     # Write DataFrame to CSV file
#     df.to_csv('./files/' + csv_filename, index=False)

#     # Close database connection
#     conn.close()

# while True:
#     try:
#         # Connect to database
#         print("before conn = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)")
#         conn = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)
#         print("conected to db")

#         # Create table and add unique constraint
#         print("before drop_table(conn)")
#         drop_table(conn)
#         print("before create_table(conn)")
#         create_table(conn)
#         add_unique_constraint(conn)

#         # Insert data from CSV files
       
#         # insert_data(conn, 'Odata2020File.csv')
#         insert_data(conn, 'Odata2021File.csv')

#         query = "SELECT * FROM data WHERE mathPTRegName = 'м.Київ'"
#         csv_filename = "query_results.csv"

#         write_sql_query_to_csv(query, 'result.csv', conn)


#         # Close database connection
#         conn.close()

#         # Exit loop if successful
#         break

#     except psycopg2.OperationalError:
#         # Connection lost, retry in 5 seconds
#         print("Connection lost. Retrying in 5 seconds...")
#         time.sleep(5)

# time.sleep(100)
# print("All good!")

db_name = 'DB_lab_1'
db_user = 'postgres'
db_pass = '2509'
db_host = 'db'
db_port = '5432'
conn = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)
