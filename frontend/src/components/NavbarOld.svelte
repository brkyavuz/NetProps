<script>
	import { page } from '$app/stores';
	let path;

	$: path = $page.url.pathname;

	export let navItems = [
		{
			name: 'Home',
			href: '/'
		},
		{
			name: 'Dashboard',
			href: '/dashboard'
		},
		{
			name: 'Inventory',
			href: '/inventory'
		},
		{
			name: 'Change Management',
			href: '/',
			childs: [
				{
					name: 'Templates',
					href: '/cm/templates'
				},
				{
					name: 'Get Config',
					href: '/cm/getconfig'
				},
				{
					name: 'Send Config',
					href: '/cm/sendconfig'
				}
			]
		}
	];
</script>

<nav
	class="navbar navbar-expand-lg navbar-dark bg-neutral-900 border-bottom border-2 border-orange-500"
>
	<div class="container-fluid">
		<a class="navbar-brand" href="/">NetProps</a>
		<button
			class="navbar-toggler"
			type="button"
			data-bs-toggle="collapse"
			data-bs-target="#navbarToggler"
			aria-controls="navbarToggler"
			aria-expanded="false"
			aria-label="Toggle navigation"
		>
			<span class="navbar-toggler-icon" />
		</button>
		<div class="collapse navbar-collapse" id="navbarToggler">
			<ul class="navbar-nav me-auto mb-2 mb-lg-0">
				{#each navItems as { name, href, childs }}
					{#if childs}
						<li class="nav-item dropdown">
							<a
								class="nav-link dropdown-toggle {childs.map(({ href }) => href).includes(path)
									? 'active'
									: ''}"
								href="/"
								id="navbarDropdown"
								role="button"
								data-bs-toggle="dropdown"
								aria-expanded="false"
							>
								{name}
							</a>
							<ul class="dropdown-menu bg-zinc-800" aria-labelledby="navbarDropdown">
								{#each childs as dropdownItem}
									<li>
										<a
											class="dropdown-item text-slate-300 {path === dropdownItem.href
												? 'active'
												: ''}"
											href={dropdownItem.href}>{dropdownItem.name}</a
										>
									</li>
								{/each}
							</ul>
						</li>
					{:else}
						<li class="nav-item">
							<a class="nav-link {path === href ? 'active' : ''}" aria-current="page" {href}
								>{name}</a
							>
						</li>
					{/if}
				{/each}
			</ul>
			<form class="d-flex">
				<input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
				<button class="btn btn-outline-light" type="submit">Search</button>
			</form>
		</div>
	</div>
</nav>
