from typing import *

from fastapi.middleware.cors import CORSMiddleware
from fastapi import (
    FastAPI,
    Request,
    Response,
    HTTPException,
    Header,
    Body,
    Depends,
)
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse
)


# <config>
app = FastAPI(
    title="Doença Endémica: API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# </config>

# <modules>
from .api import user

app.include_router(user.router, prefix="/api")

@app.get("/web/{path:path}")
def send_to_frontend(path: str): 
    ''' Redireciona o trafego para o frontend in Vue.
    '''

    return RedirectResponse(
        url=f"https://google.com/{path}"
    )
#fi

# </modules>

