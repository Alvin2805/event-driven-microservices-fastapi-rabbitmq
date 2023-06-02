from database import Base
from sqlalchemy.orm import Mapped,mapped_column

class User(Base):
    __tablename__ = "mtr_user"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    username:Mapped[str] = mapped_column(unique=True,nullable=False)
    password:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)