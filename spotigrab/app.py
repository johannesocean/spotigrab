import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api import router as api_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['GET', 'POST'],
    allow_headers=['*'],
)

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='127.0.0.1',
        port=5000,
        log_level='info',
        reload=True
    )
