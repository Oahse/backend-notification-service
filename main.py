from fastapi import FastAPI, Request
from core.config import Settings
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from routes.email import router as user_router
from routes.notification import router as notification_router
from core.utils.response import Response, RequestValidationError 

app = FastAPI(
    title="Notification Service API",
    description="API to handle sending email and push notifications to users.",
    version="1.0.0"
)
settings = Settings()

# Add CORS middleware if configured
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip("/") for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

        
# Include the routers
app.include_router(user_router)
app.include_router(notification_router)


@app.get("/")
async def read_root():
    return {
        "service": "Notification Service API",
        "status": "Running",
        "version": "1.0.0",
        
    }

# Handle validation errors globally
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        e = {
            "type": error.get("type"),
            "loc": error.get("loc"),
            "msg": error.get("msg"),
        }
        if "ctx" in error:
            e["ctx"] = error["ctx"]
        errors.append(e)

    # If only one error, return as a single object
    message = errors[0] if len(errors) == 1 else errors


    return Response(message=message, success=False, code=422)


