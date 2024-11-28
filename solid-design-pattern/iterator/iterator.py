from abc import ABCMeta, abstractmethod


class Patient:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name


class IIterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self) -> IIterator:
        pass


class WaitingRoom(Aggregate):
    def __init__(self):
        self.__patients = []

    def get_patients(self) -> list[Patient]:
        return self.__patients

    def get_count(self) -> int:
        return len(self.__patients)

    def check_in(self, patient: Patient):
        self.__patients.append(patient)

    def get_iterator(self) -> IIterator:
        return WaitingRoomIterator(self)


class WaitingRoomIterator(IIterator):
    def __init__(self, aggregate: WaitingRoom):
        self.__position = 0
        self.__aggregate = aggregate

    def has_next(self) -> bool:
        return self.__position < self.__aggregate.get_count()

    def next(self):
        if not self.has_next():
            print("患者がいません。")
            return

        patient = self.__aggregate.get_patients()[self.__position]
        self.__position += 1
        return patient


if __name__ == "__main__":
    waiting_room = WaitingRoom()
    waiting_room.check_in(Patient(1, "Yamada"))
    waiting_room.check_in(Patient(2, "Suzuki"))
    waiting_room.check_in(Patient(3, "Tanaka"))

    iterator = waiting_room.get_iterator()
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
    print(iterator.next())
