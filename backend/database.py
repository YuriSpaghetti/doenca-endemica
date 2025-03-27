from sqlalchemy import Engine
from sqlmodel import Field, Session, SQLModel, create_engine, Enum
from typing import Optional
from typing import *
from datetime import date
from functools import cache
from util import config, logger
import os
import enum


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)

    account_created: date
    email: str
    name: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)
# fi


class Role(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
# fi


class Session_type(enum.Enum):
    e = 0
# fi


class User_Session(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None)
    type: Session_type = Field(sa_type=Enum(Session_type))  # type: ignore
# fi


db: Engine = None #type: ignore

def _init_db():
    global db

    logger.info("Inicializando banco de dados.")
    SQLModel.metadata.create_all(
        db := create_engine(f"sqlite:///{os.path.normpath(config.db_path)}")
    )
#fi
