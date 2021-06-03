import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_11")

connection = cx_Oracle.connect(user="admin", password="Pgy3121.2021", dsn="pgy3121_high")
