<!-- 底部菜单 -->
<template>
  <footer class="bottom-menu">
    <img src="../assets/img/设置.svg" alt="设置" />
    <img src="../assets/img/退出.svg" alt="退出" />
  </footer>
</template>

<script setup lang="ts"></script>

<style lang="css" scoped>
.bottom-menu {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
  padding: 0 12px;
  box-sizing: border-box;
}
img {
  width: 18px;
  height: 18px;
  cursor: pointer;
}
img:nth-of-type(2) {
  width: 22px;
  height: 22px;
}
</style>
