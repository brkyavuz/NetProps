<script>
	import { Table } from 'sveltestrap/src';

	const fetchInventory = (async () => {
		const response = await fetch('http://127.0.0.1:8000/inventory');
		return await response.json();
	})();
</script>

{#await fetchInventory}
	<p>...waiting</p>
{:then data}
	<Table dark responsive striped>
		<thead>
			<tr>
				<th>Hostname</th>
				<th>Address</th>
				<th>Groups</th>
				<th>Model</th>
			</tr>
		</thead>
		<tbody>
			{#each data.message as device}
				<tr>
					<td>{device[0]}</td>
					<td>{device[1]}</td>
					<td>{device[2]}</td>
					<td>{device[3]}</td>
				</tr>
			{/each}
		</tbody>
	</Table>
{:catch error}
	<p>An error occurred!</p>
	<p>{error}</p>
{/await}
