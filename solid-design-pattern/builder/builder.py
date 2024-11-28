from abc import ABCMeta, abstractmethod


class Computer:
    def __init__(self):
        self.type = None
        self.cpu = None
        self.ram = None

    def __str__(self):
        return f"type: {self.type} cpu: {self.cpu}, ram: {self.ram}"


class ComputerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def add_cpu(self, cpu: str):
        pass

    @abstractmethod
    def add_ram(self, ram: int):
        pass


class DesktopBuilder(ComputerBuilder):
    def __init__(self):
        self.__computer = Computer()
        self.__computer.type = "Desktop"

    def add_cpu(self, cpu: str):
        self.__computer.cpu = cpu

    def add_ram(self, ram: int):
        self.__computer.ram = ram

    def get_result(self) -> Computer:
        return self.__computer


class LaptopBuilder(ComputerBuilder):
    def __init__(self):
        self.__computer = Computer()
        self.__computer.type = "Laptop"

    def add_cpu(self, cpu: str):
        self.__computer.cpu = cpu

    def add_ram(self, ram: int):
        self.__computer.ram = ram

    def get_result(self) -> Computer:
        return self.__computer


class Director:
    def __init__(self, builder: ComputerBuilder):
        self.__builder = builder

    def construct(self):
        self.__builder.add_cpu("Core i5")
        self.__builder.add_ram(16)

    def high_spec_construct(self):
        self.__builder.add_cpu("M2")
        self.__builder.add_ram(64)


if __name__ == "__main__":
    desktop_builder = DesktopBuilder()
    desktop_director = Director(desktop_builder)
    desktop_director.construct()
    desktop_computer = desktop_builder.get_result()
    print(desktop_computer)

    laptop_builder = LaptopBuilder()
    laptop_director = Director(laptop_builder)
    laptop_director.high_spec_construct()
    laptop_computer = laptop_builder.get_result()
    print(laptop_computer)
