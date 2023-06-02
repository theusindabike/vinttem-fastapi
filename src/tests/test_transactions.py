import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from src.main import app
from src.db import get_session
from src.models.transaction import Transaction, TransactionType


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
    response = client.get("/api/v1/transactions/mocked")

    app.dependency_overrides.clear()
    data = response.json()

    assert response.status_code == 200


def test_create_transcation(client: TestClient):
    response = client.post(
        "/api/v1/transactions",
        json={
            "user": "matheus",
            "value": 6.66,
            "category": 1,
            "type": 1,
            "description": "look this amazing purchase! what do you think?",
        },
    )

    data = response.json()

    assert response.status_code == 200
    assert data["user"] == "matheus"

def test_update_transaction(session: Session, client: TestClient):
    transaction_1 = Transaction(user="bianca", value=6.69, category=1, type=1, description="what nice transaction")

    session.add(transaction_1)
    session.commit()

    response = client.patch(f"/api/v1/transactions/{transaction_1.id}", json={"type": 2})
    data = response.json()


    assert response.status_code == 200
    assert data["user"] == "bianca"
    assert data["type"] == 2

