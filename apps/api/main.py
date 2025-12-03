from ninja import NinjaAPI
from .routes import router as api_router


api = NinjaAPI(
    title="Kimyo site api",
)

api.add_router("", api_router)
