from abc import ABCMeta, abstractmethod


class Server(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, user_id: str):
        pass


class RealServer(Server):
    def handle(self, user_id: str):
        print(f"RealServer: {user_id}の処理を実行中...")


class Proxy(Server):
    def __init__(self, server: Server):
        self.__server = server

    def _authorize(self, user_id: str):
        authorized_user_id = ["1", "2", "3"]

        if not user_id in authorized_user_id:
            raise Exception("操作が許可されていません。")

    def handle(self, user_id: str):
        self._authorize(user_id)

        print(f"Proxy: {user_id}の処理を開始します。")
        self.__server.handle(user_id)
        print(f"Proxy: {user_id}の処理が完了しました。")


if __name__ == "__main__":
    server = RealServer()
    proxy = Proxy(server)
    proxy.handle("1")
    proxy.handle("4")
