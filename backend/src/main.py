import asyncio
from typing import *

from contextlib import asynccontextmanager
from tasks import get_scheduler, setup_tasks
import uvicorn
from util import get_logger, config
from database import initialize_db
from api import user

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi import (
    FastAPI,
)

# <config>
logger = get_logger()
logger.info("Inicializando Projeto...")

db = initialize_db()
sched = get_scheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    sched.start()
    setup_tasks()
    yield
    sched.shutdown()
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
