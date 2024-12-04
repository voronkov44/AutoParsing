import mysql.connector
from datetime import datetime, timedelta
from database import connect_db, close_db



def check_upcoming_games():
    # Подключаемся к базе данных
    db_connection = connect_db()
    cursor = db_connection.cursor()

    # Получаем текущее время
    now = datetime.now()

    # Устанавливаем время на 3 часа назад от текущего времени
    three_hours_ago = now - timedelta(hours=3)

    # SQL запрос для получения матчей со статусом 1 и которые начались более 3 часов назад
    query = """
    SELECT id_match, data FROM `matches_24/25` 
    WHERE status = 1
    """

    cursor.execute(query)
    upcoming_games = cursor.fetchall()  # Получаем все матчи со статусом 1

    # Фильтруем матчи по времени
    ready_to_process = []
    for match in upcoming_games:
        match_id, match_data = match
        match_date_str, match_time_str = match_data.split(' ')
        match_datetime = datetime.strptime(f"{match_date_str} {match_time_str}", "%Y-%m-%d %H:%M:%S")

        # Проверяем, начался ли матч более 3 часов назад
        if match_datetime < three_hours_ago:
            ready_to_process.append(match_id)

    cursor.close()
    close_db(db_connection)

    return ready_to_process  # Возвращаем список id матчей, готовых к обработке
