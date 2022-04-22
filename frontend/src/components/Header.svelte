<script lang="ts">
	import { Col, Container, Row, Breadcrumb, BreadcrumbItem, Nav, NavItem } from 'sveltestrap/src';
	export let path;
	export let navLinks;
</script>

<!-- <Container fluid>
	<div class="d-flex bd-highlight mb-3">
		{#each navLinks as { name, href, childs }}
			{#if childs}
				{#each childs as childLink}
					{#if path === childLink.href}
						<div class="p-2 bd-highlight"><h1>{name} - {childLink.name}</h1></div>
						<div class="ms-auto p-2 bd-highlight align-self-center">
							<Breadcrumb>
								<BreadcrumbItem>
									<a href="/">Home</a>
								</BreadcrumbItem>
								<BreadcrumbItem>
									<a href={childLink.href}>{name}</a>
								</BreadcrumbItem>
								<BreadcrumbItem active>
									{childLink.name}
								</BreadcrumbItem>
							</Breadcrumb>
						</div>
					{/if}
				{/each}
			{:else if path === href}
				<h1>{name}</h1>
			{/if}
		{/each}
	</div>
</Container> -->

<Container fluid>
	<Row>
		{#each navLinks as { name, href, childs }}
			{#if childs}
				{#each childs as childLink}
					{#if path === childLink.href}
						<Col md="12" class="mt-3 px-3">
							<Breadcrumb class="">
								<BreadcrumbItem>
									<a href="/" class="text-decoration-none text-orange-400">Home</a>
								</BreadcrumbItem>
								<BreadcrumbItem>
									<a class="text-decoration-none text-orange-400" href={childLink.href}>{name}</a>
								</BreadcrumbItem>
								<BreadcrumbItem active>
									{childLink.name}
								</BreadcrumbItem>
							</Breadcrumb>
						</Col>
					{/if}
				{/each}
			{:else if path === href}
				<Col md="12" class="mt-3 px-3">
					<Breadcrumb class="">
						<BreadcrumbItem>
							<a href="/" class="text-decoration-none text-orange-400">Home</a>
						</BreadcrumbItem>
						<BreadcrumbItem active>
							{#if name !== 'Home'}
								{name}
							{/if}
						</BreadcrumbItem>
					</Breadcrumb>
				</Col>
			{/if}
		{/each}
	</Row>
</Container>

<!-- <div class="container-fluid bg-secondary">
	<div class="row">div.col</div>

</div> -->

<!-- <div class="container-fluid bg-secondary">
	{#each navLinks as { name, href, childs }}
		{#if childs}
			{#each childs as childLink}
				{#if path === childLink.href}
					<h1 class="float-start bg-light">{childLink.name}</h1>
					<Breadcrumb class="float-end bg-light">
						<BreadcrumbItem>
							<a href="/">Home</a>
						</BreadcrumbItem>
						<BreadcrumbItem>
							<a href={childLink.href}>{name}</a>
						</BreadcrumbItem>
						<BreadcrumbItem active>
							{childLink.name}
						</BreadcrumbItem>
					</Breadcrumb>
				{/if}
			{/each}
		{:else if path === href}
			<h1>{name}</h1>
			<Breadcrumb>
				<BreadcrumbItem active>{name}</BreadcrumbItem>
			</Breadcrumb>
		{/if}
	{/each}
</div> -->
