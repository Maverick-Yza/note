<template>
  <div class="test-container">
    <h1>Vue 测试页面 🚀</h1>
    <p>这是一个用于验证 Vue 环境的测试组件</p>

    <!-- 1. 数据绑定示例 -->
    <div class="demo-section">
      <h3>1. 数据绑定</h3>
      <p>当前时间: {{ currentTime }}</p>
      <input
        type="text"
        v-model="message"
        placeholder="输入内容..."
      >
      <p>你输入的内容: {{ message }}</p>
    </div>

    <!-- 2. 事件处理示例 -->
    <div class="demo-section">
      <h3>2. 事件处理</h3>
      <button @click="count++">点击计数 (当前: {{ count }})</button>
      <button @click="resetCount" style="margin-left: 10px;">重置计数</button>
    </div>

    <!-- 3. 条件渲染示例 -->
    <div class="demo-section">
      <h3>3. 条件渲染</h3>
      <button @click="showSecret = !showSecret">
        {{ showSecret ? '隐藏' : '显示' }} 秘密内容
      </button>
      <p v-if="showSecret" class="secret">🎉 你发现了隐藏的秘密！</p>
    </div>

    <!-- 4. 列表渲染示例 -->
    <div class="demo-section">
      <h3>4. 列表渲染</h3>
      <ul>
        <li v-for="(item, index) in fruits" :key="index">
          {{ index + 1 }}. {{ item }}
        </li>
      </ul>
      <input
        type="text"
        v-model="newFruit"
        placeholder="添加水果..."
      >
      <button @click="addFruit">添加</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 数据定义
const message = ref('') // 双向绑定的输入内容
const count = ref(0) // 计数器
const showSecret = ref(false) // 控制条件渲染
const fruits = ref(['苹果', '香蕉', '橙子']) // 列表数据
const newFruit = ref('') // 新添加的水果
const currentTime = ref('') // 当前时间

// 方法定义
const resetCount = () => {
  count.value = 0
}

const addFruit = () => {
  if (newFruit.value.trim()) {
    fruits.value.push(newFruit.value.trim())
    newFruit.value = '' // 清空输入框
  }
}

// 生命周期钩子：页面加载时获取当前时间
onMounted(() => {
  const updateTime = () => {
    currentTime.value = new Date().toLocaleString()
  }
  updateTime() // 初始化
  setInterval(updateTime, 1000) // 每秒更新一次
})
</script>

<style scoped>
.test-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 0 20px;
  font-family: Arial, sans-serif;
}

.demo-section {
  margin: 30px 0;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 8px;
  background-color: #f9f9f9;
}

button {
  padding: 6px 12px;
  cursor: pointer;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #359e75;
}

.secret {
  color: #e74c3c;
  font-weight: bold;
  margin-top: 10px;
}

input {
  padding: 6px;
  margin: 0 5px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>