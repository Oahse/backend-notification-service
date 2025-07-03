from fastapi import APIRouter, HTTPException, BackgroundTasks
from core.utils.response import Response
from services.notification import NotificationService  # assuming your UserService is here
from schemas.notification import NotificationCreate  # your Pydantic schemas


router = APIRouter(prefix='/api/v1/notification', tags=["Notification"])

@router.post("/")
async def send_notification(notification_in: NotificationCreate, background_tasks: BackgroundTasks):
    service = NotificationService(background_tasks)
    
    res, err = service.send(
        to_user_id=notification_in.to_user_id,
        body=notification_in.body,
        title=notification_in.title,
        token=notification_in.token, 
        data=notification_in.data,
        type=notification_in.type
    )
    if err:
        raise HTTPException(status_code=400, detail=err)
    
    return Response(data=None, message=res, code=201)
