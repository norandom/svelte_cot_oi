import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import type { UserConfig } from 'vite';


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
})
