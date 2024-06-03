from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from entities.product import AlternativeProduct, SourceProductInputUrl
from interfaces.database import BasicDatabase
from interfaces.scraper import BasicScraper


@dataclass
class BasicResponder(metaclass=ABCMeta):
    scraper: BasicScraper
    database: BasicDatabase | None

    @abstractmethod
    def respond(self, product_url: SourceProductInputUrl) -> list[AlternativeProduct]:
        raise NotImplementedError
