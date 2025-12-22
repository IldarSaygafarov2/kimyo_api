from ninja import Router
from django.http import HttpRequest
from apps.api.schemas.user_request import UserRequestCreationSchema, UserRequestSchema
from apps.main.models import UserRequest
from apps.main.utils import send_user_request_to_telegram


router = Router(tags=["Заявки пользователей"])


@router.post("/send/", response=UserRequestSchema)
def send_user_request(request: HttpRequest, data: UserRequestCreationSchema):
    user_request = UserRequest.objects.create(**data.model_dump())

    sent_request = send_user_request_to_telegram(user_request)
    print(sent_request)
    return user_request
