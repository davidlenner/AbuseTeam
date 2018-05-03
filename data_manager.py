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
                    INSERT INTO question (title, message, submission_time) VALUES (%(title)s, %(message)s, %(submission_time)s);
                    """, {'title': new_title, 'message': new_message, 'submission_time': time})


@util.connection_handler
def add_answer(cursor, new_id, new_message,time):
    cursor.execute("""
                    INSERT INTO answer (question_id, message, submission_time) VALUES (%(question_id)s, %(message)s, %(submission_time)s);
                    """, {'question_id': new_id, 'message': new_message, 'submission_time': time})


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
                    """, {'title': edited_title, 'message': edited_message, 'id': id})
