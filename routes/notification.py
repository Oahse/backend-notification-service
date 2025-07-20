from fastapi import APIRouter, HTTPException, BackgroundTasks
from core.utils.response import Response
from services.notification import NotificationService  # assuming your UserService is here
from schemas.notification import NotificationCreate, TelegramNotificationCreate  # define your schemas


router = APIRouter(prefix='/api/v1/notification', tags=["Notification"])
service = NotificationService  # or instantiate inside the endpoint

@router.post("/push")
async def send_push_notification(notification_in: NotificationCreate, background_tasks: BackgroundTasks):
    service_instance = service(background_tasks)
    res, err = service_instance.send(
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

@router.post("/telegram")
async def send_telegram_notification(notification_in: TelegramNotificationCreate, background_tasks: BackgroundTasks):
    service_instance = service(background_tasks)
    res, err = service_instance.send_telegram(
        chat_id=notification_in.chat_id,
        text=notification_in.text,
        photo_path=notification_in.photo_path,
        document_path=notification_in.document_path,
        photo_caption=notification_in.photo_caption,
        document_caption=notification_in.document_caption,
    )
    if err:
        raise HTTPException(status_code=400, detail=err)
    return Response(data=None, message=res, code=201)
