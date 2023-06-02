from fastapi import APIRouter, Request 
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from src.db import ActiveSession
from src.models.transaction import Transaction, TransactionIncoming, TransactionResponse

router = APIRouter()


@router.get("/")
async def list_transactions(*, session: Session = ActiveSession):
    transactions = session.exec(select(Transaction)).all()
    return transactions

@router.post("/", response_model=TransactionResponse)
async def create_transaction(*, session: Session = ActiveSession, request: Request, transaction: TransactionIncoming):
    db_transaction = Transaction.from_orm(transaction)
    session.add(db_transaction)
    session.commit()
    session.refresh(db_transaction)
    return db_transaction


@router.get("/mocked")
async def root():
    return {
        "results": [
            {
                "id": "fake_id_1",
                "user": "matheus",
                "value": 111.11,
                "category": "marketStuff",
                "type": "even",
                "description": "fake description 1",
            },
            {
                "id": "fake_id_2",
                "user": "matheus",
                "value": 222.22,
                "category": "marketStuff",
                "type": "even",
                "description": "fake description 2",
            },
            {
                "id": "fake_id_3",
                "user": "matheus",
                "value": 3.33,
                "category": "marketStuff",
                "type": "even",
                "description": "fake description 3",
            },
            {
                "id": "fake_id_4",
                "user": "bianca",
                "value": 4444.44,
                "category": "marketStuff",
                "type": "even",
                "description": "fake description 4",
            },
            {
                "id": "fake_id_5",
                "user": "bianca",
                "value": 5.55,
                "category": "marketStuff",
                "type": "even",
                "description": "fake description 4",
            },
        ]
    }
