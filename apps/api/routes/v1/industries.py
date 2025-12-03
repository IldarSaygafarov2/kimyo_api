from ninja import Router
from django.http import HttpRequest
from apps.main.models import Industry
from apps.api.schemas.industry import IndustrySchema


router = Router(
    tags=["Отрасли"],
)


@router.get("/", response=list[IndustrySchema])
def get_industries(request: HttpRequest):
    items = Industry.objects.all()
    return items
