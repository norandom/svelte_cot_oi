<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { selectedCommodity } from '../stores'; // Verify import path
  import { createChart } from 'lightweight-charts';

  let chartContainer: HTMLDivElement;
  let chart: any; // Use any if specific type is not available
  let lineSeries: any; // This will hold the line series object

  async function fetchData(commodity: string) {
    console.log('Fetching data for:', commodity);
    const url = `http://localhost:5001/data/${commodity.toLowerCase()}`;
    const response = await fetch(url);
    const data = await response.json();
    updateChart(data);
  }

  function updateChart(data) {
    if (chartContainer) {
      if (!chart) {
        chart = createChart(chartContainer, { width: chartContainer.clientWidth, height: 300 });
        lineSeries = chart.addLineSeries(); // Ensure line series is created here
      }

      if (lineSeries) {
        lineSeries.setData(data);
      } else {
        console.error('Line series not initialized');
      }
    }
  }

  onMount(() => {
    selectedCommodity.subscribe(commodity => {
      fetchData(commodity);
    });
  });
</script>

<div bind:this={chartContainer}></div>
