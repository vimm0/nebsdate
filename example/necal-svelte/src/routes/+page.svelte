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
	$: prevdata = "";
	$: upcomingdata = "";
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
	let numRows;
	let firstDayOfMonth = 0;
	let daysInMonth = 0;
	let lastCell = 0;

	function getDay(data, colIndex) {
		return constants.daysShort[data(colIndex).day][locale];
	}
	function getEvents(data, colIndex) {
		if (data[colIndex]) {
			let events = data[colIndex].events;
			return (events || []).map((x) => x.name[locale]).join("; ");
		}
	}
	function getEventParts(data, colIndex) {
		if (data[colIndex]) {
			let events = data[colIndex].events;
			return events.length ? events[0].name[locale].split(" (") : [""];
		}
	}
	function getPanchanga(data, colIndex) {
		if (data[colIndex]) {
			return data[colIndex].panchanga;
		}
	}
	function getAd(data, colIndex) {
		if (data[colIndex]) {
			return data[colIndex].ad;
		}
	}
	function getTithi(data, colIndex) {
		if (data[colIndex]) {
			let tithi = data[colIndex].tithi;
			return constants.tithis[tithi < 29 ? tithi : 14][locale];
		}
	}
	function getFirstTithi(data, colIndex) {
		if (data[colIndex]) {
			let tithi = data[colIndex].tithi;
			return tithi === 0 || tithi === 23;
		}
	}

	function getChandrama(data, colIndex) {
		if (data[colIndex]) {
			let chandrama = data[colIndex].chandrama;
			return constants.chandramas[Math.floor(parseInt(chandrama))][
				locale
			];
		}
	}
	function getChandramaPrefix(data, colIndex) {
		if (data[colIndex]) {
			let chandrama = data[colIndex].chandrama;
			return chandrama > parseInt(chandrama)
				? constants.extraMonth[locale]
				: "";
		}
	}

	function getYearNe() {
		return en2neNumbers(+currentYearMonth.year);
	}
	function getMonthNe() {
		return constants.monthsBS[+currentYearMonth.month - 1].ne;
	}

	function getMonthNs(data, colIndex) {
		if (data[colIndex]) {
			let nsMonth = data[colIndex].nsMonth;
			return constants.monthNS[nsMonth][locale];
		}
	}

	function getYearNs(data, colIndex) {
		if (data[colIndex]) {
			let nsYear = data[colIndex].nsYear;

			return locale === "ne" ? en2neNumbers(nsYear) : nsYear;
		}
	}

	function getMonthNsNe(data, colIndex) {
		if (data[colIndex]) {
			let nsMonth = data[colIndex].nsMonth;
			return constants.monthNS[nsMonth].ne;
		}
	}

	function getYearNsNe(data, colIndex) {
		if (data[colIndex]) {
			let nsYear = data[colIndex].nsYear;
			return en2neNumbers(nsYear);
		}
	}
	function getDayNe(data, colIndex) {
		if (data[colIndex]) {
			let day = data[colIndex].day;
			return constants.days[day].ne;
		}
	}

	function getDateNe(data, colIndex) {
		if (data[colIndex]) {
			let date = data[colIndex].date;
			return en2neNumbers(date);
		}
	}

	function getDateAd(data, colIndex) {
		if (data[colIndex]) {
			let ad = data[colIndex].ad;
			return parseInt(ad.split("-")[2]);
		}
	}

	function getSaits(data, colIndex) {
		if (data[colIndex]) {
			let saits = data[colIndex].saits;
			return saits.map((x) => constants.saits[x][locale]).join("; ");
		}
	}

	function getSunrise(data, colIndex) {
		if (data[colIndex]) {
			let panchanga = data[colIndex].panchanga;
			return locale === "ne" ? panchanga.sunrise : ne2enNumbers("०६:१२");
		}
	}
	function getSunset(data, colIndex) {
		if (data[colIndex]) {
			let panchanga = data[colIndex].panchanga;
			return locale === "ne"
				? panchanga.sunset
				: ne2enNumbers(panchanga.sunset);
		}
	}

	function getBirthnames(data, colIndex) {
		if (data[colIndex]) {
			let panchanga = data[colIndex].panchanga;
			return (panchanga.birthname || []).map(({ dt, nakshatra }) => ({
				nakshatra,
				dt: locale === "ne" ? en2neNumbers(dt) : dt,
			}));
		}
	}

	function getInDayss(data, colIndex) {
		if (data[colIndex]) {
			let ad = data[colIndex].ad;
			return getInDays(ad);
		}
	}

	function IsToday(data, colIndex) {
		if (data[colIndex]) {
			return isToday(data(colIndex).ad);
		}
	}
	function IsHoliday(data, colIndex) {
		if (data[colIndex]) {
			return data(colIndex).gh || data(colIndex).day === 6;
		}
	}
	function getDate(data, colIndex) {
		if (data[colIndex]) {
			return locale === "ne"
				? en2neNumbers(data(colIndex).date)
				: data(colIndex).date;
		}
	}

	// console.log(todayBs);
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
	$: getInDays = (ad) => {};
	currentYearMonthState.subscribe((yearMonth) => {
		if (yearMonth) {
			const [year, month] = yearMonth.split("-");
			currentYearMonth = { year, month };
			// loading = true;
			fetch(`/src/lib/data/${yearMonth}.json`)
				.then((res) => res.json())
				.then((json) => {
					data = json;
					console.log("current month ", json);
					firstDayOfMonth = data[0].day;
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

	function previousYearMonthState(yearMonth) {
		if (yearMonth) {
			const [year, month] = yearMonth.split("-");
			currentYearMonth = { year, month };
			fetch(`/src/lib/data/${yearMonth}.json`)
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
			fetch(`/src/lib/data/${yearMonth}.json`)
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

	function getDinData(colIndex) {
		return data[colIndex];
	}
	function getPrevMonthDinData(colIndex) {
		return prevdata[prevdata.length - colIndex - firstDayOfMonth];
	}

	function getupcomingMonthDinData(weekday) {
		// console.log(upcomingdata.filter(obj => obj.day === weekday));
		return upcomingdata.filter((obj) => obj.day === weekday)[0];
	}

	function setToday() {
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
	onMount(() => {
		const selected = null;
		if (selected) {
			currentYearMonthState.set(selected);
		} else {
			setToday();
		}
	});

	function dinProps(data, colIndex) {
		if (data) {
			const {
				day,
				date,
				events,
				panchanga,
				tithi,
				ad,
				gh,
				chandrama,
				saits,
				nsMonth,
				nsYear,
			} = data[colIndex];

			return {
				day: constants.daysShort[day][locale],
				events: (events || []).map((x) => x.name[locale]).join("; "),
				panchanga,
				ad,
				eventParts: events.length
					? events[0].name[locale].split(" (")
					: [""],
				date: locale === "ne" ? en2neNumbers(date) : date,
				tithi: constants.tithis[tithi < 29 ? tithi : 14][locale],
				firstTithi: tithi === 0 || tithi === 23,
				chandrama:
					constants.chandramas[Math.floor(parseInt(chandrama))][
						locale
					],
				chandramaPrefix:
					chandrama > parseInt(chandrama)
						? constants.extraMonth[locale]
						: "",
				isHoliday: gh || day === 6,
				isToday: isToday(ad),
				yearNe: en2neNumbers(+currentYearMonth.year),
				monthNe: constants.monthsBS[+currentYearMonth.month - 1].ne,
				monthNs: constants.monthNS[nsMonth][locale],
				yearNs: locale === "ne" ? en2neNumbers(nsYear) : nsYear,
				monthNsNe: constants.monthNS[nsMonth].ne,
				yearNsNe: en2neNumbers(nsYear),
				dayNe: constants.days[day].ne,
				dateNe: en2neNumbers(date),
				dateAd: parseInt(ad.split("-")[2]),
				saits: saits.map((x) => constants.saits[x][locale]).join("; "),
				sunrise:
					locale === "ne" ? panchanga.sunrise : ne2enNumbers("०६:१२"),
				sunset:
					locale === "ne"
						? panchanga.sunset
						: ne2enNumbers(panchanga.sunset),
				birthnames: (panchanga.birthname || []).map(
					({ dt, nakshatra }) => ({
						nakshatra,
						dt: locale === "ne" ? en2neNumbers(dt) : dt,
					})
				),
				inDays: getInDays(ad),
				data, // Include the original data object if needed
			};
		}
	}
</script>

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
		{#each Array(numRows) as _, rowIndex}
			{#each Array(7) as _, colIndex}
				<div class="card-date">
					{#if rowIndex * 7 + colIndex > 0 && rowIndex * 7 + colIndex <= daysInMonth}
						<Din
							isCurrent={true}
							{...dinProps(data, rowIndex * 7 + colIndex - 1)}
						/>
					{:else if rowIndex * 7 + colIndex <= 0}
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
						/>
					{/if}
				</div>
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
