# Day 1 – 프로젝트 셋업 기록

## 1. 목표

- GitHub 레포 생성 및 기본 구조 세팅
- FastAPI 백엔드 초기 셋업 (`/health`, `/ingredients` 엔드포인트)
- Vue 3 + Vite 프론트엔드 초기 셋업
- 프론트엔드에서 백엔드 API 호출 성공
- 오늘 사용한 주요 개념(FastAPI, uvicorn, CORS, Vite, onMounted 등) 정리

---

## 2. 프로젝트 디렉토리 구조

```
home-recipe-assistant/
  backend/
  frontend/
  docs/
  .gitignore
  README.md
```

---

## 3. Git 작업 내역

```bash
# 초기 작업
git clone <repo-url>
cd home-recipe-assistant
mkdir backend frontend docs
git add backend frontend docs
git commit -m "Initial project setup"
git push origin main
```

---

## 4. FastAPI 백엔드 셋업

### 4.1 가상환경 생성 및 패키지 설치

```bash
cd backend

# 가상환경 생성
python -m venv .venv

# Git Bash
source .venv/Scripts/activate
# PowerShell
# .\.venv\Scripts\Activate.ps1

# FastAPI + Uvicorn 설치
pip install fastapi "uvicorn[standard]"

# requirements.txt 생성
echo "fastapi
uvicorn[standard]" > requirements.txt
```

### 4.2 서버 실행

```bash
uvicorn main:app --reload
```

---

## 5. `backend/main.py` 코드 예시

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Home Recipe Assistant API")

# CORS 설정
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
    return [
        {"id": 1, "name": "양파", "amount": 3, "unit": "개"},
        {"id": 2, "name": "닭가슴살", "amount": 500, "unit": "g"},
    ]
```

---

## 6. Vue 3 + Vite 프론트엔드 셋업

### 6.1 프로젝트 생성

```bash
cd ../frontend

npm create vite@latest . -- --template vue
npm install
npm run dev
```

---

## 7. `frontend/src/App.vue` 코드 예시

```vue
<script setup>
import { ref, onMounted } from 'vue'

const health = ref(null)
const ingredients = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const healthRes = await fetch('http://localhost:8000/health')
    if (!healthRes.ok) throw new Error('Health check failed')
    health.value = await healthRes.json()

    const ingRes = await fetch('http://localhost:8000/ingredients')
    if (!ingRes.ok) throw new Error('Failed to load ingredients')
    ingredients.value = await ingRes.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main style="padding: 24px;">
    <h1>Home Recipe Assistant</h1>

    <section>
      <h2>Backend Health</h2>
      <pre v-if="health">{{ health }}</pre>
      <div v-else-if="loading">로딩 중...</div>
      <div v-else-if="error" style="color:red;">{{ error }}</div>
    </section>

    <section style="margin-top:24px;">
      <h2>Ingredients (Mock)</h2>
      <ul>
        <li v-for="item in ingredients" :key="item.id">
          {{ item.name }} - {{ item.amount }}{{ item.unit }}
        </li>
      </ul>
    </section>
  </main>
</template>
```

---

## 8. Day 1 – 사용한 주요 개념 정리

### 8.1 FastAPI란?
- Python 기반 ASGI 웹 프레임워크
- 빠름, 비동기(Async) 지원
- 타입 힌트 기반 자동 문서화 (Swagger UI)
- Pydantic으로 요청/응답 검증

### 8.2 uvicorn이란?
- FastAPI를 구동하는 ASGI 서버
- 실행: `uvicorn main:app --reload`
  - `main` → main.py
  - `app` → FastAPI 인스턴스

### 8.3 --reload 옵션
- 개발 환경 전용 옵션
- 코드 변경 시 서버 자동 재시작
- 배포 환경에서는 사용 금지

### 8.4 npm create vite@latest . -- --template vue
- Vite 기반 Vue 프로젝트를 현재 폴더에 생성

### 8.5 CORS & CORSMiddleware
- 서로 다른 Origin(도메인/포트) 간 호출 허용 설정
- 프론트(5173) → 백엔드(8000)는 Origin이 다르므로 CORS 필요

### 8.6 Middleware란?
- 요청/응답이 엔드포인트에 도달하기 전·후 실행되는 레이어
- 대표 용도: CORS, 인증, 로깅, 공통 헤더 설정

### 8.7 Vue의 onMounted 동작 순서
- 컴포넌트 렌더링 → DOM 생성 → onMounted 콜백 실행
- API 호출 후 응답 값에 따라 화면 자동 갱신 (ref 변화 감지)

---