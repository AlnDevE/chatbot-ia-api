from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat_router

#Para iniciar o projeto
# python -m uvicorn server:app
app = FastAPI()

# configuração de CORS
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router.router)