from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):

    def __init__(self, message):
        self.message = message

    def send(self):
        print(self.message)


class SMSNotification(Notification):

    def __init__(self, message):
        self.message = message

    def send(self):
        print(self.message)


class PushNotification(Notification):

    def __init__(self, message):
        self.message = message

    def send(self):
        print(self.message)


email = EmailNotification("Email sent: Hello Victor")
sms = SMSNotification("SMS sent: Hello Victor")
push = PushNotification("Push notification sent: Hello Victor")

notifications = [email, sms, push]

for notification in notifications:
    notification.send()