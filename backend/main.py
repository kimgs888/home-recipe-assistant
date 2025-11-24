from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Home Recipe Assistant API")

# 프론트 개발 서버(origin) 허용
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/ingredients")
def get_ingredients():
    # Day1: 아직 DB 없으니까 더미 데이터로 응답
    return [
        {"id": 1, "name": "양파", "amount": 3, "unit": "개"},
        {"id": 2, "name": "닭가슴살", "amount": 500, "unit": "g"},
    ]
