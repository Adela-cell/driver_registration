# app/routes.py
from fastapi import APIRouter, HTTPException
from app.models import Driver
from app.database import drivers_collection

router = APIRouter()

# 1. Register a new driver
@router.post("/drivers/register")
async def register_driver(driver: Driver):
    # Check if the driver already exists using their phone number
    if drivers_collection.find_one({"phone": driver.phone}):
        raise HTTPException(status_code=400, detail="A driver with this phone number already exists.")

    # Save the new driver's information in the database
    drivers_collection.insert_one(driver.dict())
    return {
        "message": "Driver registered successfully!",
        "driver": driver.dict(),
    }

# 2. Retrieve a driver using their phone number
@router.get("/drivers/{phone}")
async def get_driver(phone: str):
    # Find the driver in the database by phone number
    driver = drivers_collection.find_one({"phone": phone})
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found.")

    # Convert the driver's MongoDB ObjectId to a string for JSON response
    driver["_id"] = str(driver["_id"])
    return {
        "message": "Driver found!",
        "driver": driver,
    }
