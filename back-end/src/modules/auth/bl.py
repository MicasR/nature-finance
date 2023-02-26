from sqlalchemy import func
from . import schemas as s
from . import dl
from . import encrypt
from . import utils as u
from .. import exceptions as ex



def create_user(details: dict) -> s.User | None:
    """
    Creates a new user in the database, using the provided user details.

    ### Args:
        details (dict): A dictionary containing user details, as specified in the UserCreate schema.

    ### Returns:
        A User object containing the details of the newly created user.

    ### Raises:
        EmailAlreadyExists: If a user with the specified email already exists in the database.
        NameAlreadyExists: If a user with the specified name already exists in the database.
        ValueError: If the user details provided are invalid, as specified in the UserCreate schema.
        Exception: Any other exception that might occur during the execution of this function.

    ### Notes:
        This function first validates the user details provided using the UserCreate schema. If the validation fails,
        a ValueError is raised with details about the specific validation error(s).

        If the user details are valid, this function checks if a user with the specified email or name already exists
        in the database. If such a user exists, an EmailAlreadyExists or NameAlreadyExists exception is raised.

        If the user details are valid and a user with the specified email or name does not already exist in the database,
        this function hashes the password provided using the `hash_password` function from the `encrypt` module,
        creates a new user in the database using the `create_user` function from the `dl` module, and returns a User
        object containing the details of the newly created user.

        If any other exception occurs during the execution of this function, it is propagated up the stack.
    """

    # VALIDATIONS
    # Validate data using Pydantic model
    new_user = s.UserCreate(**details)

    # Validate if email exists
    if dl.get_user_by_email(new_user.email): raise ex.email_exists

    # Validate if name exists
    if dl.get_user_by_name(new_user.name): raise ex.name_exists

    # TRANSFORM INPUT
    # hash password
    new_user.password = encrypt.hash_password(new_user.password)

    # INTERACT WITH DB
    db_user = dl.create_user(new_user.__dict__)

    # Return user
    return s.User(**db_user.__dict__)



def authenticate_user(credentials: dict) -> s.Token:
    """
    This function is used to authenticate a user given a dictionary of credentials.
    It validates that the credentials match an existing user and returns a token that can be used to authorize requests.

    ### Args:
        credentials (dict): A dictionary with the user's email and password.
    
    ### Returns:
        s.Token: A Pydantic model representing the user's token.
    
    ### Raises:
        ValueError: If the user details provided are invalid, as specified in the UserCredentials schema.
        InvalidCredentials: Raised when the provided credentials do not match an existing user.
        Exception: Any other exception that might occur during the execution of this function.
    
    ### Notes:
        - Validates the credentials using the Pydantic UserCredentials schema.
        - Verifies that the user exists in the database.
        - Verifies that the provided password matches the user's password.
        - Updates the user's last login time.
        - Generates a new access token using the create_access_token function from the u module.
        - Returns the resulting token.
    """
    # VALIDATIONS
    # validate data Pydantic model
    cred = s.UserCredentials(**credentials)
    
    # validate that user exists
    user = dl.get_user_by_email(cred.email)
    if not user: raise ex.invalid_credentials

    # validate that password match
    if not encrypt.verify_password(user.password, cred.password): raise ex.invalid_credentials

    # TRANSFORM INPUT
    # update last login
    user.last_login = func.now()

    # INTERACT WITH DB
    db_user = dl.update_user(user)

    # RETURN
    return s.Token(access_token = u.create_access_token(db_user.id))
