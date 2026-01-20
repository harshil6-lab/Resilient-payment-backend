from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
import logging

router = APIRouter(prefix="/payment", tags = ["Payment"])

class PaymentRequest(BaseModel):
    user_id : int
    amount : float

@router.post("/initiate")

def intitiate_payment(request: PaymentRequest):
    logging.info("Payment intiation request received for user_id : %s | Amount : %s",request.user_id,request.amount)

    if request.amount <= 0:
        logging.error("Invalid Payment Amount : %s from user_id : %s",request.amount,request.user_id)
        raise HTTPException(status_code=400, detail="Invalid payment amount, Amount must be greater than zero.")
    

    return {
        "status" : "Good",
        "Message" : "Payment initiated succsessfully"
    }