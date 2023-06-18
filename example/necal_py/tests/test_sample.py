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
