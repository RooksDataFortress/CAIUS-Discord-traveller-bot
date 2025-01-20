import datetime
from typing import Tuple

async def update_gambling_balance(db, user_id: int, username: str, amount: int, gambling_skill: int = 0) -> Tuple[int, int, int]:
    balancecollection = db.gamblebooks
    
    # Get existing document or initialize new balances
    user_doc = balancecollection.find_one({"user_id": user_id})
    current_balance = user_doc.get("balance", 0) if user_doc else 0
    current_bonus = user_doc.get("bonus_balance", 0) if user_doc else 0
    
    # Calculate new balances
    new_balance = current_balance + amount
    bonus_amount = int(amount * 0.1 * gambling_skill) if amount > 0 and gambling_skill > 0 else 0
    new_bonus = current_bonus + bonus_amount
    
    # Prepare and update data
    data = {
        "user_id": user_id,
        "username": username,
        "balance": new_balance,
        "bonus_balance": new_bonus,
        "last_updated": datetime.datetime.now()
    }
    
    balancecollection.update_one(
        {"user_id": user_id},
        {"$set": data},
        upsert=True
    )
    
    return new_balance, new_bonus, bonus_amount