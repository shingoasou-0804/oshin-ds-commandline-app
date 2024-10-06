from __future__ import annotations
import copy
from abc import ABCMeta, abstractmethod


class ItemPrototype(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.__name = name
        self.__review: list[str] = []

    def __str__(self):
        return f"{self.__name}: {self.__review}"

    def set_review(self, review: str):
        self.__review.append(review)

    @abstractmethod
    def create_copy(self) -> ItemPrototype:
        pass


class DeepCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.deepcopy(self)


class ShallowCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.copy(self)


class ItemManager:
    def __init__(self):
        self.items = {}

    def register_item(self, key: str, item: ItemPrototype):
        self.items[key] = item

    def create(self, key: str):
        if key in self.items:
            item = self.items[key]
            return item.create_copy()
        raise Exception("指定されたキーが存在しません。")


if __name__ == "__main__":
    mouse = DeepCopyItem("マウス")
    keyboard = ShallowCopyItem("キーボード")

    manager = ItemManager()
    manager.register_item("mouse", mouse)
    manager.register_item("keyboard", keyboard)

    cloned_mouse = manager.create("mouse")
    cloned_keyboard = manager.create("keyboard")

    cloned_mouse.set_review("Good!")
    cloned_keyboard.set_review("SoSo!")

    print("mouse(original): ", mouse)
    print("mouse(copy): ", cloned_mouse)
    print("")
    print("keyboard(original): ", keyboard)
    print("keyboard(copy): ", cloned_keyboard)
