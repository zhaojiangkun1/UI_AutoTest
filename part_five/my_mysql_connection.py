import pymysql
# 获取mySql的连接
db_connection = pymysql.Connect(
    host="localhost",
    user="admin",
    password="123456",
    database="python_ui",
    charset="utf8"
)
# 获取游标
cursor = db_connection.cursor()
# 书写Sql
sql = "insert into goods(id,name,description) " \
      "values (1,'手机','苹果手机')," \
      "(2,'衣服','是一件T恤衫')"
# 执行sql
cursor.execute(sql)
# 提交sql
db_connection.commit()
# 关闭游标
cursor.close()
# 关闭链接
db_connection.close()