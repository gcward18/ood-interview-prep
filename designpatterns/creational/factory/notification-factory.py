from abc import abstractmethod, ABC
from enum import Enum

'''
You’re designing a system that sends notifications to users via different channels: Email, SMS, and Push Notification.

Each notification type has its own way of sending messages:
- EmailSender sends via SMTP.
- SMSSender sends via a third-party SMS API.
- PushSender sends via a mobile push service.

You need to implement a solution that:
- Accepts a notification_type (like 'email', 'sms', or 'push')
- Returns the appropriate sender class without exposing the instantiation logic to the client.

This is a strong candidate for the Factory Pattern, as it decouples client code from object instantiation.

🧪 Requirements
- Define a common interface (e.g., NotificationSender) with a send(message) method.
- Implement three concrete classes: EmailSender, SMSSender, PushSender.
- Use a factory class/function (NotificationFactory) to instantiate the correct sender.
- Simulate a few sends in a main-like block.
'''
class NotificationSender(ABC):
    @abstractmethod
    def send(self, sender: str, recipient: str, message: str):
        pass

class EmailSender(NotificationSender):
    def send(self, sender: str, recipient: str, message: str):
        print(f"Email Message\nFrom: {sender}\nTo: {recipient}\nMessage: {message}\n")

class SMSSender(NotificationSender):
    def send(self, sender: str, recipient: str, message: str):
        print(f"SMS Message\nFrom: {sender}\nTo: {recipient}\nMessage: {message}\n")
        
class PushSender(NotificationSender):
    def send(self, sender: str, recipient: str, message: str):
        print(f"Push Message From: {sender}\nTo: {recipient}\nMessage: {message}\n")

class NotificationType(Enum):
    EMAIL   = "EMAIL"
    SMS     = "SMS"
    PUSH    = "PUSH"

class NotificationFactory:
    @staticmethod
    def create_notification_sender(notification_type: NotificationType):
        match notification_type:
            case NotificationType.EMAIL:
                return EmailSender()
            case NotificationType.SMS:
                return SMSSender()
            case NotificationType.PUSH:
                return PushSender()

if __name__ == "__main__":
    notification_factory = NotificationFactory()
    sms = notification_factory.create_notification_sender(NotificationType.SMS)
    email = notification_factory.create_notification_sender(NotificationType.EMAIL)
    push = notification_factory.create_notification_sender(NotificationType.PUSH)
    
    sms.send("George Ward", "Phillip Mejia", "Yo!")
    email.send("George Ward", "Phillip Mejia", "Check your inbox.")
    push.send("George Ward", "Phillip Mejia", "New message for you!")
    