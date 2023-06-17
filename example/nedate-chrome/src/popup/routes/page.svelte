<script>
	import constants from "../lib/utils/constants";
	// @ts-ignore
	import { yearsState, currentYearMonthState } from "../store";
	// @ts-ignore
	import { onDestroy, onMount } from "svelte";
	// @ts-ignore
	import en2neNumbers from "../lib/utils/en2neNumbers";
	// import ne2enNumbers from "../lib/utils/ne2enNumbers";
	// @ts-ignore
	import getBS from "../lib/utils/getBS";
	// @ts-ignore
	import Din from "../../components/Din.svelte";
	// import { _ } from "../i18n";
	import "./styles.css";
	const DEFAULT_LANG = "ne";
	// @ts-ignore
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
	// @ts-ignore
	const englishLongDays = [
		"Sunday",
		"Monday",
		"Tuesday",
		"Wednesday",
		"Thursday",
		"Friday",
		"Saturday",
	];
	// @ts-ignore
	const englishShortDays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

	$: data = "";
	$: prevdata = "";
	$: upcomingdata = "";
	$: title = "";
	$: subtitle = "";

	let numRows;
	let lastCell = 0;
	let daysInMonth = 0;
	let firstDayOfMonth = 0;
	let locale = DEFAULT_LANG;

	let today = new Date();
	let currentYearMonth = {};
	today = {
		// @ts-ignore
		year: today.getFullYear(),
		month: today.getMonth() + 1,
		date: today.getDate(),
	};
	// @ts-ignore
	const date = `${today.year}-${today.month}-${today.date}`;
	// @ts-ignore
	const todayBs = getBS(today.year, today.month, today.date);
	// @ts-ignore
	const dateBs = `${todayBs.year}-${todayBs.month}-${todayBs.date}`;


		$: if (data) {
		// @ts-ignore
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
						// @ts-ignore
						[today.year, today.month, today.date][i] === parseInt(x)
				).length === 3
		);
	};
// @ts-ignore
		$: getInDays = (ad) => {};
	currentYearMonthState.subscribe((yearMonth) => {
		if (yearMonth) {
			const [year, month] = yearMonth.split("-");
			currentYearMonth = { year, month };
			// loading = true;
			fetch(`/static/data/${yearMonth}.json`)
				.then((res) => res.json())
				.then((json) => {
					data = json;
					console.log("current month ", json);
					// @ts-ignore
					firstDayOfMonth = data[0].day;
					// @ts-ignore
					daysInMonth = data[data.length - 1].date;
					numRows = Math.ceil((firstDayOfMonth + daysInMonth) / 7);
				})
				.catch(console.error)
				.finally(() => {
					// console.log("final");
					// loading = false;
					// scrollTodayIntoView();
				});
		}
	});
	onMount(() => {
		const selected = null;
		if (selected) {
			currentYearMonthState.set(selected);
		} else {
			setToday();
		}
	});

	function previousYearMonthState(yearMonth) {
		if (yearMonth) {
			const [year, month] = yearMonth.split("-");
			currentYearMonth = { year, month };
			fetch(`/static/data/${yearMonth}.json`)
				.then((res) => res.json())
				.then((json) => {
					prevdata = json;
					console.log("prevmonth ", json);
				})
				.catch(console.error)
				.finally(() => {});
		}
	}

	function upcomingYearMonthState(yearMonth) {
		if (yearMonth) {
			const [year, month] = yearMonth.split("-");
			currentYearMonth = { year, month };
			fetch(`/static/data/${yearMonth}.json`)
				.then((res) => res.json())
				.then((json) => {
					upcomingdata = json;
					console.log("upcoming month ", json);
					lastCell = numRows * 7 - (firstDayOfMonth + daysInMonth);
					// console.log(lastCell);
				})
				.catch(console.error)
				.finally(() => {});
		}
	}

	function padZero(n) {
		return +n < 10 ? "0" + n : n + "";
	}

	function setToday() {
		// @ts-ignore
		const { year, month } = getBS(today.year, today.month, today.date);
		if (year && month) {
			let currentYearMonth = `${year}-${padZero(month)}`;
			let previousYearMonth = `${year}-${padZero(month - 1)}`;
			let upcomingYearMonth = `${year}-${padZero(month + 1)}`;
			currentYearMonthState.set(currentYearMonth);
			previousYearMonthState(previousYearMonth);
			upcomingYearMonthState(upcomingYearMonth);
		} else {
			location.hash = "";
		}
	}

	function dinProps(data, colIndex) {
		const {
			day,
			date,
			events,
			// @ts-ignore
			panchanga,
			tithi,
			ad,
			gh,
			chandrama,
			// @ts-ignore
			saits,
			// @ts-ignore
			nsMonth,
			// @ts-ignore
			nsYear,
		} = data[colIndex];

		return {
			// day: constants.daysShort[day][locale],
			// events: (events || []).map((x) => x.name[locale]).join("; "),
			// panchanga,
			// ad,
			eventParts: events.length
				? events[0].name[locale].split(" (")
				: [""],
			date: locale === "ne" ? en2neNumbers(date) : date,
			tithi: constants.tithis[tithi < 29 ? tithi : 14][locale],
			firstTithi: tithi === 0 || tithi === 23,
			chandrama:
				constants.chandramas[Math.floor(parseInt(chandrama))][locale],
			// chandramaPrefix:
			// 	chandrama > parseInt(chandrama)
			// 		? constants.extraMonth[locale]
			// 		: "",
			isHoliday: gh || day === 6,
			isToday: isToday(ad),
			// yearNe: en2neNumbers(+currentYearMonth.year),
			// monthNe: constants.monthsBS[+currentYearMonth.month - 1].ne,
			// monthNs: constants.monthNS[nsMonth][locale],
			// yearNs: locale === "ne" ? en2neNumbers(nsYear) : nsYear,
			// monthNsNe: constants.monthNS[nsMonth].ne,
			// yearNsNe: en2neNumbers(nsYear),
			// dayNe: constants.days[day].ne,
			// dateNe: en2neNumbers(date),
			dateAd: parseInt(ad.split("-")[2]),
			// saits: saits.map((x) => constants.saits[x][locale]).join("; "),
			// sunrise:
			// 	locale === "ne" ? panchanga.sunrise : ne2enNumbers("०६:१२"),
			// sunset:
			// 	locale === "ne"
			// 		? panchanga.sunset
			// 		: ne2enNumbers(panchanga.sunset),
			// birthnames: (panchanga.birthname || []).map(
			// 	({ dt, nakshatra }) => ({
			// 		nakshatra,
			// 		dt: locale === "ne" ? en2neNumbers(dt) : dt,
			// 	})
			// ),
			// inDays: getInDays(ad),
			// data, // Include the original data object if needed
		};
	}
</script>
<main>
	<div class="header-row" style="display: flow-root;">
		<div class="nepali-month-year">
			{title}
		</div>
		<div class="english-month-year">
			{subtitle}
		</div>
	</div>
	<div class="navigation" />
	<div class="grid">
		{#each nepaliShortDays as neDe}
			<div
				class="day-name"
			>
				{neDe}
			</div>
		{/each}
	</div>
	<div class="grid">
		{#each Array(numRows) as _, rowIndex}
			{#each Array(7) as _, colIndex}
					{#if rowIndex * 7 + colIndex > 0 && rowIndex * 7 + colIndex <= daysInMonth}
						<Din
							isCurrent={true}
							{...dinProps(data, rowIndex * 7 + colIndex - 1)}
						/>
					<!-- {:else if rowIndex * 7 + colIndex <= 0}
						{#if prevdata.length > 0}
							<Din
								isCurrent={false}
								{...dinProps(
									prevdata,
									prevdata.length - colIndex - firstDayOfMonth
								)}
							/>
						{/if}
					{:else if lastCell > 0}
						<Din
							isCurrent={false}
							{...dinProps(
								upcomingdata.filter(
									(obj) => obj.day === colIndex
								),
								0
							)}
						/> -->
					{/if}
			{/each}
		{/each}
	</div>
</main>

<style>
	main {
		position: relative;
		max-width: 1280px;
		margin-right: auto;
		margin-left: auto;
	}

	.navigation {
		margin-bottom: 1em;
		display: flex;
		justify-content: flex-end;
	}
</style>