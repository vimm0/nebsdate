import sys

from PyQt5.QtCore import QLocale
from PyQt5.QtWidgets import QApplication, QCalendarWidget

app = QApplication(sys.argv)

calendar = QCalendarWidget()
calendar.setLocale(QLocale("ne_NP"))
calendar.show()

sys.exit(app.exec_())


# Add Nepali months and days
# for month in range(1, 13):
#     print(calendar.locale().monthNames()[month])
#     calendar.setDateText(month, 0, calendar.locale().monthNames()[month])
#     for day in range(1, 32):
#         calendar.setDateText(month, day, calendar.locale().dayNames()[day])

# import sys
# from PyQt5.QtCore import QDate, Qt, QRect
# from PyQt5.QtGui import QFont, QFontMetrics, QPainter
# from PyQt5.QtWidgets import QApplication, QCalendarWidget, QLabel
#
#
# class NepaliCalendarWidget(QCalendarWidget):
#     def __init__(self, parent=None):
#         super(NepaliCalendarWidget, self).__init__(parent)
#
#         self.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
#         self.setGridVisible(True)
#         self.setMinimumDate(QDate(1944, 4, 13))  # Minimum Nepali date
#         self.setMaximumDate(QDate(2090, 12, 31))  # Maximum Nepali date
#
#         self.setWindowTitle('Nepali Calendar')
#
#         # Set the calendar to display Nepali dates
#         self.set_nepali_calendar()
#
#     def set_nepali_calendar(self):
#         font = self.font()
#         font_metrics = QFontMetrics(font)
#         cell_width = self.width() / 7
#
#         # Set Nepali month and day names
#         nepali_months = [
#             'बैशाख', 'जेठ', 'असार', 'श्रावण', 'भाद्र', 'असोज', 'कार्तिक', 'मंसिर', 'पुष', 'माघ', 'फागुन', 'चैत'
#         ]
#         nepali_days = [
#             'आईतवार', 'सोमवार', 'मङ्गलवार', 'बुधवार', 'बिहिवार', 'शुक्रवार', 'शनिवार'
#         ]
#
#         # Set Nepali month names
#         for column in range(7):
#             month_label = QLabel(self)
#             month_label.setAlignment(Qt.AlignCenter)
#             month_label.setFont(font)
#             month_label.setText(nepali_months[column])
#             month_label.setFixedWidth(int(cell_width))
#             self.set_label_in_cell(QDate(1900, column + 1, 1), month_label)
#
#         # Set Nepali day names
#         for row in range(6):
#             for column in range(7):
#                 if row == 0:
#                     day_label = QLabel(self)
#                     day_label.setAlignment(Qt.AlignCenter)
#                     day_label.setFont(font)
#                     day_label.setText(nepali_days[column])
#                     day_label.setFixedWidth(int(cell_width))
#                     self.set_label_in_cell(QDate(1900, column + 1, row + 1), day_label)
#
#     def set_label_in_cell(self, date, label):
#         index = self.indexAt(date)
#         if index.isValid():
#             rect = self.visualRect(index)
#             label.setGeometry(rect)
#             label.show()
#
#     def paintCell(self, painter, rect, date):
#         # Customize the painting of calendar cells here
#         # You can modify this method to display Nepali dates
#
#         super(NepaliCalendarWidget, self).paintCell(painter, rect, date)
#
#         # Example: Display Nepali day in the bottom-right corner of the cell
#         nepali_date = self.get_nepali_date(date)
#         day_str = str(nepali_date.day())
#
#         painter.save()
#
#         # Set the font
#         font = painter.font()
#         font.setPixelSize(12)
#         painter.setFont(font)
#
#         # Calculate the text size
#         text_rect = painter.boundingRect(rect, Qt.AlignBottom | Qt.AlignRight, day_str)
#
#         # Adjust the rect for the text size
#         rect.adjust(0, 0, -text_rect.width(), -text_rect.height())
#
#         # Draw the text
#         painter.drawText(rect, Qt.AlignBottom | Qt.AlignRight, day_str)
#
#         painter.restore()
#
#     def get_nepali_date(self, date):
#         # TODO: Implement the conversion from Gregorian to Nepali date
#         # You would need to calculate the Nepali year, month, and day based on the Bikram Sambat calendar rules.
#         # There are libraries and algorithms available that can help you with the conversion.
#
#         # Placeholder implementation that simply returns the same Gregorian date
#         return date
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     widget = NepaliCalendarWidget()
#     widget.show()
#     sys.exit(app.exec_())
