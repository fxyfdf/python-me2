import sqlite3

conn = sqlite3.connect('test.db')
# create_sql = 'create table company(id int primary key not null, emp_name text not null);'
drop_table = 'drop table company'
create_sql = 'create table company(id int  , emp_name text );'
#conn.execute(drop_table)
# conn.execute(create_sql)
insert_sql = 'insert into company values(?, ?)'
conn.execute(insert_sql, (100, 'LY'))
conn.execute(insert_sql, (200, 'July'))
# cursors = conn.execute('select id, emp_name from company')
# for row in cursors:
#     print(row[0], row[1])
# #commit 之后才可以保存
# shwo_db = conn.execute('commit')
select_tables = conn.execute('select * from sqlite_master;')
#conn.close()