<script setup>
import { ref, onMounted } from "vue";
import apiClient from "./api/client";

const pingMessage = ref("Loading...");
const errorMessage = ref("");

onMounted(async () => {
  try {
    const res = await apiClient.get("/ping");
    // FastAPI에서 {"message": "pong"} 반환
    pingMessage.value = res.data.message;
  } catch (err) {
    console.error(err);
    errorMessage.value = "백엔드 서버에 연결할 수 없습니다.";
  }
});
</script>

<template>
  <main>
    <h1>Home Recipe Assistant – DAY2</h1>

    <section>
      <h2>백엔드 통신 상태</h2>
      <p>Ping 결과: {{ pingMessage }}</p>
      <p v-if="errorMessage" style="color: red">
        {{ errorMessage }}
      </p>
    </section>
  </main>
</template>

<style scoped>
main {
  padding: 2rem;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI",
    sans-serif;
}

h1 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
}

h2 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}
</style>
