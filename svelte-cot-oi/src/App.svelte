<script lang="ts">
  import Header from './components/Header.svelte';
  import Footer from './components/Footer.svelte';
  import Sidebar from './components/Sidebar.svelte';
  import COTChart from './lib/COTchart.svelte';

</script>

<div class="app">
  <Header />

  <div class="main-content">
    <Sidebar />
    <main>
      <h1>Commitment of Traders - Silver Open Interest</h1>
      <p>Just a test.</p>
      <COTChart />
    </main>
  </div>

  <Footer />
</div>

<style>
  .app {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }
  .main-content {
    display: flex;
    flex: 1;
  }
  main {
    flex: 1;
    padding: 20px;
  }
</style>
