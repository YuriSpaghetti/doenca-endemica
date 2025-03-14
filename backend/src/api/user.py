from main import app, default_url
from . import token

user_url = default_url.joinpath("user")
tags = ["user"]

@app.post(user_url.endpoint("create"), tags=tags)
def create_account():
    pass
#fi

@app.post(user_url.endpoint("login"), tags=tags)
def login() -> token.SerializedToken :
    return """{"lol":0}"""
#fi

@app.get(user_url.endpoint("{user_id}"), tags=tags)
def fetch_user(user_id: int):
    return {
        "user": "seila",
        "id": user_id
    } 
#fi