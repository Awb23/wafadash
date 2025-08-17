// front/vite.config.js

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

export default defineConfig({
  plugins: [react()],

  // ✅ ADD THIS 'base' OPTION
  // This tells Vite to build all asset links with a /static/ prefix
  base: '/static/',
})