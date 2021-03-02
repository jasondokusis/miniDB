from database import Database
import os
# create db with name "smdb"
db = Database('vsmdb', load=False)
# create a single table named "classroom"
db.create_table('classroom', ['building', 'room_number', 'capacity'], [str, str,int])

# insert 5 rows
db.insert('classroom', ['Packard', '101', '500'])
db.insert('classroom', ['Painter', '514', '10'])
db.insert('classroom', ['Taylor', '3128', '70'])
db.insert('classroom', ['Watson', '100', '30'])
db.insert('classroom', ['Watson', '120', '50'])

db.update('classroom', 10, 'capacity', 'capacity <= 30')

db.delete('classroom', 'capacity <= 10')

db.drop_table('test')
db.create_table('test', ['capacity', 'capacity1', 'capacity2'], [int, int, int], 'capacity')
db.insert('test', ['501', '502', '503'])
db.insert('classroom', ['Painter', '100', '1'])

print(db.classroom.column_types)

db.classroom.show()

print(db.top)
#db.change_max_rollback(7)




