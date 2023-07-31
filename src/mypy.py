from typing import Iterable
import logging


def broadcast_notification(message: str, relevant_user_emails: Iterable[str]):
    for email in relevant_user_emails:
        logging.getLogger().info(f"{message} 메시지를 {email} 에게 전달")
