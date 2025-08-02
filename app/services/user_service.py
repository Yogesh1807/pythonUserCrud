from app.schemas.user import UserCreate
from app.models.user import User
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException, status
from typing import List, Optional
from datetime import datetime
import logging

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def create_user(self, data: UserCreate, actor: str) -> User:
        """
        Create a new user.
        """
        try:
            user_data = data.dict(exclude={"created_by", "created_at", "modified_by", "modified_at"})
            user = User(
                 **user_data,
                created_by=actor,
                created_at=datetime.utcnow(),
                modified_by=actor,
                modified_at=datetime.utcnow()
            )
            return self.repo.create(user)
        except Exception as exc:
            logging.error(f"Error creating user: {exc}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error creating user"
            )

    def get_user(self, user_id: int) -> User:
        """
        Retrieve a user by ID.
        """
        user = self.repo.get(user_id)
        if not user:
            logging.warning(f"User not found: {user_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    def update_user(self, user_id: int, data: UserCreate, actor: str) -> User:
        """
        Update an existing user.
        """
        user = self.repo.get(user_id)
        if not user:
            logging.warning(f"User not found for update: {user_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        try:
            update_data = data.dict(exclude_unset=True)
            update_data["modified_by"] = actor
            update_data["modified_at"] = datetime.utcnow()
            return self.repo.update(user_id, update_data)
        except Exception as exc:
            logging.error(f"Error updating user {user_id}: {exc}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error updating user"
            )

    def delete_user(self, user_id: int) -> dict:
        """
        Delete a user by ID.
        """
        user = self.repo.get(user_id)
        if not user:
            logging.warning(f"User not found for delete: {user_id}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        try:
            self.repo.delete(user_id)
            return {"detail": "User deleted successfully"}
        except Exception as exc:
            logging.error(f"Error deleting user {user_id}: {exc}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error deleting user"
            )

    def list_users(self) -> List[User]:
        """
        List all users.
        """
        try:
            return self.repo.list_users()
        except Exception as exc:
            logging.error(f"Error listing users: {exc}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error listing users"
            )
