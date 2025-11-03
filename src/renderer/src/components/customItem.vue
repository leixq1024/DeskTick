<!-- 持仓项 -->
<template>
  <article class="custom-item">
    <!-- 信息 -->
    <section class="name">
      <span>{{ fundInfo.name }}</span>
      <span>代码:{{ fundInfo.fundcode }}</span>
    </section>
    <!-- 净值 -->
    <section class="info">
      <span class="net-value"> {{ fundInfo.gsz }}</span>
      <span
        :class="{
          rise: parseFloat(fundInfo.gszzl) > 0,
          fall: parseFloat(fundInfo.gszzl) < 0
        }"
      >
        {{ fundInfo.gszzl }}%</span
      >
    </section>
  </article>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
const { code } = defineProps({ code: String })
const fundInfo = ref<{
  name: string
  code: string
  netWorth: string
  dailyGrowth: string
}>({ name: '', code: '', netWorth: '', dailyGrowth: '' })
const updateFundInfo = async () => {
  const fundData = await window.electron.ipcRenderer.invoke('get-fund-data', code)
  fundInfo.value = JSON.parse(fundData.replaceAll('jsonpgz(', '').replaceAll(');', ''))
}
onMounted(() => {
  updateFundInfo()
})
</script>

<style scoped>
.custom-item {
  display: flex;
  justify-content: space-between;
}
.name,
.info {
  color: #fff;
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  gap: 12px;
}
.name span:first-child {
  font-size: 14px;
  letter-spacing: 1px;
}

.name span:last-child {
  font-size: 12px;
  color: #7c7d81;
  letter-spacing: 1px;
}
.net-value {
  font-size: 16px;
}
.rise {
  color: #e86a45;
}
.fall {
  color: #62ca78;
}
</style>
