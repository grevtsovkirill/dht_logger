import psycopg2
import datetime

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

#sensor text, reading text, value float, timestamp timestamp
def add_readings(sensor, reading, value, timestamp):
    query = """
    INSERT INTO
        DS18B20_local
    VALUES
        (%s, %s, %s, %s)
    """
    values = (sensor, reading, value, timestamp)
    cur.execute(query, values)
#dt = int(datetime.datetime.now().timestamp())
#print(dt)
#dt_object = datetime.datetime.fromtimestamp(dt)
#print("dt_object =", dt_object)
#add_readings('DS18B20', 'T', 18.75,  dt_object)    

def print_table():
    cur.execute('select * from DS18B20_local')
    results = cur.fetchall()       
    for result in results:
        print(result)
