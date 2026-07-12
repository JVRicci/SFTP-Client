from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_collumn
from db.database import Base


class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_collumn(String(50), nullable=False)
    host: Mapped[str] = mapped_collumn(String(50), nullable=False)
    port: Mapped[int] = mapped_collumn(Integer, nullable=False)
    username: Mapped[str] = mapped_collumn(String(100), nullable=False)
    remote_path: Mapped[str] = mapped_collumn(String(100), nullable=False)
    local_path: Mapped[str] = mapped_collumn(String(100), nullable=False)
    editor: Mapped[str] = mapped_collumn(String(50), nullable=False)
    favorite: Mapped[bool] = mapped_collumn(Boolean, default=False)
    notes: Mapped[str | None] = mapped_collumn(Text, nullable=True)
