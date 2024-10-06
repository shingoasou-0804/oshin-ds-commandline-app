from abc import ABCMeta, abstractmethod


class CreditCard(metaclass=ABCMeta):
    def __init__(self, owner: str):
        self.__owner = owner

    @property
    def owner(self) -> str:
        return self.__owner

    @abstractmethod
    def get_card_type(self) -> str:
        pass

    @abstractmethod
    def get_annual_charge(self) -> int:
        pass


class Platinum(CreditCard):
    def get_card_type(self) -> str:
        return "Platinum"

    def get_annual_charge(self) -> int:
        return 30000


class Gold(CreditCard):
    def get_card_type(self) -> str:
        return "Gold"

    def get_annual_charge(self) -> int:
        return 10000


class CreditCardFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_credit_card(self, owner: str) -> CreditCard:
        pass

    @abstractmethod
    def register_credit_card(self, credit_card: CreditCard):
        pass

    def create(self, owner: str) -> CreditCard:
        credit_card = self.create_credit_card(owner)
        self.register_credit_card(credit_card)

        return credit_card


credit_card_database: list[CreditCard] = []


class PlatinumCreditCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str) -> CreditCard:
        return Platinum(owner)

    def register_credit_card(self, credit_card: CreditCard):
        credit_card_database.append(credit_card)


class GoldCreditCardFactory(CreditCardFactory):
    def create_credit_card(self, owner: str) -> CreditCard:
        return Gold(owner)

    def register_credit_card(self, credit_card: CreditCard):
        credit_card_database.append(credit_card)


if __name__ == "__main__":
    platinum_card_factory = PlatinumCreditCardFactory()
    platinum_card = platinum_card_factory.create("Tanaka")
    print(platinum_card.get_card_type())

    gold_card_factory = GoldCreditCardFactory()
    gold_card = gold_card_factory.create("Suzuki")
    print(gold_card.get_card_type())

    print(credit_card_database)
