import asyncio
from typing import *

from contextlib import asynccontextmanager
import uvicorn
from util import logger, config, scheduler
from api import user
from database import _init_db

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import (
    FastAPI,
)

# <config>
logger.info("Inicializando Projeto...")
_init_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()
#fi

fastapi_app = FastAPI(
    title = "Doença Endémica: API",
    lifespan = lifespan
)

fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# </config>

# <modules>

logger.info("Importando Modulos da API...")
fastapi_app.include_router(user.router, prefix="/api")

@fastapi_app.get("/web/{path:path}")
def send_to_frontend(path: str):
    """Redireciona o trafego para o frontend in Vue."""
    return RedirectResponse(url=f"https://google.com/{path}")
#fi

# </modules>

async def main():
    server = uvicorn.Server(
        config = uvicorn.Config(
            app=fastapi_app,
            host="0.0.0.0",
            port=8080,
            workers=config.workers,
        )
    )

    await asyncio.wait([
        asyncio.create_task(server.serve()),
    ])
# fi

if __name__ == "__main__":
    asyncio.run(main())
# fi
