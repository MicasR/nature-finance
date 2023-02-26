from . import models as m
from db.session_handler import session_maker



def create_user(details: dict) -> m.User:
    """
    Creates a new user in the database with the provided details.
    
    ### Args:
    - details (dict): A dictionary containing the details of the new user.
    
    ### Returns:
    - A User instance representing the newly created user.

    ### Raises:
        SQLAlchemyError: If there's an error with the database update.
    """
    new_user = m.User(**details)
    with session_maker() as session:
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    return new_user



def get_user_by_email(email: str) -> m.User | None:
    """
    Retrieves a user from the database by their email.
    
    ### Args:
    - email (str): The email of the user to retrieve.
    
    ### Returns:
    - A User instance representing the user with the specified email, or None if no such user exists.

    ### Raises:
        SQLAlchemyError: If there's an error with the database update.
    """
    with session_maker() as session:
        user = session.query(m.User
        ).filter(m.User.email == email
        ).first()
    return user



def get_user_by_name(name: str) -> m.User | None:
    """
    Retrieves a user from the database by their name.
    
    ### Args:
    - name (str): The name of the user to retrieve.
    
    ### Returns:
    - A User instance representing the user with the specified name, or None if no such user exists.

    ### Raises:
        SQLAlchemyError: If there's an error with the database update.
    """
    with session_maker() as session:
        user = session.query(m.User
        ).filter(m.User.name == name
        ).first()
    return user



def get_user_by_id(user_id: int) -> m.User | None:
    """
    Retrieves a user from the database by their ID.
    
    ### Args:
    - user_id (int): The ID of the user to retrieve.
    
    ### Returns:
    - A User instance representing the user with the specified ID, or None if no such user exists.

    ### Raises:
        SQLAlchemyError: If there's an error with the database update.
    """
    with session_maker() as session:
        user = session.query(m.User
        ).filter(m.User.id == user_id
        ).first()
    return user



def update_user(user: m.User) -> m.User:
    """
    Update the user data in the database.

    ### Args:
        user (m.User): The user data to be updated.

    ### Returns:
        m.User: The updated user data.

    ### Raises:
        SQLAlchemyError: If there's an error with the database update.
    """
    with session_maker() as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user
