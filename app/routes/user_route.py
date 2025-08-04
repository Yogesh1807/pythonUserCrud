from fastapi import APIRouter, Depends, Request
import time
import logging
from fastapi import Request
from sqlmodel import Session
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db.session import get_session
from typing import List
from app.utils.auth import verify_token
from app.core.config import settings

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(request: Request, user: UserCreate, session: Session = Depends(get_session)) -> UserRead:
    actor = "admin"  # Replace with logic to get current user, e.g. from token
    service = UserService(UserRepository(session))
    return service.create_user(user,actor)

@router.get("/{user_id}", response_model=UserRead)
def get_user(request: Request, user_id: int, session: Session = Depends(get_session)) -> UserRead:
    service = UserService(UserRepository(session))
    return service.get_user(user_id)

@router.put("/{user_id}", response_model=UserRead)
def update_user(request: Request, user_id: int, user: UserCreate, session: Session = Depends(get_session)) -> UserRead:
    service = UserService(UserRepository(session))
    return service.update_user(user_id, user)

@router.delete("/{user_id}", response_model=dict)
def delete_user(request: Request, user_id: int, session: Session = Depends(get_session)) -> dict:
    service = UserService(UserRepository(session))
    service.delete_user(user_id)
    return {"detail": "User deleted successfully"}

@router.get("/", response_model=List[UserRead])
def list_users(request: Request, session: Session = Depends(get_session)) -> List[UserRead]:
    service = UserService(UserRepository(session))
    return service.list_users()
