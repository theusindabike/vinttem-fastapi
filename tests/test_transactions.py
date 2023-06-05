import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from src.db import get_session
from src.main import app
from src.transactions.models import Transaction, TransactionType, TransactionCategory


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_list_transcations(client: TestClient):
    response = client.get("/api/v1/transactions/mocked/")

    app.dependency_overrides.clear()

    assert response.status_code == 200


def test_create_transcation(client: TestClient):
    response = client.post(
        "/api/v1/transactions",
        json={
            "user": "matheus",
            "value": 6.66,
            "category": TransactionCategory.recreation,
            "type": TransactionType.proportional,
            "description": "look this amazing purchase! what do you think?",
        },
    )

    data = response.json()

    assert response.status_code == 200
    assert data["user"] == "matheus"


def test_update_transaction(session: Session, client: TestClient):
    transaction_1 = Transaction(
        user="bianca",
        value=6.69,
        category=TransactionCategory.recreation,
        type=TransactionType.proportional,
        description="what nice transaction",
    )

    session.add(transaction_1)
    session.commit()

    response = client.patch(
        f"/api/v1/transactions/{transaction_1.id}",
        json={"type": TransactionType.even},
    )
    data = response.json()

    assert response.status_code == 200
    assert data["user"] == "bianca"
    assert data["type"] == TransactionType.even


def test_delete_transaction(session: Session, client: TestClient):
    transaction_1 = Transaction(
        user="bianca",
        value=6.69,
        category=1,
        type=1,
        description="what nice transaction",
    )

    session.add(transaction_1)
    session.commit()

    response = client.delete(f"/api/v1/transactions/{transaction_1.id}/")
    data = response.json()

    assert response.status_code == 200
    assert data["ok"]
