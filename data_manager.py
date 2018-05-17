import util


@util.connection_handler
def get_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question;
                    """)
    questions = cursor.fetchall()

    return questions


@util.connection_handler
def get_question_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE id = %(id)s;
                    """,
                   {'id': id})
    question = cursor.fetchall()

    return question


@util.connection_handler
def search_question(cursor, search_phrase):
    cursor.execute("""
                    SELECT * FROM question
                    WHERE (title LIKE %(searched_phrase)s OR message LIKE %(searched_phrase)s);
                    """,
                   {'searched_phrase': '%' + search_phrase + '%'})
    searched_questions = cursor.fetchall()

    return searched_questions


@util.connection_handler
def add_question(cursor, new_title, new_message, time, user_id):
    cursor.execute("""
                    INSERT INTO question (title, message, submission_time, user_id)
                    VALUES (%(title)s, %(message)s, %(submission_time)s, %(user_id)s);
                    """,
                   {'title': new_title, 'message': new_message, 'submission_time': time, 'user_id': user_id})


@util.connection_handler
def edit_question(cursor, edited_title, edited_message, id):
    cursor.execute("""
                    UPDATE question
                    SET title=%(title)s, message=%(message)s
                    WHERE id = %(id)s;
                    """,
                   {'title': edited_title, 'message': edited_message, 'id': id})


@util.connection_handler
def delete_question(cursor, id):
    cursor.execute("""
                    DELETE FROM question
                    WHERE id = %(id)s;
                    """,
                   {'id': id})


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
def add_answer(cursor, new_id, new_message, time, user_id):
    cursor.execute("""
                    INSERT INTO answer (question_id, message, submission_time, user_id)
                    VALUES (%(question_id)s, %(message)s, %(submission_time)s, %(user_id)s);
                    """,
                   {'question_id': new_id, 'message': new_message, 'submission_time': time, 'user_id': user_id})


@util.connection_handler
def get_answer_by_id(cursor, id):
    cursor.execute("""
                    SELECT * FROM answer
                    WHERE id = %(id)s;
                    """,
                   {'id': id})
    answer = cursor.fetchall()
    return answer


@util.connection_handler
def edit_answer(cursor, id, message):
    cursor.execute("""
                    UPDATE answer
                    SET message = %(message)s 
                    WHERE id = %(id)s;""",
                   {'id': id, 'message': message})


@util.connection_handler
def delete_answer(cursor, id):
    cursor.execute("""
                    DELETE FROM answer
                    WHERE id = %(id)s
                    """,
                   {'id': id})


@util.connection_handler
def delete_answer_by_question_id(cursor, question_id):
    cursor.execute("""
                        DELETE FROM answer
                        WHERE question_id = %(question_id)s
                        """,
                        {'question_id': question_id})


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
def get_user_id_and_name(cursor, user_name):
    cursor.execute("""
                    SELECT id, user_name
                    FROM users
                    WHERE user_name=%(user_name)s;
                    """,
                   {'user_name': user_name})
    user_id_and_name = cursor.fetchall()

    return user_id_and_name


@util.connection_handler
def registration(cursor, username, password, time):
    cursor.execute("""INSERT INTO users (user_name,password,registration_time) VALUES (%(user_name)s,%(password)s,%(registration_time)s);
                    """, {'user_name': username, 'password': password, 'registration_time': time})


@util.connection_handler
def get_user_questions(cursor, user_id):
    cursor.execute("""
                    SELECT title, message
                    FROM question
                    WHERE user_id=%(user_id)s;
                    """,
                    {'user_id': user_id})
    questions = cursor.fetchall()

    return questions


@util.connection_handler
def get_user_answers(cursor, user_id):
    cursor.execute("""
                    SELECT message
                    FROM answer
                    WHERE user_id=%(user_id)s;
                    """,
                   {'user_id': user_id})
    answers = cursor.fetchall()

    return answers


@util.connection_handler
def get_username(cursor, user_id):
    cursor.execute("""
                    SELECT user_name
                    FROM USERS
                    WHERE user_id=%(user_id);
                    """,
                   {'user_id': user_id})
    user_name = cursor.fetchall()

    return user_name

