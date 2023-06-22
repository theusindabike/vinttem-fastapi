from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, condecimal, validator
from sqlalchemy import Column
from sqlalchemy import Enum as SA_Enum
from sqlmodel import Field, SQLModel


class TransactionCategory(str, Enum):
    recreation = "recreation"
    market_stuff = "marketStuff"
    health = "health"
    study = "study"
    cloths = "cloths"
    housing = "housing"
    transport = "transport"
    subscription = "subscription"
    pets = "pets"
    gifts = "gifts"
    personal_care = "personalCare"
    donations = "donations"
    shopping = "shopping"
    travel = "travel"


class TransactionType(str, Enum):
    proportional = "proportional"
    even = "even"
    individual = "individual"


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional[str]
    value: Optional[condecimal(max_digits=10, decimal_places=2, ge=0)] = Field()
    category: Optional[TransactionCategory] = Field(
        sa_column=Column(SA_Enum(TransactionCategory), default=None, index=False)
    )
    type: Optional[TransactionType] = Field(
        sa_column=Column(SA_Enum(TransactionType), default=None, index=False)
    )
    description: Optional[str] = Field(max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_edited: datetime = Field(default_factory=datetime.utcnow)

    @validator("user")
    def must_be_bianca_or_matheus(cls, v):
        if v not in ("matheus", "bianca"):
            raise ValueError("must be matheus or bianca")
        return v


class TransactionResponse(BaseModel):
    user: Optional[str]
    value: Optional[Decimal]
    category: Optional[TransactionCategory]
    type: Optional[TransactionType]
    description: Optional[str]


class TransactionIncoming(BaseModel):
    user: Optional[str]
    value: Optional[str]
    category: Optional[TransactionCategory]
    type: Optional[TransactionType]
    description: Optional[str]

    class Config:
        extra = Extra.allow
        arbitrary_types_allowed = True

        # def __init__(self, *args, **kwargs):
        # pass
