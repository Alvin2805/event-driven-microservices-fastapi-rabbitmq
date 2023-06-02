from database import Base
from sqlalchemy.orm import Mapped,mapped_column

class UserDetail(Base):
    __tablename__ = "mtr_user_detail"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    fullname:Mapped[str] = mapped_column(unique=True,nullable=False)
    company:Mapped[str] = mapped_column(nullable=False)
    username:Mapped[str] = mapped_column(nullable=False)
    address:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    login_id:Mapped[int] = mapped_column(nullable=False) # communication with service1