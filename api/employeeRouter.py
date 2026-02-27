from fastapi import APIRouter

router = APIRouter()


@router.get("/api/employee/list")
async def listemployee():
    return "List of employee"


@router.get("/api/employee/create")
async def createemployee():
    return "Employee Created"