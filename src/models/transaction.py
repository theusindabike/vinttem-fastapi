from enum import Enum
from typing import Optional
from pydantic import condecimal
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Enum as SA_Enum


class TransactionCategory(Enum):
    recreation = 1
    market_stuff = 2


class TransactionType(Enum):
    proportional = 1
    even = 2


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: str
    value: condecimal(max_digits=10, decimal_places=2, ge=0) = Field(nullable=False)
    category: TransactionCategory = Field(
        sa_column=Column(SA_Enum(TransactionCategory), default=None, index=False)
    )
    type: TransactionType = Field(
        sa_column=Column(SA_Enum(TransactionType), default=None, index=False)
    )
    description: str = Field(max_length=255)
