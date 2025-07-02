from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from schemas.user import EmailType
from core.utils.encryption import PasswordManager
from typing import List, Optional
from core.utils.generator import generator
from fastapi import APIRouter, Depends, HTTPException, status,BackgroundTasks
from datetime import datetime, timedelta
from core.utils.messages.email import send_email

class EmailService:
    def __init__(self, background_tasks: BackgroundTasks):
        self.background_tasks = background_tasks

    async def send(self, *, to_email: str, from_email: str, from_password: str, html_content: str, type: EmailType):
        activation_link = "https://yourapp.com/activate?token=abc123"
    
        # send email in background (won't block the response)
        self.background_tasks.add_task(send_email, 
                              to_email=email_in.to_email, 
                              html_content=email_in.html_content,
                              from_email="youremail@gmail.com",
                              from_password="your-app-password")
        
        try:
            self.db.add(new_user)
            await self.db.commit()
            await self.db.refresh(new_user)
            # print(new_user.activation_token,'newuser',new_user.activation_token_expires)
            
            return new_user, None
        except SQLAlchemyError as e:
            await self.db.rollback()
            return None, f"DB error during user creation: {str(e)}"

    
