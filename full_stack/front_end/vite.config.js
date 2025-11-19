import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()], // 启用Vue插件
  server: {
    open: true // 启动时自动打开浏览器
  }
})