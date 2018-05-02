import util


@util.connection_handler
def get_question_and_title(cursor):
    cursor.execute("""
                    SELECT * FROM question;
                    """)
    questions = cursor.fetchall()
    return questions


@util.connection_handler
def add_question(cursor, new_title, new_message):
    cursor.execute("""
                    INSERT INTO question (title, message) VALUES (%(title)s, %(message)s);
                    """, {'title': new_title, 'message': new_message})


@util.connection_handler
def add_answer(cursor, new_id, new_message):
    cursor.execute("""
                    INSERT INTO answer (question_id, message) VALUES (%(question_id)s, %(message)s);
                    """, {'question_id': new_id, 'message': new_message})


