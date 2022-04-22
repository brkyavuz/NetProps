<script lang="ts">
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
	export let path;
	export let navLinks;
</script>

<Navbar light expand="lg" class="navbar-dark bg-zinc-900 border-bottom border-2 border-orange-500">
	<NavbarBrand href="/"><img src="/netprobe_logo.png" alt="NetProbe" /></NavbarBrand>
	<NavbarToggler on:click={() => (isOpen = !isOpen)} />
	<Collapse {isOpen} navbar expand="lg" on:update={handleUpdate}>
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
						<DropdownMenu end class="bg-zinc-900">
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
