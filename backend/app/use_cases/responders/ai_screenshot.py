from dataclasses import dataclass

from entities.product import AlternativeProduct, SourceProduct, SourceProductInputUrl
from interfaces.database import BasicDatabase
from interfaces.scraper import AiScreenshotBasicScraper
from interfaces.service import BasicResponder


@dataclass
class AiScreenshotResponder(BasicResponder):
    scraper: AiScreenshotBasicScraper
    database: BasicDatabase | None = None

    def respond(self, product_url: SourceProductInputUrl) -> list[SourceProduct]:
        return [self.scraper.parse(product_url=product_url)]
