# backend/routers/recipe.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)

class RecipeIn(BaseModel):
    title: str
    ingredients: list[str]
    steps: list[str] | None = None

class RecipeOut(BaseModel):
    title: str
    ingredients_count: int
    preview: str

@router.post("", response_model=RecipeOut)
def create_recipe(payload: RecipeIn):
    """
    간단한 Echo용 엔드포인트:
    - 받은 title 그대로 반환
    - 재료 개수 계산
    - steps가 있으면 첫 단계만 preview로 반환
    """
    preview = ""
    if payload.steps:
        preview = payload.steps[0]

    return RecipeOut(
        title=payload.title,
        ingredients_count=len(payload.ingredients),
        preview=preview,
    )