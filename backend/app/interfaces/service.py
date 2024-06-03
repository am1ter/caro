from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

from backend.app.interfaces.database import BasicDatabase
from backend.app.interfaces.scraper import BasicScraper
from entities.product import AlternativeProduct, SourceProductInputUrl


@dataclass
class BasicResponder(metaclass=ABCMeta):
    database: BasicDatabase
    scraper: BasicScraper

    @abstractmethod
    def respond(self, url: SourceProductInputUrl) -> list[AlternativeProduct]:
        raise NotImplementedError
