from abc import ABCMeta, abstractmethod

from entities.product import SourceProduct, SourceProductInputUrl


class BasicScraper(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, url: SourceProductInputUrl) -> SourceProduct:
        raise NotImplementedError
