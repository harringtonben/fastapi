from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get('/')
async def get():
    return JSONResponse('Everything is nice and healthy!!!')