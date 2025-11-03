<!-- 自选列表 -->
<template>
  <div class="custom-list">
    <customItem v-for="code in fundCodeList" :key="code" :code="code"></customItem>
  </div>
</template>

<script setup lang="ts">
import customItem from './customItem.vue'
const fundCodeList: string[] = ['512480']
</script>

<style scoped></style>
