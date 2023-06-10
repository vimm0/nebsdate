<script>
	import constants from "../lib/utils/constants";
	import { yearsState, currentYearMonthState } from "../store";
	import { onDestroy, onMount } from "svelte";
	import en2neNumbers from "../lib/utils/en2neNumbers";
	import ne2enNumbers from "../lib/utils/ne2enNumbers";
	import getBS from "../lib/utils/getBS";
	import Din from "../components/Din.svelte";
	import { _ } from "../i18n";

	const DEFAULT_LANG = "ne";
	const nepaliLongDays = [
		"आइतबार",
		"सोमबार",
		"मंगलबार",
		"बुधवार",
		"बिहीवार",
		"शुक्रवार",
		"शनिवार",
	];
	const nepaliShortDays = [
		"आइत",
		"सोम",
		"मंगल",
		"बुध",
		"बिही",
		"शुक्र",
		"शनि",
	];
	const englishLongDays = [
		"Sunday",
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday",
	];
	const englishShortDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

	$: data = "";
	$: title = "";
	$: subtitle = "";

	let today = new Date();
	let currentYearMonth = {};
	today = {
		year: today.getFullYear(),
		month: today.getMonth() + 1,
		date: today.getDate(),
	};
	let locale = DEFAULT_LANG;
	const date = `${today.year}-${today.month}-${today.date}`;
	const todayBs = getBS(today.year, today.month, today.date);
	const dateBs = `${todayBs.year}-${todayBs.month}-${todayBs.date}`;

	console.log(todayBs);
	$: if (data) {
		const dateAD = new Date(data[0].ad);
		title = `${constants.monthsBS[+currentYearMonth.month - 1][locale]} ${
			locale === DEFAULT_LANG
				? en2neNumbers(currentYearMonth.year)
				: currentYearMonth.year
		}`;
		subtitle = `${constants.monthsAD[dateAD.getMonth()]}/${
			constants.monthsAD[dateAD.getMonth() + 1]
		} ${dateAD.getFullYear()}`;
	}
	$: isToday = (ad) => {
		return (
			ad
				.split("-")
				.filter(
					(x, i) =>
						[today.year, today.month, today.date][i] === parseInt(x)
				).length === 3
		);
	};
	$: getInDays = (ad) => {
		// let daysDiff = Math.round(
		// 	(new Date(`${today.year}-${today.month}-${today.date}`).getTime() -
		// 		new Date(ad).getTime()) /
		// 		8.64e7
		// );
		// let inDays = $_(
		// 	daysDiff === 0
		// 		? "today"
		// 		: daysDiff === 1
		// 		? "yesterday"
		// 		: daysDiff === -1
		// 		? "tomorrow"
		// 		: ""
		// );
		// inDays =
		// 	inDays ||
		// 	`${
		// 		locale === "ne"
		// 			? en2neNumbers(Math.abs(daysDiff))
		// 			: Math.abs(daysDiff)
		// 	} ${$_(daysDiff > 1 ? "daysBefore" : "daysLeft")}`;
		// return inDays;
	};
	currentYearMonthState.subscribe((yearMonth) => {
		if (yearMonth) {
			const [year, month] = yearMonth.split("-");
			currentYearMonth = { year, month };
			// loading = true;
			fetch(`/src/lib/data/${yearMonth}.json`)
				.then((res) => res.json())
				.then((json) => {
					data = json;
					console.log(json);
				})
				.catch(console.error)
				.finally(() => {
					console.log("final");
					// loading = false;
					// scrollTodayIntoView();
				});
		}
	});

	function padZero(n) {
		return +n < 10 ? "0" + n : n + "";
	}

	function setToday() {
		const { year, month } = getBS(today.year, today.month, today.date);
		if (year && month) {
			currentYearMonthState.set(`${year}-${padZero(month)}`);
		} else {
			location.hash = "";
		}
	}
	onMount(() => {
		// window.addEventListener('hashchange', hashchangeHandler)
		const selected = null;
		if (selected) {
			currentYearMonthState.set(selected);
		} else {
			//   location.hash = ''
			setToday();
		}
	});
</script>

<!-- <header class="row">
	<div class="col logo">
		<a href="/">
			<h1>{title}</h1>
		</a>
		<p>{subtitle}</p>
	</div>
</header> -->
<main>
	<div class="header-row" style="display: flow-root;">
		<div style="float: left; font-weight: bold;font-size: 2rem;">
			{title}
		</div>
		<div style="float: right; font-weight: bold;font-size: 2rem;">
			{subtitle}
		</div>
	</div>
	<div class="navigation" />
	<div class="grid">
		{#each nepaliShortDays as neDe}
			<div
				class="card-date"
				style="text-align:center;font-weight: bold;font-size: 2rem;"
			>
				{neDe}
			</div>
		{/each}
		{#each data as { day, date, events, panchanga, tithi, ad, gh, chandrama, saits, nsMonth, nsYear }}
		<!-- {constants.daysShort[day][locale]} -->
			<!-- {#if neDe === constants.daysShort[day][locale]} -->
			<Din
				day={constants.daysShort[day][locale]}
				events={(events || []).map((x) => x.name[locale]).join("; ")}
				{panchanga}
				{ad}
				eventParts={events.length
					? events[0].name[locale].split(" (")
					: [""]}
				date={locale === "ne" ? en2neNumbers(date) : date}
				tithi={constants.tithis[tithi < 29 ? tithi : 14][locale]}
				firstTithi={tithi === 0 || tithi === 23}
				chandrama={constants.chandramas[
					Math.floor(parseInt(chandrama))
				][locale]}
				chandramaPrefix={chandrama > parseInt(chandrama)
					? constants.extraMonth[locale]
					: ""}
				isHoliday={gh || day === 6}
				isToday={isToday(ad)}
				yearNe={en2neNumbers(+currentYearMonth.year)}
				monthNe={constants.monthsBS[+currentYearMonth.month - 1].ne}
				monthNs={constants.monthNS[nsMonth][locale]}
				yearNs={locale === "ne" ? en2neNumbers(nsYear) : nsYear}
				monthNsNe={constants.monthNS[nsMonth].ne}
				yearNsNe={en2neNumbers(nsYear)}
				dayNe={constants.days[day].ne}
				dateNe={en2neNumbers(date)}
				dateAd={parseInt(ad.split("-")[2])}
				saits={saits.map((x) => constants.saits[x][locale]).join("; ")}
				sunrise={locale === "ne"
					? panchanga.sunrise
					: ne2enNumbers("०६:१२")}
				sunset={locale === "ne"
					? panchanga.sunset
					: ne2enNumbers(panchanga.sunset)}
				birthnames={(panchanga.birthname || []).map(
					({ dt, nakshatra }) => ({
						nakshatra,
						dt: locale === "ne" ? en2neNumbers(dt) : dt,
					})
				)}
				inDays={getInDays(ad)}
			/>
			<!-- {/if} -->
		{/each}
	</div>
</main>

<style>
	header,
	main {
		position: relative;
		max-width: 1280px;
		margin-right: auto;
		margin-left: auto;
	}

	.logo h1 {
		display: inline;
	}
	.logo a {
		display: inline;
		color: var(--color);
		text-decoration: none;
	}

	.switch {
		position: relative;
		display: inline-block;
		width: 60px;
		height: 34px;
	}

	.switch:not(:first-child) {
		margin-top: 1em;
	}

	.switch input {
		opacity: 0;
		width: 0;
		height: 0;
	}

	.slider {
		position: absolute;
		cursor: pointer;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background-color: var(--color);
		-webkit-transition: 0.4s;
		transition: 0.4s;
		border-radius: 34px;
	}

	.lang .slider {
		background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='34' width='60'%3E%3Ctext x='10' y='23' fill='red'%3E🇳🇵%3C/text%3E%3Ctext x='34' y='23' fill='red'%3E🇬🇧%3C/text%3E%3C/svg%3E");
	}

	.theme .slider {
		background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='34' width='60'%3E%3Ctext x='10' y='23' fill='red'%3E🌙%3C/text%3E%3Ctext x='34' y='23' fill='red'%3E🌞%3C/text%3E%3C/svg%3E");
	}

	.slider:before {
		position: absolute;
		content: "";
		height: 26px;
		width: 26px;
		left: 4px;
		bottom: 4px;
		background-color: var(--bg-color);
		-webkit-transition: 0.4s;
		transition: 0.4s;
		border-radius: 50%;
	}

	.switch-input:checked + .slider {
		background-color: var(--color);
	}

	.switch-input:focus + .slider {
		box-shadow: 0 0 1px var(--bg-color);
	}

	.switch-input:checked + .slider:before {
		background-color: var(--bg-color);
		-webkit-transform: translateX(26px);
		-ms-transform: translateX(26px);
		transform: translateX(26px);
	}

	.dropdown-content {
		opacity: 0;
		visibility: hidden;
		display: flex;
		position: absolute;
		background-color: var(--secondary-bg-color);
		box-shadow: var(--box-shadow);
		flex-direction: column;
		padding: 16px;
		border-radius: 4px;
		right: 0;
		background-color: var(--secondary-bg-color);
		transition: opacity 225ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
		z-index: 100;
		box-shadow: 0 0 1px 0 rgba(0, 0, 0, 0.31),
			0 24px 36px -8px rgba(0, 0, 0, 0.25);
		border-radius: 4px;
	}
	.source-link {
		text-decoration: none;
		color: var(--color);
		padding: 0.5em;
		margin: 0.5em -0.5em -0.5em -0.5em;
	}
	.source-link pre {
		margin: 0;
	}
	.source-link:hover {
		background-color: var(--hover-bg-color);
	}
	.navigation {
		margin-bottom: 1em;
		display: flex;
		justify-content: flex-end;
	}
	.navigation > *:not(:first-child) {
		margin-left: 0.5em;
	}
</style>
