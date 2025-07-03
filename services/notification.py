from typing import Optional
from fastapi import BackgroundTasks
from core.utils.messages.push import send_notification
from schemas.notification import NotificationType  # Import your schema
from core.utils.generator import generator

class NotificationService:
    def __init__(self, background_tasks: BackgroundTasks):
        self.background_tasks = background_tasks

    def send(self,to_user_id: str,body: str, token: str, data:dict={}, title: Optional[str] = None, type: NotificationType = NotificationType.CUSTOM):
            notification_id = str(generator.get_id())
            
            try:
                self.background_tasks.add_task(
                    send_notification,id=notification_id, to_user_id=to_user_id, title=title, body=body, type=type, token=token, data = data
                )
                return "Notification sent successfully", None
            except Exception as e:
                return None, str(e)

