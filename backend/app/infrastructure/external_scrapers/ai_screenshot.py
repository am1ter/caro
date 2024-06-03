from dataclasses import dataclass
from typing import Any

from entities.product import SourceProduct, SourceProductInputUrl
from interfaces.scraper import AiScreenshotBasicScraper
from pydantic import HttpUrl


@dataclass
class DumplingAiToChatGptScraper(AiScreenshotBasicScraper):

    def _take_screenshot(self, product_url: SourceProductInputUrl) -> HttpUrl:
        return HttpUrl(url=str(product_url.url) + "_screenshot.png")

    def _parse_screenshot(self, screenshot_url: HttpUrl) -> dict[str, Any]:
        return {"name": "Test Product", "price": 100, "currency": "ARS"}

    def _convert_to_product(
        self, product_url: SourceProductInputUrl, screenshot_url: HttpUrl, data_raw_json: dict[str, Any]
    ) -> SourceProduct:
        return SourceProduct(product_url=product_url, screenshot_url=screenshot_url, **data_raw_json)
