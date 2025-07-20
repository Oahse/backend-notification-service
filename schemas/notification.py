from enum import Enum
from typing import Optional
from pydantic import BaseModel

class NotificationType(str, Enum):
    MESSAGE = "message"
    ALERT = "alert"
    REMINDER = "reminder"
    SYSTEM = "system"
    CUSTOM = "custom"

class NotificationCreate(BaseModel):
    to_user_id: str
    body: str
    title: Optional[str] = None
    token: str
    data: dict ={}
    type: NotificationType = NotificationType.CUSTOM


class TelegramNotificationCreate(BaseModel):
    chat_id: int
    text: Optional[str]
    photo_path: Optional[str]
    document_path: Optional[str]
    photo_caption: Optional[str]
    document_caption: Optional[str]
