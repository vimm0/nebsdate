import os
import unittest
import datetime

import bs
from bs.config import REFERENCE_DATE_AD, MIN_DATE, MAX_DATE

RANDOM_CONVERSION_MAPS = [
    {'bs': {'year': 2013, 'month': 2, 'day': 8}, 'ad': {'year': 1956, 'month': 5, 'day': 21}},
    {'bs': {'year': 2051, 'month': 10, 'day': 1}, 'ad': {'year': 1995, 'month': 1, 'day': 15}},
    {'bs': {'year': 2076, 'month': 6, 'day': 27}, 'ad': {'year': 2019, 'month': 10, 'day': 14}},
    {'bs': {'year': 2077, 'month': 4, 'day': 4}, 'ad': {'year': 2020, 'month': 7, 'day': 19}}
]


class ParaTestCasae(unittest.TestCase):
    def __init__(self):
        self.eq = self.assertTrue


class TestNepaliDateTime(unittest.TestCase):
    def test_max_date_gt_min_date(self):
        assert bs.MAX_YEAR > bs.MIN_YEAR

    def test_reference_dates(self):
        re_year, re_month, re_day = REFERENCE_DATE_AD.values()
        # print(re_year, re_month, re_day)

        georgian_date = datetime.date(
            re_year,
            re_month,
            re_day
        )
        bs_date = bs.date.from_datetime_date(from_date=georgian_date)
        assert bs_date.year == MIN_DATE['year']
        assert bs_date.month == MIN_DATE['month']
        assert bs_date.day == MIN_DATE['day']

    def test_random_conversions(self):
        for rd_maps in RANDOM_CONVERSION_MAPS:
            dt = bs.date.from_datetime_date(datetime.date(**rd_maps['ad']))
            assert dt == bs.date(**rd_maps['bs'])

    def test_conversion_to_nepali(self):
        # Test conversion from Gregorian to Nepali
        gregorian_date = (2023, 6, 19)
        expected_nepali_date = (2080, 3, 4)
        ne_date = bs.date.from_datetime_date(from_date=datetime.date(*gregorian_date))
        nepali_date = (ne_date.year, ne_date.month, ne_date.day)
        self.assertEqual(nepali_date, expected_nepali_date)

    def test_conversion_to_gregorian(self):
        # Test conversion from Nepali to Gregorian
        nepali_date = (2080, 3, 4)
        expected_gregorian_date = (2023, 6, 19)
        gre_date = bs.date(*nepali_date).to_datetime_date()
        gregorian_date = (gre_date.year, gre_date.month, gre_date.day)
        self.assertEqual(gregorian_date, expected_gregorian_date)

    def test_month_name(self):
        # Test getting the name of a Nepali month
        nepali_date = (2080, 3, 5)
        expected_month_name = 'Asar'
        ne_date = bs.date(*nepali_date)
        month_name = ne_date.strftime('%B')
        self.assertEqual(month_name, expected_month_name)

    def test_vikram_year(self):
        gregorian_date_1 = (2023, 6, 19)
        gregorian_date_2 = (2023, 4, 19)
        gregorian_date_3 = (2023, 4, 12)
        gregorian_date_4 = (2023, 1, 12)
        en_date_1 = datetime.date(*gregorian_date_1)
        en_date_2 = datetime.date(*gregorian_date_2)
        en_date_3 = datetime.date(*gregorian_date_3)
        en_date_4 = datetime.date(*gregorian_date_4)
        # expected_vikram_year = 2080
        self.assertEqual(bs.to_vikram_year(en_date_1), 2080)
        self.assertEqual(bs.to_vikram_year(en_date_2), 2080)
        self.assertEqual(bs.to_vikram_year(en_date_3), 2079)
        self.assertEqual(bs.to_vikram_year(en_date_4), 2079)

    def test_is_leap_year(self):
        # Test checking if a Nepali year is a leap year
        gregorian_date_1 = (2023, 6, 19)
        gregorian_date_2 = (2024, 6, 19)

        bs_date_1 = bs.date.from_datetime_date(from_date=datetime.date(*gregorian_date_1))
        bs_date_2 = bs.date.from_datetime_date(from_date=datetime.date(*gregorian_date_2))
        self.assertFalse(bs.is_vikram_leap_year(bs_date_1))
        self.assertTrue(bs.is_vikram_leap_year(bs_date_2))


class TestDateMethod(unittest.TestCase):
    def test_date_init(self):
        dt = bs.date(2075, 5, 20)
        assert dt.year == 2075
        assert dt.month == 5
        assert dt.day == 20

    def test_date_today(self):
        ndt = bs.date.today()
        assert bs.MIN_YEAR <= ndt.year <= bs.MAX_YEAR
        assert 1 <= ndt.day <= 32
        assert 1 <= ndt.month <= 12

        dt = bs.date.from_datetime_date(
            (datetime.datetime.utcnow() + datetime.timedelta(seconds=bs.NEPAL_TIME_UTC_OFFSET)).date()
        )
        assert ndt == dt

    def test_datetime_init(self):
        dt = bs.datetime(2033, 2, 10, 10, 5, 30, 123456)
        assert dt.year == 2033
        assert dt.month == 2
        assert dt.day == 10
        assert dt.hour == 10
        assert dt.minute == 5
        assert dt.second == 30
        assert dt.microsecond == 123456

    def test_datetime_now(self):
        dt = bs.datetime.now()
        assert bs.MIN_YEAR <= dt.year <= bs.MAX_YEAR
        assert 1 <= dt.day <= 32
        assert 1 <= dt.month <= 12
        assert 0 <= dt.hour <= 23
        assert 0 <= dt.minute <= 59
        assert 0 <= dt.second <= 59
        assert 0 <= dt.microsecond <= 999999
        assert isinstance(dt.tzinfo, bs.UTC0545)

    def test_datetime_utcnow(self):
        dt = bs.datetime.now()
        utc_dt = dt.utcnow()
        utc_545 = utc_dt + datetime.timedelta(hours=5, minutes=45)
        assert dt.year == utc_545.year
        assert dt.month == utc_545.month
        assert dt.day == utc_545.day
        assert dt.hour == utc_545.hour
        assert dt.minute == utc_545.minute

    def test_datetime_timestamp(self):
        dt = bs.datetime(2078, 2, 23)
        ad_dt = datetime.datetime(2021, 6, 6, tzinfo=bs.UTC0545())
        assert dt.timestamp() == ad_dt.timestamp()


class TestDateFormat(unittest.TestCase):

    def test_strftime_date(self):
        dt = bs.date(2077, 6, 4)
        assert dt.strftime("%m/%d/%Y") == "06/04/2077"
        assert dt.strftime("%A of %B %d %y") == "Sunday of Aswin 04 77"
        assert dt.strftime("%a %b") == "Sun Asw"

        dt = bs.date(2077, 2, 32)
        assert dt.strftime("%d-%m-%Y") == "32-02-2077"

    def test_strftime_datetime(self):
        dt = bs.datetime(2052, 10, 29, 15, 22, 50, 2222)
        assert dt.strftime("%m/%d/%Y %I:%M:%S.%f %p %a %A") == "10/29/2052 03:22:50.002222 PM Mon Monday"

    def test_strptime_date(self):
        assert bs.datetime.strptime("2011-10-11", "%Y-%m-%d").date() == bs.date(2011, 10, 11)
        assert bs.datetime.strptime("2077-02-32", "%Y-%m-%d").date() == bs.date(2077, 2, 32)

    def test_strptime_datetime(self):
        assert bs.datetime.strptime("Asar 23 2025 10:00:00",
                                    "%B %d %Y %H:%M:%S") == bs.datetime(2025, 3, 23, 10, 0, 0)

    def test_strptime_year_special_case(self):
        assert bs.datetime.strptime("89", "%y") == bs.datetime(2089, 1, 1)
        assert bs.datetime.strptime("90", "%y") == bs.datetime(1990, 1, 1)
        assert bs.datetime.strptime("00", "%y") == bs.datetime(2000, 1, 1)


class TestDateConfig(unittest.TestCase):

    def test_utc_offset(self):
        # NPT = UTC + 05: 45
        eq = self.assertTrue
        eq(bs.NEPAL_TIME_UTC_OFFSET, (5 * 60 + 45) * 60)

    def test_calendar_path_exists(self):
        BASE_DIR = os.path.join(os.path.dirname(__file__))
        CALENDAR_PATH = os.path.join(BASE_DIR, '../data', 'bs.csv')
        self.assertTrue(os.path.exists(CALENDAR_PATH))

    def test_reference_date_ad_valid(self):
        REFERENCE_DATE_AD = {'year': 1918, 'month': 4, 'day': 13}
        self.assertFalse(REFERENCE_DATE_AD['year'] >= MIN_DATE['year'])
        self.assertTrue(REFERENCE_DATE_AD['year'] <= MAX_DATE['year'])
        self.assertTrue(REFERENCE_DATE_AD['month'] >= MIN_DATE['month'])
        self.assertTrue(REFERENCE_DATE_AD['month'] <= MAX_DATE['month'])
        self.assertTrue(REFERENCE_DATE_AD['day'] >= MIN_DATE['day'])
        self.assertTrue(REFERENCE_DATE_AD['day'] <= MAX_DATE['day'])

    def test_min_date_valid(self):
        MIN_DATE = {'year': 1975, 'month': 1, 'day': 1}
        self.assertTrue(MIN_DATE['year'] >= REFERENCE_DATE_AD['year'])
        self.assertTrue(MIN_DATE['year'] <= MAX_DATE['year'])
        self.assertTrue(MIN_DATE['month'] <= REFERENCE_DATE_AD['month'])
        self.assertTrue(MIN_DATE['month'] <= MAX_DATE['month'])
        self.assertTrue(MIN_DATE['day'] <= REFERENCE_DATE_AD['day'])
        self.assertTrue(MIN_DATE['day'] <= MAX_DATE['day'])

    def test_max_date_valid(self):
        MAX_DATE = {'year': 2100, 'month': 12, 'day': 30}
        self.assertTrue(MAX_DATE['year'] >= REFERENCE_DATE_AD['year'])
        self.assertTrue(MAX_DATE['year'] >= MIN_DATE['year'])
        self.assertTrue(MAX_DATE['month'] >= REFERENCE_DATE_AD['month'])
        self.assertTrue(MAX_DATE['month'] >= MIN_DATE['month'])
        self.assertTrue(MAX_DATE['day'] >= REFERENCE_DATE_AD['day'])
        self.assertTrue(MAX_DATE['day'] >= MIN_DATE['day'])


class BSTestCase(unittest.TestCase):

    def test_days_in_month(self):
        self.assertEqual(bs._days_in_month(2079, 1), 31)
        self.assertEqual(bs._days_in_month(2079, 2), 31)
        self.assertEqual(bs._days_in_month(2079, 4), 31)  # Invalid month

    def test_days_before_year(self):
        self.assertEqual(bs._days_before_year(2079), 37987)
        self.assertEqual(bs._days_before_year(2080), 38352)

    def test_days_before_month(self):
        self.assertEqual(bs._days_before_month(2079, 3), 62)
        self.assertEqual(bs._days_before_month(2079, 4), 94)  # Invalid month

    def test_ymd2ord(self):
        self.assertEqual(bs._ymd2ord(2079, 1, 1), 37988)
        self.assertEqual(bs._ymd2ord(2079, 6, 15), 38158)

    def test_ord2ymd(self):
        self.assertEqual(bs._ord2ymd(37988), (2079, 1, 1))
        self.assertEqual(bs._ord2ymd(38158), (2079, 6, 15))

    # def test_to_bs(self):
    #     dt = datetime(2023, 6, 21)
    #     bs_date = to_bs(dt)
    #     self.assertEqual(bs_date, (2079, 3, 7))
    #
    # def test_to_ad(self):
    #     bs_date = (2079, 3, 7)
    #     dt = to_ad(bs_date)
    #     self.assertEqual(dt, datetime(2023, 6, 21))


if __name__ == '__main__':
    unittest.main()
