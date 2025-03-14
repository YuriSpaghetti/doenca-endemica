import json

# Um float represetando uma timestamp do unix.
stamp = float
SerializedToken = str

class UserAuthToken:
    token_id: int
    user_id: int
    name: str
    issued_on: stamp
    valid_until: stamp
    signature: str

    def __init__(
        self,       
        id: int,
        name: str,
        issued_on: stamp,
        valid_until: stamp,
        signature: str,
    ):
        self.id: int = id
        self.name: str = name
        self.issued_on: stamp = issued_on
        self.valid_until: stamp = valid_until
        self.signature: str = signature
    #fi

    def serialize(self) -> SerializedToken:
        return json.dumps({
            "id": self.id,
            "name": self.name,
            "issuedOn": self.issued_on,
            "validUntil": self.valid_until,
            "signature": self.signature,
        })
    #fi

    @classmethod
    def deserialize(json_token: str):
        token_dict = json.loads(json_token)
        token = UserAuthToken(
            token_dict["id"],
            token_dict["name"],
            token_dict["issuedOn"],
            token_dict["validUntil"],
            token_dict["signature"],
        )

        if not token.validate():
            raise token.ValidationError("Failed to validate Serialized token")
        #fi

        return token 
    #fi

    @classmethod
    class ValidationError(Exception): pass

    #TODO
    def validate(self) -> bool:
        ''' Fala com o banco de dados e valida a authencidade do emissor do token.
            Não valida se este está expirado.
        '''
        return True
    #fi 
#fi