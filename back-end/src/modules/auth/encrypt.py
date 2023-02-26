from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password: str) -> str:
    """
    Hashes a plain password using Argon2 algorithm.
    
    ### Args:
    - password (str): Plain password.

    ### Returns:
    - str: Hashed password.
    """
    return ph.hash(password)


def verify_password(hashed_password: str, plain_password: str) -> bool:
    """
    Verifies if a plain password matches with a hashed password.
    
    ### Args:
    - hashed_password (str): Hashed password.
    - plain_password (str): Plain password.

    ### Returns:
    - bool: True if the plain password matches with the hashed password, False otherwise.
    """
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except VerifyMismatchError:
        return False
