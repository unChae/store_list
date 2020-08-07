import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='2289',
                       db='python', charset='utf8')
 
curs = conn.cursor()
sql = """insert into test(name,num)
         values (%s, %s)"""
curs.execute(sql, ('hong', 1))
curs.execute(sql, ('lee', 2))
conn.commit()
 
conn.close()