import requests
from constance import config
from core.settings import TELEGRAM_API_URL
from apps.main.models.user_request import UserRequest


def send_user_request_to_telegram(user_request: UserRequest):
    message = f"""
Имя: <b>{user_request.name}</b>
Номер телефона: <b>{user_request.phone_number}</b>
Компания: <b>{user_request.company}</b>
Комментарий: <b>{user_request.comment}</b>
"""
    return requests.post(
        TELEGRAM_API_URL + "sendMessage",
        json={
            "chat_id": config.TELEGRAM_CHANNEL_USERNAME,
            "text": message,
            "parse_mode": "HTML"
        },
    )
