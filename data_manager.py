import util


@util.connection_handler
def get_question_and_title(cursor):
    cursor.execute("""
                    SELECT * FROM question;
                    """)
    questions = cursor.fetchall()
    return questions


@util.connection_handler
def get_answers(cursor, id):
    cursor.execute("""
                      SELECT * FROM answer
                      WHERE question_id = %(id)s;
                      """,
                   {'id': id})
    answers = cursor.fetchall()
    return answers


@util.connection_handler
def question_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE id = %(id)s;
                    """,
                   {'id': id})
    question = cursor.fetchall()
    return question


@util.connection_handler
def add_question(cursor, new_title, new_message, time):
    cursor.execute("""
                    INSERT INTO question (title, message, submission_time)
                    VALUES (%(title)s, %(message)s, %(submission_time)s);
                    """,
                   {'title': new_title, 'message': new_message, 'submission_time': time})


@util.connection_handler
def add_answer(cursor, new_id, new_message,time):
    cursor.execute("""
                    INSERT INTO answer (question_id, message, submission_time)
                    VALUES (%(question_id)s, %(message)s, %(submission_time)s);
                    """,
                   {'question_id': new_id, 'message': new_message, 'submission_time': time})


@util.connection_handler
def get_answer_by_id(cursor, id):
    cursor.execute("""SELECT * FROM answer
                    WHERE id = %(id)s;
                    """,
                   {'id': id})
    answer = cursor.fetchall()
    return answer


@util.connection_handler
def update_answer(cursor, id, message):
    cursor.execute("""UPDATE answer
                    SET message = %(message)s 
                    WHERE id = %(id)s;""",
                   {'id': id, 'message': message})


@util.connection_handler
def edit_question(cursor, edited_title, edited_message, id):
    cursor.execute("""
                    UPDATE question
                    SET title=%(title)s, message=%(message)s
                    WHERE id = %(id)s;
                    """,
                   {'title': edited_title, 'message': edited_message, 'id': id})

@util.connection_handler
def get_password(cursor, typed_user_name):
    cursor.execute("""
                    SELECT password
                    FROM users
                    WHERE user_name =%(user_name)s;
                    """,
                   {'user_name': typed_user_name})
    database_password = cursor.fetchall()

    return database_password


@util.connection_handler
def check_user(cursor):
    cursor.execute("""
                    SELECT *
                    FROM users;
                    """,)
    users = cursor.fetchall()

    return users


@util.connection_handler
def get_user_id(cursor, user_name):
    cursor.execute("""
                    SELECT id
                    FROM users
                    WHERE user_name=%(user_name)s;
                    """,
                   {'user_name': user_name})
    user_id = cursor.fetchall()

    return user_id


@util.connection_handler
def registration(cursor, username, password, time):
    cursor.execute("""INSERT INTO users (user_name,password,registration_time) VALUES (%(user_name)s,%(password)s,%(registration_time)s);
                    """, {'user_name': username, 'password': password, 'registration_time': time})


@util.connection_handler
def check_usernames(cursor):
    cursor.execute("""SELECT user_name FROM users""")

    usernames = cursor.fetchall()
    return usernames