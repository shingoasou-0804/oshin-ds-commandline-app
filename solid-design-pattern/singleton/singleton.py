import datetime


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def output(self, content: str):
        now = datetime.datetime.now()
        print(f"{now}: {content}")


class Test:
    pass


if __name__ == "__main__":
    test1 = Test()
    test2 = Test()
    print("Test: ", test1 == test2)

    logger1 = Logger()
    logger2 = Logger()
    print("Singleton: ", logger1 == logger2)

    logger1.output("logger1のログ")
    logger2.output("logger2のログ")
