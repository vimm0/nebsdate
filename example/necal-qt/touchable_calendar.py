
import sys
from PyQt5.QtCore import Qt, QDate, QLocale
from PyQt5.QtWidgets import QApplication, QCalendarWidget, QLabel, QVBoxLayout, QWidget
from PyQt5.uic.properties import QtCore


# Conversion functions between Gregorian and Bikram Sambat calendars
def to_bikram_sambat(gregorian_date):
    # Convert Gregorian year to Bikram Sambat year
    bs_year = gregorian_date.year() + 57

    # Calculate the remaining Bikram Sambat components
    bs_month = (gregorian_date.month() + 8) % 12
    if bs_month == 0:
        bs_month = 12

    bs_day = gregorian_date.day()

    return QDate(bs_year, bs_month, bs_day)

def from_bikram_sambat(bs_date):
    # Convert Bikram Sambat year to Gregorian year
    gregorian_year = bs_date.year() - 57

    # Calculate the remaining Gregorian components
    gregorian_month = (bs_date.month() + 4) % 12
    if gregorian_month == 0:
        gregorian_month = 12

    gregorian_day = bs_date.day()

    return QDate(gregorian_year, gregorian_month, gregorian_day)


class CalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.calendar = QCalendarWidget(self)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.updateDateLabel)
        # QLocale.setDefault(QLocale.India)
        # QLocale.setDefault(QLocale(QLocale.Hebrew, QLocale.Israel))
        self.calendar.setLocale(QLocale.Persian)

        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)

        self.dateLabel = QLabel(self)
        self.dateLabel.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.calendar)
        layout.addWidget(self.dateLabel)

        self.setLayout(layout)

        self.setWindowTitle("Nepali Bikram Sambat Calendar")

    def updateDateLabel(self):
        selected_date = self.calendar.selectedDate()
        bs_date = to_bikram_sambat(selected_date)
        bs_date_str = bs_date.toString("yyyy-MM-dd")
        bs_date_str = bs_date_str.replace("-", " ")
        bs_date_str = self.convertToNepali(bs_date_str)
        self.dateLabel.setText(f"Selected Date: {bs_date_str} (Bikram Sambat)")

    def convertToNepali(self, date_str):
        nepali_locale = QLocale(QLocale.Nepali, QLocale.Nepal)
        # QCalendarWidget.LongDayNames
        # self.calendar.horizontalHeaderFormat()
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)

        converted_date = nepali_locale.toDate(date_str, "yyyy MM dd")
        day_name = nepali_locale.dayName(converted_date.dayOfWeek(), QLocale.LongFormat)
        month_name = nepali_locale.monthName(converted_date.month(), QLocale.LongFormat)
        nepali_date_str = f"{day_name} {converted_date.day()} {month_name} {converted_date.year()}"
        return nepali_date_str


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarWidget()
    window.show()
    sys.exit(app.exec_())
