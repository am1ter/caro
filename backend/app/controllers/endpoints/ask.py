from typing import Annotated
from fastapi import APIRouter, Depends
from infrastructure.external_scrapers.ai_screenshot import DumplingAiToChatGptScraper
from use_cases.responders.ai_screenshot import AiScreenshotResponder
from system.settings import Settings

from entities.product import AlternativeProduct, SourceProductInputUrl

router = APIRouter(prefix=f"/{Settings().BACKEND_API_PREFIX}/ask")


UrlDep = Annotated[SourceProductInputUrl, Depends()]
ScraperDep = Annotated[DumplingAiToChatGptScraper, Depends()]


def create_responder(scraper: ScraperDep) -> AiScreenshotResponder:
    return AiScreenshotResponder(scraper=scraper)


ResponderDep = Annotated[AiScreenshotResponder, Depends(create_responder)]


@router.post(path="/", status_code=200)
async def ask_about_webpage(product_url: UrlDep, responder: ResponderDep) -> list[AlternativeProduct]:
    """
    Run parsing of webpage and return results
    1. Get URL of the webpage from the request and validate it
    2. Initialize infrastructure to scrap the webpage (external APIs, DB, etc)
    3. Run service to scrap the webpage and save results to the database
    4. Go to the site with alternatives and find the product
    5. Return results as a comparison of the original product and alternatives
    """
    alternatives = responder.respond(product_url=product_url)
    return alternatives
