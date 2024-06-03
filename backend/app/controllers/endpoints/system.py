from fastapi import APIRouter

from system.settings import Settings

router = APIRouter(prefix=f"/{Settings().BACKEND_API_PREFIX}/system")


@router.get(path="/healthcheck", status_code=200)
async def run_healthcheck() -> bool:
    """Run system self check"""
    return True