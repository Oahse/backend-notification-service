from fastapi import BackgroundTasks
from typing import Optional
from core.utils.generator import generator
from core.utils.messages.push import send_notification
from core.utils.messages.telegram import TelegramBotHandler as tbot  # your telegram util
from schemas.notification import NotificationType

class NotificationService:
    def __init__(self, background_tasks: BackgroundTasks):
        self.background_tasks = background_tasks

    def send(
        self,
        to_user_id: str,
        body: str,
        token: str,
        data: dict = {},
        title: Optional[str] = None,
        type: NotificationType = NotificationType.CUSTOM
    ):
        notification_id = str(generator.get_id())
        try:
            self.background_tasks.add_task(
                send_notification,
                id=notification_id,
                to_user_id=to_user_id,
                title=title,
                body=body,
                type=type,
                token=token,
                data=data
            )
            return "Notification sent successfully", None
        except Exception as e:
            return None, str(e)

    def send_telegram(
        self,
        chat_id: int,
        text: Optional[str] = None,
        photo_path: Optional[str] = None,
        document_path: Optional[str] = None,
        photo_caption: Optional[str] = None,
        document_caption: Optional[str] = None,
    ):
        
        try:
            self.background_tasks.add_task(
                tbot.send,
                chat_id=chat_id,
                text=text,
                photo_path=photo_path,
                document_path=document_path,
                photo_caption=photo_caption,
                document_caption=document_caption
            )
            return "Telegram message sent successfully", None
        except Exception as e:
            return None, str(e)
