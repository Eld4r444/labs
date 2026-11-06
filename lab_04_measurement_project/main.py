import json
import logging
from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max


def load_config(config_path="config.json"):
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def setup_logging(log_file):
    Path(log_file).parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )


def main():
    config = load_config()
    setup_logging(config["log_file"])
    logging.info("Программа запущена")

    input_path = Path(config["input_file"])
    print("Файл измерений:", input_path)

    try:
        numbers = read_numbers(input_path)
        validate_numbers(numbers)
    except FileNotFoundError:
        logging.error("Файл не найден: %s", input_path)
        print("Ошибка: файл не найден:", input_path)
        return
    except ValueError as error:
        logging.error("Ошибка данных: %s", error)
        print("Ошибка данных:", error)
        return

    logging.info("Файл %s успешно прочитан", input_path)
    logging.info("Прочитано значений: %d", len(numbers))

    count = len(numbers)
    minimum = find_min(numbers)
    maximum = find_max(numbers)
    average = calculate_average(numbers)

    print("Количество значений:", count)
    print("Минимум:", minimum)
    print("Максимум:", maximum)
    print(f"Среднее значение: {average:.2f}")
    logging.info("Количество: %d, минимум: %s, максимум: %s, среднее: %.2f", count, minimum, maximum, average)
    logging.info("Программа завершена")


if __name__ == "__main__":
    main()
