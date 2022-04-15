<script>
	const fetchInventory = (async () => {
		const response = await fetch('http://127.0.0.1:8000/inventory');
		return await response.json();
	})();
</script>

<h1>Inventory Page</h1>
{#await fetchInventory}
	<p>...waiting</p>
{:then data}
	<table class="table table-dark">
		<thead>
			<tr>
				<th scope="col">Hostname</th>
				<th scope="col">IP Address</th>
				<th scope="col">Type</th>
				<th scope="col">Role</th>
				<th scope="col">Groups</th>
			</tr>
		</thead>
		<tbody>
			{#each data.message as device}
				<tr>
					<td>{device[0]}</td>
					<td>{device[1]}</td>
					<td>{device[2]}</td>
					<td>{device[3]}</td>
					<td>{device[4]}</td>
				</tr>
			{/each}
		</tbody>
	</table>
{:catch error}
	<p>An error occurred!</p>
	<p>{error}</p>
{/await}
