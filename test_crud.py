import psycopg2
import config

def test_delete():
    try :
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("delete from pet where name='성탄이'")

    except Exception as e:
        print(f'error : {e}')
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())

def test_select():
    try :
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("select * from pet")
        records = cursor.fetchall()

        for record in records:
            print(record, type(record))

    except Exception as e:
        print(f'error : {e}')
    finally:
        cursor and cursor.close()
        conn and conn.close()

def test_insert():
    try :
        conn = psycopg2.connect(**config.db)

        cursor = conn.cursor()
        cursor.execute("insert into pet values('성탄이', '정은이', 'dog', 'm', '2019-06-19')")

    except Exception as e:
        print(f'error : {e}')
    finally:
        cursor and cursor.close()
        conn and (conn.commit() or conn.close())


def main():
    test_insert()
    test_select()
    print("=========================")
    test_delete()
    test_select()
    print("=========================")
    # test_update()
    # test_select()

__name__ == '__main__' and main()
