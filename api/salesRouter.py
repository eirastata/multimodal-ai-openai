from fastapi import APIRouter

router = APIRouter()


@router.get("/api/sales/list")
async def listsales():
    return "List of sales"


@router.get("/api/sales/create")
async def createsales():
    return "Sales created with success"