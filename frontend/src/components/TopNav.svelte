<script lang="ts">
	import { page } from '$app/stores';
	let path;
	$: path = $page.url.pathname;

	import {
		Collapse,
		Navbar,
		NavbarToggler,
		NavbarBrand,
		Nav,
		NavItem,
		NavLink,
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem
	} from 'sveltestrap';

	let isOpen = false;

	function handleUpdate(event) {
		isOpen = event.detail.isOpen;
	}

	// My Variables
	const navLinks = [
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

<Navbar light expand="lg" class="navbar-dark border-bottom border-2 border-orange-500">
	<NavbarBrand href="/">NetProbe</NavbarBrand>
	<NavbarToggler on:click={() => (isOpen = !isOpen)} />
	<Collapse {isOpen} navbar expand="md" on:update={handleUpdate}>
		<Nav class="ms-auto" navbar>
			{#each navLinks as { name, href, childs }}
				{#if childs}
					<Dropdown nav inNavbar>
						<DropdownToggle
							nav
							caret
							class={childs.map(({ href }) => href).includes(path) ? 'active' : ''}
							>{name}</DropdownToggle
						>
						<DropdownMenu end class="bg-zinc-800">
							{#each childs as dropdownItem}
								<DropdownItem
									href={dropdownItem.href}
									class="text-slate-300 {path === dropdownItem.href ? 'active' : ''}"
									>{dropdownItem.name}</DropdownItem
								>
							{/each}
						</DropdownMenu>
					</Dropdown>
				{:else}
					<NavItem>
						<NavLink {href} class={path === href ? 'active' : ''}>{name}</NavLink>
					</NavItem>
				{/if}
			{/each}
		</Nav>
	</Collapse>
</Navbar>
