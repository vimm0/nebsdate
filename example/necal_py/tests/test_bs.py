import unittest
import datetime

import bs
from bs.config import REFERENCE_DATE_AD, MIN_DATE

RANDOM_CONVERSION_MAPS = [
    {'bs': {'year': 2013, 'month': 2, 'day': 8}, 'ad': {'year': 1956, 'month': 5, 'day': 21}},
    {'bs': {'year': 2051, 'month': 10, 'day': 1}, 'ad': {'year': 1995, 'month': 1, 'day': 15}},
    {'bs': {'year': 2076, 'month': 6, 'day': 27}, 'ad': {'year': 2019, 'month': 10, 'day': 14}},
    {'bs': {'year': 2077, 'month': 4, 'day': 4}, 'ad': {'year': 2020, 'month': 7, 'day': 19}}
]


class TestSample(unittest.TestCase):
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


class TestParam(unittest.TestCase):

    def test_max_date_gt_min_date(self):
        assert bs.MAX_YEAR > bs.MIN_YEAR


class TestDateMethods(unittest.TestCase):
    def test_init(self):
        dt = bs.date(2075, 5, 20)
        assert dt.year == 2075
        assert dt.month == 5
        assert dt.day == 20

    def test_today(self):
        ndt = bs.date.today()
        assert bs.MIN_YEAR <= ndt.year <= bs.MAX_YEAR
        assert 1 <= ndt.day <= 32
        assert 1 <= ndt.month <= 12

        dt = bs.date.from_datetime_date(
            (datetime.datetime.utcnow() + datetime.timedelta(seconds=bs.NEPAL_TIME_UTC_OFFSET)).date()
        )
        assert ndt == dt


class TestDatetimeMethods(unittest.TestCase):

    def test_init(self):
        dt = bs.datetime(2033, 2, 10, 10, 5, 30, 123456)
        assert dt.year == 2033
        assert dt.month == 2
        assert dt.day == 10
        assert dt.hour == 10
        assert dt.minute == 5
        assert dt.second == 30
        assert dt.microsecond == 123456

    def test_now(self):
        dt = bs.datetime.now()
        assert bs.MIN_YEAR <= dt.year <= bs.MAX_YEAR
        assert 1 <= dt.day <= 32
        assert 1 <= dt.month <= 12
        assert 0 <= dt.hour <= 23
        assert 0 <= dt.minute <= 59
        assert 0 <= dt.second <= 59
        assert 0 <= dt.microsecond <= 999999
        assert isinstance(dt.tzinfo, bs.UTC0545)

    def test_utcnow(self):
        dt = bs.datetime.now()
        utc_dt = dt.utcnow()
        utc_545 = utc_dt + datetime.timedelta(hours=5, minutes=45)
        assert dt.year == utc_545.year
        assert dt.month == utc_545.month
        assert dt.day == utc_545.day
        assert dt.hour == utc_545.hour
        assert dt.minute == utc_545.minute

    def test_timestamp(self):
        dt = bs.datetime(2078, 2, 23)
        ad_dt = datetime.datetime(2021, 6, 6, tzinfo=bs.UTC0545())
        assert dt.timestamp() == ad_dt.timestamp()


class TestStrftime(unittest.TestCase):

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


class TestStrptime(unittest.TestCase):

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


# import random
# from nepali_datetime import NepaliDateTime
#
# class TestNepaliDateTime(unittest.TestCase):
#     def test_to_nepali_date(self):
#         for _ in range(10):
#             ad_year = random.randint(1900, 2100)
#             ad_month = random.randint(1, 12)
#             ad_day = random.randint(1, 28)  # Assuming the maximum day is 28 for simplicity
#
#             nep_date = NepaliDateTime.to_nepali_date(ad_year, ad_month, ad_day)
#
#             expected_nep_date = self._convert_to_nepali_date(ad_year, ad_month, ad_day)
#
#             self.assertEqual(nep_date.year, expected_nep_date[0])
#             self.assertEqual(nep_date.month, expected_nep_date[1])
#             self.assertEqual(nep_date.day, expected_nep_date[2])
#
#     def test_to_ad_date(self):
#         for _ in range(10):
#             nep_year = random.randint(1800, 2100)
#             nep_month = random.randint(1, 12)
#             nep_day = random.randint(1, 28)  # Assuming the maximum day is 28 for simplicity
#
#             ad_date = NepaliDateTime.to_ad_date(nep_year, nep_month, nep_day)
#
#             expected_ad_date = self._convert_to_ad_date(nep_year, nep_month, nep_day)
#
#             self.assertEqual(ad_date.year, expected_ad_date[0])
#             self.assertEqual(ad_date.month, expected_ad_date[1])
#             self.assertEqual(ad_date.day, expected_ad_date[2])
#
#     def _convert_to_nepali_date(self, year, month, day):
#         # Implement your own conversion logic here using the library's functionality
#         # Replace this dummy implementation with the actual conversion code
#         nep_year = year + 56
#         nep_month = month + 2
#         nep_day = day + 6
#         return nep_year, nep_month, nep_day
#
#     def _convert_to_ad_date(self, year, month, day):
#         # Implement your own conversion logic here using the library's functionality
#         # Replace this dummy implementation with the actual conversion code
#         ad_year = year - 56
#         ad_month = month - 2
#         ad_day = day - 6
#         return ad_year, ad_month, ad_day

if __name__ == '__main__':
    unittest.main()
