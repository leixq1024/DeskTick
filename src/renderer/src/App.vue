<template>
  <main class="container">
    <!-- 标题 -->
    <header class="container-header" @mousedown="mousedown">持仓</header>
    <!-- 持仓列表 -->
    <customList />
    <bottomMenu />
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import customList from './components/customList.vue'
import bottomMenu from './components/bottomMenu.vue'

// 响应式变量
const isKeyDown = ref(false)
const coordinatesX = ref(0)
const coordinatesY = ref(0)

const mousedown = (e: MouseEvent): void => {
  isKeyDown.value = true
  coordinatesX.value = e.x
  coordinatesY.value = e.y
  document.onmousemove = (ev) => {
    if (isKeyDown.value) {
      const x = ev.screenX - coordinatesX.value
      const y = ev.screenY - coordinatesY.value
      // 给主进程传入坐标
      const data = {
        appX: x,
        appY: y
      }
      window.electron.ipcRenderer.send('custom-adsorption', data)
    }
  }
  document.onmouseup = () => {
    isKeyDown.value = false
  }
}
</script>

<style scoped></style>
