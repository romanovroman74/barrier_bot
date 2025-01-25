import pymysql
import config

# Функция подключения к БД
def getConnection():
    try:
        connection = pymysql.connect(
            host=config.mysql_host,
            user=config.mysql_user,
            password=config.mysql_password,
            database=config.mysql_db,
            port=config.mysql_port,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print("Ошибка подключения к базе данных:", e)
        return None

# Проверка наличия пользователя в базе
def check_user_exists(user_id):
    connection = getConnection()
    if not connection:
        return False, "Ошибка подключения к базе данных"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            result = cursor.fetchone()
            return bool(result), None
    except Exception as e:
        return False, str(e)
    finally:
        connection.close()

# Добавление пользователя в базу
def add_user(user_id, phone_number, first_name, last_name):
    connection = getConnection()
    if not connection:
        return False, "Ошибка подключения к базе данных"
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO users (user_id, phone_number, first_name, last_name)
                VALUES (%s, %s, %s, %s)
            """, (user_id, phone_number, first_name, last_name))
            connection.commit()
            return True, None
    except Exception as e:
        return False, str(e)
    finally:
        connection.close()