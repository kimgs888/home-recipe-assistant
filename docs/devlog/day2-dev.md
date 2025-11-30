# DAY2 – 기본 API & 프론트 통신 구축

> 목표: **FastAPI 기본 엔드포인트 + Vue(onMounted)에서 호출 → 화면에 표시**  
> + 폴더 구조, uvicorn 옵션, Git 브랜치 전략 정리

---

## 1. FastAPI 기본 엔드포인트 만들기

### 1-1. 현재 구조(예시)

백엔드 쪽 디렉터리 구조를 아래처럼 맞춰 둔다고 가정:

```text
backend/
  ├─ main.py
  ├─ routers/
  │    ├─ __init__.py
  │    ├─ ping.py
  │    └─ recipe.py
  └─ models/   (오늘은 안 써도 됨, 나중에 확장용)
