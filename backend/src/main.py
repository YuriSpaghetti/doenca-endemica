from typing import *
from datetime import datetime, timedelta
from textwrap import dedent
from pathlib import PurePath

from fastapi import FastAPI, Request, Response, Header, Body, HTTPException, Depends
from fastapi.responses import JSONResponse, HTMLResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

PurePath.str = PurePath.__str__
PurePath.endpoint = lambda self, path: self.joinpath(path).str() 

# <config>
default_url = PurePath("/api/")

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

from api import user

# </modules>

