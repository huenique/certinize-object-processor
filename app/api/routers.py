import fastapi

from app.api.endpoints import certificates, templates

router = fastapi.APIRouter()
router.include_router(templates.router)
router.include_router(certificates.router)
