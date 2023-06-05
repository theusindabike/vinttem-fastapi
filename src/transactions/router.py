from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select

from src.db import ActiveSession
from src.transactions.models import (
    Transaction,
    TransactionIncoming,
    TransactionResponse,
)

router = APIRouter()


@router.get("/")
async def list_transactions(*, session: Session = ActiveSession):
    transactions = session.exec(select(Transaction)).all()
    return transactions


@router.post("/", response_model=TransactionResponse)
async def create_transaction(
    *, session: Session = ActiveSession, transaction: TransactionIncoming
):
    db_transaction = Transaction.from_orm(transaction)
    session.add(db_transaction)
    session.commit()
    session.refresh(db_transaction)
    return db_transaction


@router.patch(
    "/{transaction_id}/",
    response_model=TransactionResponse,
)
async def update_transaction(
    *,
    transaction_id: int,
    session: Session = ActiveSession,
    patch_transaction: TransactionIncoming
):
    transaction = session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="i'm sorry, nothing here")

    patch_transaction_data = patch_transaction.dict(exclude_unset=True)
    for key, value in patch_transaction_data.items():
        setattr(transaction, key, value)

    session.commit()
    session.refresh(transaction)
    return transaction


@router.delete(
    "/{transaction_id}/",
)
async def delete_transaction(*, session: Session = ActiveSession, transaction_id: int):
    transaction = session.get(Transaction, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="i'm sorry, nothing here")

    session.delete(transaction)
    session.commit()
    return {"ok": True}


@router.get("/mocked/")
async def mockedList():
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
