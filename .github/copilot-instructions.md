# Copilot Instructions for Home Recipe Assistant

## Project Overview
- **Architecture:**
  - Monorepo with `backend` (FastAPI) and `frontend` (Vue 3 + Vite).
  - Frontend and backend communicate via HTTP (REST API).
  - Backend exposes `/health` and `/ingredients` endpoints (ingredients are mock data for now).
  - CORS is enabled for local frontend dev servers.

## Key Workflows
- **Backend:**
  - Start dev server: `uvicorn backend.main:app --reload`
  - Dependencies: see `backend/requirements.txt` (FastAPI, uvicorn)
  - No database yet; ingredient data is hardcoded in `main.py`.
- **Frontend:**
  - Start dev server: `npm run dev` in `frontend/`
  - Build: `npm run build`
  - Preview: `npm run preview`
  - Main entry: `frontend/src/main.js`, root component: `frontend/src/App.vue`

## Conventions & Patterns
- **API endpoints:**
  - All backend endpoints are defined in `backend/main.py`.
  - Frontend fetches from `http://localhost:8000` (see `App.vue`).
- **Component structure:**
  - Vue SFCs in `frontend/src/components/`
  - Use `<script setup>` syntax for Vue components.
- **Styling:**
  - Global styles in `frontend/src/style.css`
- **Cross-component communication:**
  - Currently simple, no Vuex/Pinia or global state management.

## Integration Points
- **Frontend <-> Backend:**
  - REST API calls (fetch) from Vue components to FastAPI endpoints.
  - CORS configured for local dev (`localhost:5173`).
- **External dependencies:**
  - Backend: FastAPI, uvicorn
  - Frontend: Vue 3, Vite

## Examples
- **Add a new backend endpoint:**
  - Edit `backend/main.py`, define a new route with `@app.get` or `@app.post`.
- **Fetch new data in frontend:**
  - Add fetch logic in `App.vue` or a component, update template to display results.

## References
- See `README.md` (root) for project summary.
- See `frontend/README.md` for Vue/Vite usage tips.
- See `backend/main.py` and `frontend/src/App.vue` for main data flow.

---
_Keep instructions concise and specific to this codebase. Update this file if major architecture or workflow changes occur._
