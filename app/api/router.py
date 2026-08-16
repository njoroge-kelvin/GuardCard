from fastapi import APIRouter

# The below code is commented out because it is not used in the current implementation. 
# Uncomment  when the corresponding endpoints are implemented.:
# from app.api.endpoints import users, auth
#
# api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])

api_router = APIRouter()


@api_router.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}