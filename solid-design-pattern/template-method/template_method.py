from abc import ABCMeta, abstractmethod


class TestTemplate(metaclass=ABCMeta):
    def test(self):
        self.setup()
        self.execute()
        self.teardown()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def teardown(self):
        print("teardown")


class ItemServiceTest(TestTemplate):
    def setup(self):
        print("setup: ItemServiceTest")

    def execute(self):
        print("execute: ItemServiceTest")


class UserServiceTest(TestTemplate):
    def setup(self):
        print("setup: UserServiceTest")

    def execute(self):
        print("execute: UserServiceTest")


if __name__ == "__main__":
    item_service_test = ItemServiceTest()
    user_service_test = UserServiceTest()

    item_service_test.test()
    print("")
    user_service_test.test()
