import util


@util.connection_handler
def get_question_and_title(cursor):
    cursor.execute("""
                    SELECT id, title, message FROM question
                    """)
    questions = cursor.fetchall()
    return questions


