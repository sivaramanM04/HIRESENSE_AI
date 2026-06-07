import sqlite3
import json
import os



DB_PATH = "database/hiresense.db"




# ==================================================
# CONNECTION
# ==================================================

def connect():


    os.makedirs(
        "database",
        exist_ok=True
    )


    return sqlite3.connect(
        DB_PATH
    )








# ==================================================
# INIT DATABASE
# ==================================================

def init_db():


    conn = connect()

    cursor = conn.cursor()



    # USERS

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            email TEXT UNIQUE,

            password TEXT

        )
        """
    )





    # INTERVIEW HISTORY

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            module TEXT,

            role TEXT,

            score TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )





    # CHAT SESSIONS

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_email TEXT,

            title TEXT,

            data TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )



    conn.commit()

    conn.close()









# ==================================================
# AUTH
# ==================================================

def create_user(
    name,
    email,
    password
):


    conn = connect()

    cursor = conn.cursor()



    try:


        cursor.execute(
            """
            INSERT INTO users
            (
            name,
            email,
            password
            )

            VALUES
            (?,?,?)

            """,
            (
                name,
                email,
                password
            )
        )


        conn.commit()


        return True



    except sqlite3.IntegrityError:


        return False



    finally:


        conn.close()









def login_user(
    email,
    password
):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *

        FROM users

        WHERE email=?
        AND password=?
        """,
        (
            email,
            password
        )
    )



    user = cursor.fetchone()


    conn.close()


    return user












# ==================================================
# INTERVIEW HISTORY
# ==================================================

def save_history(
    module,
    role,
    score
):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO history
        (
        module,
        role,
        score
        )

        VALUES
        (?,?,?)
        """,
        (
            module,
            role,
            str(score)
        )
    )



    conn.commit()

    conn.close()









def get_history():


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *

        FROM history

        ORDER BY id DESC
        """
    )


    data = cursor.fetchall()


    conn.close()


    return data












# ==================================================
# CHAT SESSIONS
# ==================================================

def save_session(
    title,
    data,
    user_email=None
):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO sessions
        (
        user_email,
        title,
        data
        )

        VALUES
        (?,?,?)

        """,
        (
            user_email,
            title,
            json.dumps(data)
        )
    )



    conn.commit()


    conn.close()










def get_sessions(
    user_email=None
):


    conn = connect()

    cursor = conn.cursor()



    if user_email:


        cursor.execute(
            """
            SELECT
            id,
            title

            FROM sessions

            WHERE user_email=?

            ORDER BY id DESC
            """,
            (
                user_email,
            )
        )



    else:


        cursor.execute(
            """
            SELECT
            id,
            title

            FROM sessions

            ORDER BY id DESC
            """
        )




    data = cursor.fetchall()



    conn.close()



    return data










def load_session(
    session_id
):


    conn = connect()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT data

        FROM sessions

        WHERE id=?
        """,
        (
            session_id,
        )
    )




    row = cursor.fetchone()



    conn.close()




    if row:


        try:


            return json.loads(
                row[0]
            )


        except:


            return {}



    return {}