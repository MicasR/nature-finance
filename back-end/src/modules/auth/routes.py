from fastapi import APIRouter, status
from . import schemas as s
from . import bl
from .. import exceptions as ex


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post(
    "/register-user",
    status_code=status.HTTP_201_CREATED,
    response_model= s.User,
    responses={
        201: {"description" : "Created user successfully."},
        409: {"model": ex.DetailBody, "description": "Conflict - User with given email or name already exists"},
        500: {"description": "Internal Server Error - Failed to create user"}
    }
)
async def register_user(details: s.UserCreate) -> s.User | None :
    """
    Registers a new user.
    \n

    ### Parameters:
    -----------
    details : UserCreate
        The details of the user to be created.\n
    \n

    ### Returns:
    -----------
    User
        The created user object.\n
    \n

    ### Raises:
    -----------
    - Validation Error: If the provided details do not confirm with the expected schema.
    - EmailAlreadyExists: If the provided email address already exists in the database.
    - value_error.any_str.min_length: If email has less than 8 characters.
    - value_error.any_str.max_length: If email has more than 64 characters.
    - NameAlreadyExists: If the provided username already exists in the database.
    - value_error.any_str.min_length: If name has less than 4 characters.
    - value_error.any_str.max_length: If name has more than 15 characters.
    - ValueError: If password does not contain at least one uppercase letter, one lowercase letter, one number, and one special character.
    \n

    ### Notes:
    -----------
    This function creates a new user using the provided details and adds it to the database.\n
    The user details are provided in a `UserCreate` schema which contains the following fields:
    - email (str): The email address of the user.
    - password (str): The password of the user.
    - username (str): The username of the user.

    \n
    If the provided email or username already exists in the database, an appropriate exception is raised.
    Otherwise, the created user object is returned.
    """
    try: return bl.create_user(details.dict())
    except ex.CustomException as e: raise e



@router.post(
    "/authenticate-user",
    response_model=s.Token,
    responses={
        200: {"description": "Login successful"},
        401: {"model": ex.DetailBody, "description": "Unauthorized - Invalid credentials provided"},
        500: {"description": "Internal Server Error - Failed to login"}
    }
)
async def login_user(credentials: s.UserCredentials):
    """
    Authenticates a user
    \n

    ### Parameters:
    -----------
    credentials : UserCredentials
        The details of the user credentials to be authenticated
    \n

    ### Returns:
    -----------
    Token
        The created token object.\n
    \n

    ### Raises:
    -----------
    - Validation Error: If the provided details do not confirm with the expected schema.
    - InvalidCredentials: Raised when the provided credentials do not match an existing user.
    \n

    ### Notes:
    -----------
    This function first validates the credentials by checking if they match an existing user. If they do not match,
    it raises an InvalidCredentials exception. If the credentials are valid, the function updates the user's last login time
    and returns a new access token.
    \n
    The credentials parameter is an object with the following fields:
    - email (str): The email address of the user.
    - password (str): The password of the user.
    """
    try: return bl.authenticate_user(credentials.dict())
    except ex.CustomException as e: raise e
