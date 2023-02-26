import datetime
import jwt
from typing import Union
from src.config import settings

def create_access_token(
    user_id: Union[str, int],
    expires_delta: datetime.timedelta = datetime.timedelta(
        minutes = settings.access_token_expire_minutes
    )
) -> str:
    """
    Generate a bearer access token with the provided user_id and an optional expiration time.

    :param user_id: The unique identifier of the user.
    :param expires_delta: The expiration time of the token.
    :return: The bearer access token.
    """
    # Define the token's payload
    payload = {
        "id": user_id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + expires_delta
    }

    # Encode the payload with a secret key to generate the token
    encoded_jwt = jwt.encode(
        payload,
        settings.secret_key,
        algorithm = settings.algorithm
    )

    # Return the token
    return encoded_jwt
