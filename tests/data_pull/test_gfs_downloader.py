# test_gfs_downloader.py
import unittest
from datetime import datetime
from src.data_pull.gfs_downloader import GFSDownloader

class TestGFSDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = GFSDownloader()

    def test_construct_url(self):
        date = datetime(2024, 10, 17)
        forecast_hour = 0
        expected_url = 'http://nomads.ncep.noaa.gov:80/dods/gfs_0p25/gfs20241017/gfs_0p25_00z'
        constructed_url = self.downloader.construct_url(asof_date=date, forecast_hour=forecast_hour)
        self.assertEqual(constructed_url, expected_url)
