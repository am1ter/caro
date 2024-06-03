import uvicorn

from system.settings import Settings


def run() -> None:
    if Settings().DEV_MODE:
        uvicorn.run(
            app="controllers.fastapi:fastapi_app",
            host=Settings().BACKEND_HOST,
            port=Settings().BACKEND_PORT,
            reload=True,
            reload_dirs=["backend/app", "app"],  # local / docker path
        )
    else:
        uvicorn.run(
            app="controllers.fastapi:fastapi_app",
            host=Settings().BACKEND_HOST,
            port=Settings().BACKEND_PORT,
        )


if __name__ == "__main__":
    run()