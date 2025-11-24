# Home Recipe Assistant – 요구사항 정리 (Draft)

## 1. 목표

- 집에 있는 재료들을 DB로 관리
- 현재 재료로 만들 수 있는 레시피 추천
- (미래) 요리 사진 업로드 → 레시피/기록 기반으로 블로그 글 자동 생성

## 2. 주요 유즈케이스

- [UC-01] 재료 등록
  - 재료 이름, 수량, 보관 위치, 유통기한을 입력해 저장한다.

- [UC-02] 재료 목록 보기
  - 현재 집에 있는 재료 목록과 수량을 확인한다.

- [UC-03] 보유 재료 기반 레시피 추천 (MVP에서는 더미 데이터도 허용)
  - 보유 재료로 만들 수 있는 레시피 목록을 보여준다.

- [UC-04] 요리 기록 저장 (사진 포함)
  - 요리 날짜, 선택한 레시피, 사진, 메모를 저장한다.

- [UC-05] 블로그용 글 자동 생성 (AI 활용, 추후)
  - 요리 기록을 바탕으로 블로그용 글(제목, 본문, 재료/과정 요약)을 생성한다.

## 3. 1차 엔티티 설계 (거친 초안)

### Ingredient
- id
- name
- category (meat / vegetable / sauce / etc)
- default_unit (g / 개 / 컵 / 스푼 등)

### IngredientStock
- id
- ingredient_id (FK → Ingredient)
- amount
- unit
- storage (냉장 / 냉동 / 실온)
- expiry_date (nullable)

### Recipe
- id
- title
- description
- source_type (manual / llm / external)

### RecipeIngredient
- recipe_id (FK → Recipe)
- ingredient_id (FK → Ingredient)
- amount
- unit

### CookSession (요리 기록)
- id
- recipe_id (nullable: 자유 요리일 수도 있음)
- cooked_at (날짜/시간)
- memo

### Photo
- id
- cook_session_id (FK)
- image_path (또는 URL)

### BlogPost
- id
- cook_session_id (FK)
- title
- content
- created_at

