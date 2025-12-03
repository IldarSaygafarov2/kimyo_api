from ninja import Router
from .v1.categories import router as categories_router
from .v1.products import router as products_router
from .v1.industries import router as industries_router
from .v1.user_requests import router as user_requests_router


router = Router()

router.add_router("/v1/categories/", categories_router)
router.add_router("/v1/products/", products_router)
router.add_router("/v1/industries/", industries_router)
router.add_router("/v1/user_requests/", user_requests_router)
