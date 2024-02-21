from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.htmx import router as htmx_router

app = FastAPI()


app.include_router(htmx_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
