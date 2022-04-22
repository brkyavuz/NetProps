<script>
	import { page } from '$app/stores';
	export let path;
	$: path = $page.url.pathname;

	export const navLinks = [
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
			href: '/cm',
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

	import TopNav from '../components/TopNav.svelte';
	import Header from '../components/Header.svelte';
</script>

<TopNav {path} {navLinks} />
<Header {path} {navLinks} />
<div class="container-fluid">
	<slot />
</div>
