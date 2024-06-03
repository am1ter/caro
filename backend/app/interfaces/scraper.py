from abc import ABCMeta, abstractmethod
from typing import Any

from pydantic import HttpUrl
from entities.product import SourceProduct, SourceProductInputUrl


class BasicScraper(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, product_url: SourceProductInputUrl) -> SourceProduct:
        raise NotImplementedError


class AiScreenshotBasicScraper(BasicScraper):
    def parse(self, product_url: SourceProductInputUrl) -> SourceProduct:
        screenshot_url = self._take_screenshot(product_url=product_url)
        data_raw_json = self._parse_screenshot(screenshot_url=screenshot_url)
        return self._convert_to_product(
            product_url=product_url, screenshot_url=screenshot_url, data_raw_json=data_raw_json
        )

    @abstractmethod
    def _take_screenshot(self, product_url: SourceProductInputUrl) -> HttpUrl:
        raise NotImplementedError

    @abstractmethod
    def _parse_screenshot(self, screenshot_url: HttpUrl) -> dict[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def _convert_to_product(
        self, product_url: SourceProductInputUrl, screenshot_url: HttpUrl, data_raw_json: dict[str, Any]
    ) -> SourceProduct:
        raise NotImplementedError
