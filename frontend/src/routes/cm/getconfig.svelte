<script lang="ts">
	import { Container, Row, Alert, Button, Form, FormGroup, Input, Label } from 'sveltestrap/src';

	let commands = '';
	let results = null;

	async function commandsPost() {
		const res = await fetch('http://localhost:8000/cm/getconfig', {
			headers: {
				'Content-Type': 'application/json'
			},
			method: 'POST',
			body: JSON.stringify({ commands })
		});

		const response = await res.json();
		results = Object.entries(response.results);
	}
</script>

<Container>
	<Row>
		<Form>
			<FormGroup>
				<Label for="commands">Enter the commands with new lines</Label>
				<Input type="textarea" name="commands" id="commands" bind:value={commands} />
			</FormGroup>
			<button class="btn btn-light w-100 float-end" type="button" on:click={commandsPost}>
				Get
			</button>
			<!-- <Button on:click={commandsPost}>Send</Button> -->
		</Form>
	</Row>
	<Row class="mt-3">
		{#if results}
			{#each results as [host, result]}
				{#if result[0].failed}
					<Alert color="danger">
						<h4 class="alert-heading text-capitalize">{host}</h4>
						<pre>{result[0].result}</pre>
					</Alert>
				{:else}
					<Alert color="success">
						<h4 class="alert-heading text-capitalize">{host}</h4>
						<pre>{result[0].result}</pre>
					</Alert>
				{/if}
			{/each}
		{/if}
	</Row>
</Container>
