from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def list_users(self) -> List[User]:
        return self.repo.get_all()

    def create_user(self, data: UserCreate) -> User:
        if self.repo.get_by_email(data.email):
            raise ValueError("E-mail já está em uso.")
        return self.repo.create(data)

    def get_user(self, user_id: int) -> Optional[User]:
        return self.repo.get_by_id(user_id)

    def update_user(self, user_id: int, data: UserUpdate) -> Optional[User]:
        user = self.repo.get_by_id(user_id)
        if not user:
            return None
        if data.email is not None:
            existing = self.repo.get_by_email(data.email)
            if existing and existing.id != user_id:
                raise ValueError("E-mail já está em uso por outro usuário.")
        return self.repo.update(user, data)

    def delete_user(self, user_id: int) -> bool:
        user = self.repo.get_by_id(user_id)
        if not user:
            return False
        self.repo.delete(user)
        return True

