# test_noaa_data_downloader.py
import unittest
from datetime import datetime
from src.data_pull.noaa_data_downloader import NOAADataDownloader

class TestNOAADataDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = NOAADataDownloader('http://nomads.ncep.noaa.gov:80/dods/', 'gfs')

    def test_construct_url(self):
        date = datetime(2024, 10, 17)
        forecast_hour = 6
        expected_url = 'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs20241017/gfs_0p25_06z'
        constructed_url = self.downloader.construct_url(asof_date=date, forecast_hour=forecast_hour)
        self.assertEqual(constructed_url, expected_url)

    def test_list_available_files(self):
        url = 'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs20241017/'
        files = self.downloader.list_available_files(url)
        # We can't test the exact files, but we can check the response type.
        self.assertIsInstance(files, list)
