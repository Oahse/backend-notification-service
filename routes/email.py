from fastapi import APIRouter, Depends, HTTPException, status,BackgroundTasks
from core.utils.response import Response
from services.email import EmailService  # assuming your UserService is here
from schemas.email import EmailCreate  # your Pydantic schemas


router = APIRouter(prefix='/api/v1/email', tags=["Email"])

@router.post("/")
async def send_email(email_in: EmailCreate, background_tasks: BackgroundTasks):
    service = EmailService(background_tasks)
    activation_link = "https://yourapp.com/activate?token=abc123"
    res, err = await service.send(
        to_email=email_in.to_email,
        from_email=email_in.from_email,
        from_password=email_in.from_password,
        activation_link=email_in.activation_link,
        type = email_in.type
    )
    if err:
        raise HTTPException(status_code=400, detail=err)
    
    return Response(data=None, message=res, code=201)
