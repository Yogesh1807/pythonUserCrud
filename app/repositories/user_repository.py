from app.models.user import User
from sqlmodel import Session

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get(self, user_id: int) -> User:
        return self.session.get(User, user_id)

    def update(self, user_id: int, data: dict) -> User:
        db_user = self.get(user_id)
        for key, value in data.items():
            setattr(db_user, key, value)
        self.session.commit()
        return db_user

    def delete(self, user_id: int):
        user = self.get(user_id)
        self.session.delete(user)
        self.session.commit()

    def list_users(self):
        return self.session.query(User).all()
