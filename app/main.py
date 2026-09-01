from fastapi import FastAPI, Depends
from app.core.config import settings
from app.core.security import get_api_key

app = FastAPI(title=settings.APP_NAME)

@app.get("/", tags=["Health"])
async def root():
    return {"status": "online", "engine": settings.APP_NAME}

@app.get("/process", dependencies=[Depends(get_api_key)], tags=["Pipeline"])
async def trigger_pipeline():
    # Pipeline logic will be integrated here
    return {"message": "Pipeline triggered successfully"}
