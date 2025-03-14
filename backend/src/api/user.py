from fastapi import APIRouter
from .. import token

router = APIRouter(prefix="/user")
tags = ["user"]

@router.post("/create", tags=tags)
def create_account():
    ''' Registra um novo usuario no banco de dados.
    '''
    pass
#fi

@router.post("/login", tags=tags)
def login() -> token.SerializedToken :
    ''' Retorna um token assinado pelo servidor.
    '''
    return """{"lol":0}"""
#fi

@router.get("/{user_id}", tags=tags)
def fetch_user(user_id: int):
    ''' Retorna, em json, toda informação relacionada ao usuario relacionado ao identificador 
    '''
    return {
        "user": "seila",
        "id": user_id
    } 
#fi