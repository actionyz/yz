import sqlite3  
conn = sqlite3.connect("db.sqlite3")  
print 'Opened database successfully'   
sql = "select * from victim"  
re = conn.execute(sql)
for i in re:
	print i[0]
