from fastapi import APIRouter

router = APIRouter(
    prefix="/cars",
    tags=["cars"]
)


@router.get("/",)
async def read_cars():
    return [
        {"name": "Aston Martin Vulcan"},
        {"name": "Bugatti Chiron"}
    ]
