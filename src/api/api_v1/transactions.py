from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("")
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
