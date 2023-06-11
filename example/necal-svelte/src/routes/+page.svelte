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
					console.log(lastCell);
				})
				.catch(console.error)
				.finally(() => {});
		}
	}

	function padZero(n) {
		return +n < 10 ? "0" + n : n + "";
	}

	function getDinData(rowIndex, colIndex) {
		return data[rowIndex * 7 + colIndex - 1];
	}
	function getPrevMonthDinData(rowIndex, colIndex) {
		return prevdata[prevdata.length - colIndex - firstDayOfMonth];
	}

	function getupcomingMonthDinData(index) {
		return prevdata[index];
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
						<!-- <Din
								day={constants.daysShort[getDinData(rowIndex, colIndex).day][locale]}
								events={(getDinData(rowIndex, colIndex).events || [])
									.map((x) => x.name[locale])
									.join("; ")}
								panchanga={getDinData(rowIndex, colIndex).panchanga}
								ad={getDinData(rowIndex, colIndex).ad}
								eventParts={getDinData(rowIndex, colIndex).events.length
									? getDinData(rowIndex, colIndex).events[0].name[locale].split(" (")
									: [""]}
								date={locale === "ne"
									? en2neNumbers(getDinData(rowIndex, colIndex).date)
									: getDinData(rowIndex, colIndex).date}
								tithi={constants.tithis[
									getDinData(rowIndex, colIndex).tithi < 29 ? getDinData(rowIndex, colIndex).tithi : 14
								][locale]}
								firstTithi={getDinData(rowIndex, colIndex).tithi === 0 || getDinData(rowIndex, colIndex).tithi === 23}
								chandrama={constants.chandramas[
									Math.floor(parseInt(getDinData(rowIndex, colIndex).chandrama))
								][locale]}
								chandramaPrefix={getDinData(rowIndex, colIndex).chandrama > parseInt(getDinData(rowIndex, colIndex).chandrama)
									? constants.extraMonth[locale]
									: ""}
								isHoliday={getDinData(rowIndex, colIndex).gh || getDinData(rowIndex, colIndex).day === 6}
								isToday={isToday(getDinData(rowIndex, colIndex).ad)}
								yearNe={en2neNumbers(+currentYearMonth.year)}
								monthNe={constants.monthsBS[
									+currentYearMonth.month - 1
								].ne}
								monthNs={constants.monthNS[getDinData(rowIndex, colIndex).nsMonth][locale]}
								yearNs={locale === "ne"
									? en2neNumbers(getDinData(rowIndex, colIndex).nsYear)
									: getDinData(rowIndex, colIndex).nsYear}
								monthNsNe={constants.monthNS[getDinData(rowIndex, colIndex).nsMonth].ne}
								yearNsNe={en2neNumbers(getDinData(rowIndex, colIndex).nsYear)}
								dayNe={constants.days[getDinData(rowIndex, colIndex).day].ne}
								dateNe={en2neNumbers(getDinData(rowIndex, colIndex).date)}
								dateAd={parseInt(getDinData(rowIndex, colIndex).ad.split("-")[2])}
								saits={getDinData(rowIndex, colIndex).saits
									.map((x) => constants.saits[x][locale])
									.join("; ")}
								sunrise={locale === "ne"
									? getDinData(rowIndex, colIndex).panchanga.sunrise
									: ne2enNumbers("०६:१२")}
								sunset={locale === "ne"
									? getDinData(rowIndex, colIndex).panchanga.sunset
									: ne2enNumbers(getDinData(rowIndex, colIndex).panchanga.sunset)}
								birthnames={(getDinData(rowIndex, colIndex).panchanga.birthname || []).map(
									({ dt, nakshatra }) => ({
										nakshatra,
										dt:
											locale === "ne"
												? en2neNumbers(dt)
												: dt,
									})
								)}
								inDays={getInDays(getDinData(rowIndex, colIndex).ad)}
							/> -->
						<Din
							isCurrent={true}
							date={locale === "ne"
								? en2neNumbers(
										getDinData(rowIndex, colIndex).date
								  )
								: getDinData(rowIndex, colIndex).date}
							isHoliday={getDinData(rowIndex, colIndex).gh ||
								getDinData(rowIndex, colIndex).day === 6}
							isToday={isToday(getDinData(rowIndex, colIndex).ad)}
						/>
					{:else if rowIndex * 7 + colIndex <= 0}
						{#if prevdata.length > 0}
							<Din
								isCurrent={false}
								date={locale === "ne"
									? en2neNumbers(
											getPrevMonthDinData(
												rowIndex,
												colIndex
											).date
									  )
									: getPrevMonthDinData(rowIndex, colIndex)
											.date}
								isHoliday={getPrevMonthDinData(
									rowIndex,
									colIndex
								).gh ||
									getPrevMonthDinData(rowIndex, colIndex)
										.day === 6}
								isToday={isToday(
									getPrevMonthDinData(rowIndex, colIndex).ad
								)}
							/>
						{/if}
					{:else if lastCell > 0}
						<!-- {#each Array(lastCell) as _, lastIndex} -->
							<!-- {lastIndex} -->
							<!-- {getupcomingMonthDinData(lastIndex).date} -->
							{rowIndex} - {colIndex}
							<!-- <Din
								isCurrent={false}
								date={locale === "ne"
									? en2neNumbers(
											getupcomingMonthDinData(lastIndex)
												.date
									  )
									: getupcomingMonthDinData(lastIndex).date}
								isHoliday={getupcomingMonthDinData(lastIndex)
									.gh ||
									getupcomingMonthDinData(lastIndex).day ===
										6}
								isToday={isToday(
									getupcomingMonthDinData(lastIndex).ad
								)}
							/> -->
						<!-- {/each} -->
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
