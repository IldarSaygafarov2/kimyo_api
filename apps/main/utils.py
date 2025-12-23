from datetime import timedelta

import requests
from constance import config

from apps.main.models.user_request import UserRequest
from core.settings import TELEGRAM_API_URL


def send_user_request_to_telegram(user_request: UserRequest):
    correct_time = user_request.created_at + timedelta(hours=5)
    message = f"""
Имя: <b>{user_request.name}</b>
Номер телефона: <b>{user_request.phone_number}</b>
Компания: <b>{user_request.company}</b>
Комментарий: <b>{user_request.comment}</b>
Дата отправки: <b>{correct_time.strftime("%Y-%m-%d %H:%M:%S")}</b>
"""
    return requests.post(
        TELEGRAM_API_URL + "sendMessage",
        json={
            "chat_id": config.TELEGRAM_CHANNEL_USERNAME,
            "text": message,
            "parse_mode": "HTML",
        },
    )
