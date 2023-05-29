from db.postgres import run_sql_query, connect
from integration.opai import get_sql_query


def execute_query_and_show_results(query):
    sql_query = ''
    if not sql_query:
        db_connection = connect()
        result = get_sql_query(db_connection, query)

        sql_query = result.content
        print(sql_query)

        executed = run_sql_query(sql_query)
        if executed:
            print('Successfully Executed!')

        else:
            print('Error!')


if __name__ == '__main__':
    execute_query_and_show_results('add new student')

