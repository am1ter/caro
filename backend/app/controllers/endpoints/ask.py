from fastapi import APIRouter, Depends
from system.settings import Settings

from entities.product import ProductInputUrl

router = APIRouter(prefix=f"/{Settings().BACKEND_API_PREFIX}/ask")


@router.post(path="/", status_code=200)
async def ask_about_webpage(url: ProductInputUrl = Depends()) -> bool:
    """
    Run parsing of webpage and return results
    1. Get URL of the webpage from the request and validate it
    2. Initialize infrastructure to scrap the webpage (external APIs, DB, etc)
    3. Run service to scrap the webpage and save results to the database
    4. Go to the site with alternatives and find the product
    5. Return results as a comparison of the original product and alternatives
    """
    return True
