import sqlite3

conn = sqlite3.connect('test.db')

# insert_sql = 'insert into company values(?, ?)'
# conn.execute(insert_sql, (100, 'LY'))
# conn.execute(insert_sql, (200, 'July'))
# conn.execute(insert_sql, (200, 'July'))
# conn.execute(insert_sql, (200, 'July'))
# conn.execute(insert_sql, (200, 'July'))
cursors = conn.execute('select id, emp_name from company')
for row in cursors:
    print(row[0], row[1])
#shwo_db = conn.execute('.tables')

conn.close()