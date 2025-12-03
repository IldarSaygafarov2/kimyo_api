from apps.main.models.user_request import UserRequest
from constance import config

import requests


def send_user_request_to_telegram(user_request: UserRequest):
    message = f"""
Имя: {user_request.name}
Номер телефона: {user_request.phone_number}
Компания: {user_request.company}
Комментарий: {user_request.comment}
"""

    url = config.TELEGRAM_CHANNEL_USERNAME + "sendMessage"
    return requests.post(
        url,
        json={
            "chat_id": config.TELEGRAM_CHANNEL_USERNAME,
            "text": message,
        },
    )
