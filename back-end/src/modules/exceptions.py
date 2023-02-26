from typing import List, Dict, Any
from fastapi import HTTPException, status
from pydantic import BaseModel

class CustomException(HTTPException):
    def __init__(
        self,
        detail: List[Dict[str, Any]],
        status_code: int = status.HTTP_409_CONFLICT
    ):
        super().__init__(
            status_code=status_code, detail=detail
        )


def detail_body(field: str, msg: str, ex_type: str) -> List[Dict[str, Any]]:
    return [
        {
            "loc": ["body", field],
            "msg": msg,
            "type": ex_type,
        }
    ]


class DetailBody(BaseModel):
    detail: List[Dict[str, Any]] = [
        {
            "loc": [
                "body",
                "field"
            ],
            "msg": "string",
            "type": "string"
        }
    ]



invalid_credentials = CustomException(detail_body(
    field="Credentials",
    msg="Invalid email or password",
    ex_type="invalid_credentials"
), status_code=status.HTTP_401_UNAUTHORIZED)



email_exists = CustomException(detail_body(
    field="email",
    msg="Email already exists",
    ex_type="conflict"
))


name_exists = CustomException(detail_body(
    field="name",
    msg="Name already exists",
    ex_type="conflict"
))
