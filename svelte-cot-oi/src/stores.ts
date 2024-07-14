import { writable } from 'svelte/store';

// Define a type for the commodity
type Commodity = 'Silver' | 'Gold';

// Create a writable store of type Commodity, with a default value
export const selectedCommodity = writable<Commodity>('Silver');
