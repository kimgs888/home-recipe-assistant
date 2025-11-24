<script setup>
import { ref, onMounted } from 'vue'

const health = ref(null)
const ingredients = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    // 백엔드 헬스 체크
    const healthRes = await fetch('http://localhost:8000/health')
    if (!healthRes.ok) {
      throw new Error('Health check failed')
    }
    health.value = await healthRes.json()

    // 재료 목록 호출
    const ingRes = await fetch('http://localhost:8000/ingredients')
    if (!ingRes.ok) {
      throw new Error('Failed to fetch ingredients')
    }
    ingredients.value = await ingRes.json()
  } catch (e) {
    console.error(e)
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <main style="padding: 24px; font-family: system-ui, -apple-system, BlinkMacSystemFont;">
    <h1>Home Recipe Assistant</h1>

    <section style="margin-top: 16px;">
      <h2>Backend Health</h2>
      <div v-if="loading">로딩 중...</div>
      <div v-else-if="error">
        <strong style="color: red;">에러:</strong> {{ error }}
      </div>
      <pre v-else>{{ health }}</pre>
    </section>

    <section style="margin-top: 24px;">
      <h2>Ingredients (Mock Data)</h2>
      <ul v-if="ingredients.length">
        <li v-for="item in ingredients" :key="item.id">
          {{ item.name }} - {{ item.amount }}{{ item.unit }}
        </li>
      </ul>
      <p v-else>재료 데이터가 없습니다.</p>
    </section>
  </main>
</template>

<style>
body {
  margin: 0;
}
</style>
