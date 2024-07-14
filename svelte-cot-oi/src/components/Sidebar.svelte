<script lang="ts">
  import { selectedCommodity } from '../stores';  // Adjust the path as necessary

  // Function to handle commodity selection
    function selectCommodity(commodity: string) {
    console.log('Commodity selected:', commodity);  // Log to check function call
    selectedCommodity.set(commodity);
  }

</script>

<aside>
  <nav>
    <ul>
      <li><button on:click={() => selectCommodity('Silver')}>Silver</button></li>
      <li><button on:click={() => selectCommodity('Gold')}>Gold</button></li>
      <!-- More commodities can be added here as buttons -->
    </ul>
  </nav>
</aside>

<style>
  aside {
    background: #e2e3e5;
    width: 200px;
    padding: 20px;
  }
  button {
    display: block;
    margin: 10px 0;
    background: none;
    border: none;
    color: #333;
    text-align: left;
    width: 100%;
    padding: 10px;
    cursor: pointer;
  }
  button:hover {
    text-decoration: underline;
  }
  button:focus {
    outline: none;
    text-decoration: underline;
  }
</style>
