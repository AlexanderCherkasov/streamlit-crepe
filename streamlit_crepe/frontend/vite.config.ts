import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

export default defineConfig({
  plugins: [react()],
  define: {
    'process.env.NODE_ENV': '"production"',
    'process.env': '{}',
    'global': 'globalThis'
  },
  build: {
    outDir: 'build',
    sourcemap: false, // Disable source maps for production
    rollupOptions: {
      input: resolve(__dirname, 'src/index.tsx'),
      output: {
        entryFileNames: 'streamlit-crepe.umd.js',
        chunkFileNames: 'streamlit-crepe.[hash].js',
        assetFileNames: 'streamlit-crepe.[ext]',
        format: 'umd',
        name: 'StreamlitCrepe'
      }
    }
  },
  css: {
    devSourcemap: false, // Disable source maps for CSS in dev mode
    postcss: {
      map: false // Disable PostCSS source maps
    }
  }
})