from database import Base
from sqlalchemy.orm import Mapped,mapped_column

class Address(Base):
    __tablename__ = "mtr_address_test"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    address:Mapped[str] = mapped_column(nullable=False)