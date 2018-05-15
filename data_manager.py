import util


@util.connection_handler
def get_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question;
                    """)
    questions = cursor.fetchall()
    return questions


@util.connection_handler
def add_question(cursor, new_title, new_message, time):
    cursor.execute("""
                    INSERT INTO question (title, message, submission_time)
                    VALUES (%(title)s, %(message)s, %(submission_time)s);
                    """,
                   {'title': new_title, 'message': new_message, 'submission_time': time})


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
def add_answer(cursor, new_id, new_message,time):
    cursor.execute("""
                    INSERT INTO answer (question_id, message, submission_time)
                    VALUES (%(question_id)s, %(message)s, %(submission_time)s);
                    """,
                   {'question_id': new_id, 'message': new_message, 'submission_time': time})


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
def delete_answer_by_question_id(cursor, question_id):
    cursor.execute("""
                    UPDATE question
                    SET title=%(title)s, message=%(message)s
                    WHERE id = %(id)s;
                    """, {'title': edited_title, 'message': edited_message, 'id': id})


@util.connection_handler
def registration(cursor, username, password, time):
    cursor.execute("""INSERT INTO users (user_name,password,registration_time) VALUES (%(user_name)s,%(password)s,%(registration_time)s);
                    """, {'user_name': username, 'password': password, 'registration_time': time})


@util.connection_handler
def check_usernames(cursor):
    cursor.execute("""SELECT user_name FROM users""")

    usernames = cursor.fetchall()
    return usernames
                    DELETE FROM answer
                    WHERE question_id = %(question_id)s;
                    """,
                   {'question_id': question_id})