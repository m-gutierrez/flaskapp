from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from website import db, login_manager
from flask_login import UserMixin
from enum import Enum

class AUTH(Enum):
    ME = 1
    SELECT = 2
    FAMILY = 3
    FRIENDS = 4
    PUBLIC = 5

@login_manager.user_loader
def load_user(id):
    return User.get(id)

class User(UserMixin, db.Model):
    id: so.Mapped[str] = so.mapped_column(sa.String(64),primary_key=True, unique=True)
    username: so.Mapped[str] = so.mapped_column(
        sa.String(64), index=True)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(64), index=True)
    picture: so.Mapped[Optional[str]] = so.mapped_column(
        sa.String(64))
    comments: so.WriteOnlyMapped['Comment'] = so.relationship(
        back_populates='author')
    log_ins: so.WriteOnlyMapped['LogIns'] = so.relationship(
        back_populates='user')
    auth: so.Mapped[AUTH] = so.mapped_column(
        index=True, default=AUTH.PUBLIC)

    @staticmethod
    def get(id):
        return db.session.get(User, id)

class LogIns(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey(User.id), index=True)
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user: so.Mapped[User] = so.relationship(back_populates="log_ins")

class Comment(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey(User.id), index=True)
    author: so.Mapped[User] = so.relationship(back_populates="comments")


