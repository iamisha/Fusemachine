from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/calculator", tags=["calculator"])

@router.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@router.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@router.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@router.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}
