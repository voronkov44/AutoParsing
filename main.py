import time
from datetime import datetime
from game_parser import parse_game
from game_checker import check_upcoming_games
from game_parser7Days import parse_game_future

#создаем функцию, которая создает файл и записывает в нее сообщение если программа запущена
def log_status(message):
    with open("status_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}: {message}\n")


def main():
    log_status("Программа запущена")
    log_status("Программа работает")

    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M")  # Получаем текущее время в формате HH:MM

            # вызываем парсер для сбора данных на 7 дней вперед
            if current_time == "00:20":
                print(f"Время для запуска парсера будущих матчей: {current_time}")
                parse_game_future()  # Вызываем функцию для парсинга будущих матчей

                # Даем паузу, чтобы не запускать несколько раз в течение одной минуты
                time.sleep(60)
                continue  # Возвращаемся к началу цикла

            # Выполняем проверку игр для обработки
            upcoming_games = check_upcoming_games()

            #собираем информацию какие матчи нужно обработать из файла game_checker и вызываем парсер если нашлись матчи
            if upcoming_games:
                print(f"Найдено матчей, которые нужно обработать: {len(upcoming_games)}. Запускаем парсер.")
                for match_id in upcoming_games:
                    print(f"Обрабатываем матч с id: {match_id}")
                    parse_game(upcoming_games)

            # Пауза между проверками
            time.sleep(60)  # Проверка раз в минуту

    except Exception as e:
        log_status(f"Программа остановлена из-за ошибки: {str(e)}")  # Логируем ошибку
    finally:
        log_status("Программа неактивна")


if __name__ == "__main__":
    main()
