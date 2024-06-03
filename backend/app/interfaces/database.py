from abc import ABCMeta, abstractmethod

from entities.product import AlternativeProduct, SourceProduct


class BasicDatabase(metaclass=ABCMeta):
    @abstractmethod
    def save(self, sp: SourceProduct, list_ap: list[AlternativeProduct]) -> None:
        raise NotImplementedError
