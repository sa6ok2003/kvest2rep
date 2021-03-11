import sqlite3

def reg_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        status_ref
        ) """)
    db.commit()
    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?)", (id, 1))
        db.commit()

def stata_user():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    status = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    return status