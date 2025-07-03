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
