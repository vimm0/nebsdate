<script>
    // export let day;
    export let tithi;
    // export let events;
    // export let panchanga;
    export let dateAd;
    export let isCurrent;
    export let isToday;
    export let eventParts;
    export let date;
    export let isHoliday;
    export let firstTithi;
    export let chandrama;
    // export let chandramaPrefix;
    // export let yearNe;
    // export let monthNe;
    // export let dayNe;
    // export let dateNe;
    // export let inDays;
    // export let saits;
    // export let sunrise;
    // export let sunset;
    // export let ad;
    // export let monthNs;
    // export let yearNs;
    // export let monthNsNe;
    // export let yearNsNe;
    // export let birthnames;
</script>

<!-- <div class={`card date ${!isToday && isHoliday ? 'holiday' : isToday ? 'today' : ''}`} data-day={day}> -->
<div
    class={`card date ${
        !isToday && isHoliday ? "holiday" : isToday ? "today" : ""
    } ${isCurrent ? "current" : "nocurrent"}`}
>
    <!-- <div class={`card date}`}> -->
    {#if eventParts}
        <p class="event">
            {eventParts[0]}
            <small>
                {eventParts.length > 1 ? ` (${eventParts[1]}` : ""}
            </small>
        </p>
    {/if}

    <h2>{date}</h2>
    <div class="tithi-date">
        <div class="tithi">
            <small>
                {firstTithi ? chandrama : ""}
            </small>
            <span>
                {tithi}
            </span>
        </div>
        <span class="date-es">
            {dateAd}
        </span>
    </div>
</div>

<style>
    .card {
        background-color: var(--secondary-bg-color);
        transition: background-color 500ms ease;
        padding: 1rem;
        display: grid;
        place-items: center;
        position: relative;
        box-shadow: var(--card-box-shadow);
        border-radius: 4px;
        content-visibility: auto;
    }
    .date::after {
        content: attr(data-day);
        position: absolute;
        top: 0;
        left: 0;
        z-index: 0;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 4.5em;
        -webkit-font-smoothing: antialiased;
        color: var(--color);
        opacity: var(--day-opacity);
        text-transform: uppercase;
    }
    .date * {
        z-index: 1;
    }
    .date:hover,
    .date:active {
        background-color: var(--hover-bg-color) !important;
        cursor: pointer;
    }
    .event {
        width: 100%;
        align-items: start;
        text-align: center;
        line-height: 1.4;
        font-size: 14px;
    }
    .date h2 {
        font-size: 3.5em;
        color: var(--header-color);
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }
    .date .tithi-date {
        display: flex;
        width: 100%;
        align-items: flex-end;
        justify-content: space-between;
        line-height: 1.2;
    }
    .date .tithi {
        display: flex;
        flex-direction: column;
        width: 100%;
        align-items: start;
    }
    .date-es {
        font-size: 1.5em;
    }
    .date .event,
    .date .tithi-date {
        color: var(--secondary-color);
        min-height: 68.5px;
    }
    .date.holiday {
        transition: background-color 500ms ease;
        background-color: var(--holiday-bg-color);
    }
    .date.nocurrent {
        transition: background-color 500ms ease;
        background-color: var(--nocurrent-bg-color) !important;
    }
    .date.nocurrent::after,
    .date.nocurrent .event,
    .date.nocurrent h2,
    .date.nocurrent .tithi-date {
        color: var(--nocurrent-color) !important;
    }

    .date.holiday.nocurrent::after,
    .date.holiday.nocurrent .event,
    .date.holiday.nocurrent h2,
    .date.holiday.nocurrent .tithi-date {
        color: #f4433647 !important;
    }
    .date.holiday::after,
    .date.holiday .event,
    .date.holiday h2,
    .date.holiday .tithi-date {
        color: var(--holiday-color);
    }
    .holiday::after,
    .today::after {
        opacity: 0.12;
    }
    .date.today {
        transition: background-color 500ms ease;
        background-color: var(--today-bg-color);
    }
    .date.today::after,
    .date.today .event,
    .date.today h2,
    .date.today .tithi-date {
        color: var(--today-color);
    }

    .col-11 {
        flex: 0 0 91.666667%;
        max-width: 91.666667%;
    }
    .mt-2 {
        margin-top: 0.5rem !important;
    }
    .key {
        display: inline-block;
        font-weight: bold;
    }
    /* .panchang .key {
        width: 84px;
    } */
    .inline {
        display: inline;
    }
    /* .sun svg {
        stroke: transparent;
    } */

    .mb-8 {
        margin-bottom: 2rem !important;
    }
    .panel {
        padding: 0 18px;
        display: none;
        overflow: hidden;
        background-color: var(--bg-color);
    }
    /* .row.border [class*="col"] {
        border: 1px solid #666;
    } */
    .col-2 {
        flex: 0 0 16.666667%;
        max-width: 16.666667%;
    }
    .col-4 {
        flex: 0 0 33.333333%;
        max-width: 33.333333%;
    }
    .col-6 {
        flex: 0 0 50%;
        max-width: 50%;
    }
    .col-8 {
        flex: 0 0 66.666667%;
        max-width: 66.666667%;
    }
    .mx-2 {
        margin-right: 0.5rem !important;
    }

    .p-1 {
        padding: 0.25rem !important;
    }

    .py-1 {
        padding-top: 0.25rem !important;
    }
</style>
