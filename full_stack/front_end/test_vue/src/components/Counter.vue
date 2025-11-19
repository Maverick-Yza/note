<template>
  <div class="counter">
    <!-- 显示当前计数（数据绑定） -->
    <h2>当前计数：{{ count }}</h2>

    <!-- 条件渲染：当 count 为 0 时显示提示 -->
    <p v-if="count === 0" class="tip">提示：已归零啦~</p>

    <!-- 事件处理：点击按钮修改 count -->
    <button @click="increment">+ 增加</button>
    <button @click="decrement" :disabled="count <= 0">- 减少</button>
  </div>
</template>

<script setup>
// Vue 3 语法：使用 setup 脚本（无需 export default）
import { ref } from 'vue'

// 定义响应式数据（count 初始值为 0）
const count = ref(0)

// 定义增加计数的方法
const increment = () => {
  count.value++  // ref 数据需要通过 .value 访问/修改
}

// 定义减少计数的方法（最低为 0）
const decrement = () => {
  if (count.value > 0) {
    count.value--
  }
}
</script>

<style scoped>
/* 组件样式（scoped 表示样式仅作用于当前组件） */
.counter {
  text-align: center;
  margin: 50px auto;
  width: 300px;
}

button {
  margin: 0 10px;
  padding: 8px 16px;
  cursor: pointer;
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.6;
}

.tip {
  color: #666;
  font-size: 14px;
}
</style>