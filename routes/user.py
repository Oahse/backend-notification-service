from fastapi import APIRouter, Depends, HTTPException, status,BackgroundTasks
from core.utils.response import Response
from services.user import EmailService  # assuming your UserService is here
from schemas.user import EmailCreate  # your Pydantic schemas


router = APIRouter(prefix='/api/v1/email', tags=["Email"])

@router.post("/")
async def send_email(email_in: EmailCreate, background_tasks: BackgroundTasks):
    service = EmailService(background_tasks)
    user, err = await service.send(
        to_email=email_in.to_email,
        from_email=email_in.from_email,
        from_password=email_in.from_password,
        html_content=email_in.html_content,
        type = email_in.type
    )
    if err:
        raise HTTPException(status_code=400, detail=err)
    
    return Response(data=user.to_dict(), message='User created successfully', code=201)
