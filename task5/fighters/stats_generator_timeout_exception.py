
class StatsGeneratorTimeoutException(Exception):
    def __init__(self):
        self.message = "Превышено максимальное время сбора статистики. Завершение"