import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик, который будет выводить логи в консоль
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    # Задаем форматирование лог-сообщений: включаем время, имя логгера, уровень и сообщение
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(handler)

    return logger
