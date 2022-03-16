import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    Text,
    BigInteger,
    VARCHAR
)

from .meta import Base

class Customers(Base):
    __tablename__ = 'Customers'
    CUST_ID = Column(BigInteger, nullable=False, primary_key=True)
    CUST_NAME = Column(VARCHAR(50))
    CUST_ADDRESS1 = Column(VARCHAR(50))
    CUST_ADDRESS2 = Column(VARCHAR(50))
    CUST_CITY = Column(VARCHAR(50))
    CUST_PROV_STATE = Column(VARCHAR(50))
    CUST_COUNTRY = Column(VARCHAR(50))
    CUST_POSTAL_ZIP = Column(VARCHAR(16))
    SHIP_NAME = Column(VARCHAR(50))
    SHIP_ADDRESS1 = Column(VARCHAR(50))
    SHIP_ADDRESS2 = Column(VARCHAR(50))
    SHIP_CITY = Column(VARCHAR(50))
    SHIP_PROV_STATE = Column(VARCHAR(50))
    SHIP_COUNTRY = Column(VARCHAR(50))
    SHIP_POSTAL_ZIP = Column(VARCHAR(16))
    CUST_PHONE1 = Column(VARCHAR(20))
    IS_DEALER = Column(VARCHAR(1))
    IS_REPAIR_FACILITY = Column(VARCHAR(1))
    DEALER_CLASS = Column(VARCHAR(1))
    CUST_CREDIT_RATING = Column(VARCHAR(12))
    DROP_DECK_TRAILERS = Column(VARCHAR(1))
    CURRENCY = Column(VARCHAR(3))

class CustomerUsers(Base):
    __tablename__ = 'CustomerUsers'
    CUST_ID = Column(BigInteger, nullable=False, primary_key=True)
    USER_ID = Column(BigInteger, nullable=False, primary_key=True)
    USERNAME_EMAIL = Column(VARCHAR(60), nullable=False, unique=True)
    PASSWORD_HASH = Column(VARCHAR(80), nullable=False)
    CUST_CONTACT_NAME = Column(VARCHAR(25))
    CUST_CONTACT_PHONE_EXT = Column(VARCHAR(20))
    CUST_CONTACT_CELL_PHONE = Column(VARCHAR(20))
    CUST_CONTACT_EMAIL = Column(VARCHAR(48))
    ACCOUNT_ADMIN = Column(VARCHAR(1))
    READ_ONLY_MANUALS = Column(VARCHAR(1))
    READ_ONLY_SCHEDULING = Column(VARCHAR(1))
    READ_ONLY_PRICE_LIST = Column(VARCHAR(1))
    READ_ONLY_ORDER_HISTORY = Column(VARCHAR(1))
    KIT_ORDER_ACCESS = Column(VARCHAR(1))
    PARTS_ORDER_ACCESS = Column(VARCHAR(1))
    ACTIVE = Column(VARCHAR(1))

    def set_password(self, pw):
        pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
        self.PASSWORD_HASH = pwhash.decode('utf8')

    def check_password(self, pw):
        if self.PASSWORD_HASH is not None:
            expected_hash = self.PASSWORD_HASH.encode('utf8')
            return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
        return False
