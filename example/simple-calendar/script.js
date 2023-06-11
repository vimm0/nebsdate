// Get current date
var currentDate = new Date();

// Get the calendar div
var calendar = document.getElementById('calendar');

// Create table element
var table = document.createElement('table');

// Create thead element and append it to the table
var thead = document.createElement('thead');
table.appendChild(thead);

// Create tr element and append it to the thead
var tr = document.createElement('tr');
thead.appendChild(tr);

// Create th elements for each day of the week and append them to the tr
var daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
for (var i = 0; i < daysOfWeek.length; i++) {
    var th = document.createElement('th');
    th.textContent = daysOfWeek[i];
    tr.appendChild(th);
}

// Create tbody element and append it to the table
var tbody = document.createElement('tbody');
table.appendChild(tbody);

// Get the number of days in the current month
var daysInMonth = new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 0).getDate();

// Get the day of the week for the first day of the month
var firstDayOfMonth = new Date(currentDate.getFullYear(), currentDate.getMonth(), 1).getDay();
console.log(firstDayOfMonth)
// Calculate the number of rows needed in the calendar
var numRows = Math.ceil((firstDayOfMonth + daysInMonth) / 7);

// Create calendar rows
for (var row = 0; row < numRows; row++) {
    // Create tr element for each row
    var tr = document.createElement('tr');
    tbody.appendChild(tr);

    // Create calendar cells for each day of the week
    for (var col = 0; col < 7; col++) {
        // Calculate the day number
        var day = row * 7 + col - firstDayOfMonth + 1;
        console.log(col, day)
        // Create td element for each day
        var td = document.createElement('td');
        tr.appendChild(td);

        // Set the day number as text content
        if (day > 0 && day <= daysInMonth) {
            td.textContent = day;
            //   console.log(day)

            // Highlight the current date
            if (currentDate.getDate() === day && currentDate.getMonth() === new Date().getMonth()) {
                td.classList.add('today');
            }
        }
    }
}

// Append the table to the calendar div
calendar.appendChild(table);
