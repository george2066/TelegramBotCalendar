import psycopg2 as pg
from telegrambotcalendar.secrets import HOST, DATABASE, USER, PASSWORD

connection = pg.connect(
    host=HOST,
    database=DATABASE,
    user=USER,
    password=PASSWORD
)

create_events = '''
CREATE TABLE events (
    id serial PRIMARY KEY,
    user_id INT NOT NULL,
    name text NOT NULL,
    date date NOT NULL,
    time time NOT NULL
);
'''

cursor = connection.cursor()

cursor.execute("select * from information_schema.tables where table_name=\'events\'")

if not bool(cursor.rowcount):
    cursor.execute(create_events)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")


insert = lambda user_id, event_name, event_text, event_date, event_time: f'insert into events (user_id, name, text, date, time) value(\'{user_id}\', \'{event_name}\', \'{event_text}\', \'{event_date}\', \'{event_time}\')'

def create_event(user_id, event_name, event_text):
    cursor.execute()

