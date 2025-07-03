from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from schemas.email import EmailType
from core.utils.encryption import PasswordManager
from typing import List, Optional
from core.utils.generator import generator
from fastapi import APIRouter, Depends, HTTPException, status,BackgroundTasks
from datetime import datetime, timedelta
from core.utils.messages.email import send_email, render_activation_email

class EmailService:
    def __init__(self, background_tasks: BackgroundTasks):
        self.background_tasks = background_tasks

    async def send(self, *, to_email: str, from_email: str, from_password: str, activation_link: str, type: EmailType):
        try:
            
            html_content = activation_link
            if type == "activation":
                html_content = render_activation_email(activation_link)

            self.background_tasks.add_task(
                send_email,
                to_email=to_email,
                html_content=html_content,
                from_email=from_email,
                from_password=from_password
            )

            return "Email sent successfully", None

        except Exception as e:
            return None, str(e)
        

    
