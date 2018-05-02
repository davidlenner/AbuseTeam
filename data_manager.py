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


