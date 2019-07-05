import pymysql


def save_goods_info_to_mysql(info_list):
    try:
        db_connection = get_connection()
        cursor = db_connection.cursor()
        for info in info_list:
            for key, value in info.items():
                sql = "insert into goods(name,description) " \
                      "values (\"%s\",\"%s\")" % (key, value)
                print(sql)
                cursor.execute(sql)
                db_connection.commit()
        # sql = "insert into goods(name,description) values ('电脑','苹果电脑')"
        # print(sql)
        # cursor.execute(sql)
        # db_connection.commit()
    finally:
        close_db(db_connection, cursor)


def get_connection():
    db_connection = pymysql.Connect(
        host="localhost",
        user="admin",
        password="123456",
        database="python_ui",
        charset="utf8"
    )
    return db_connection


def close_db(db_connection, cursor):
    cursor.close()
    db_connection.close()


# if __name__ == "__main__":
#     save_goods_info_to_mysql()
