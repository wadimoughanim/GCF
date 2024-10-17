# test_gdas_downloader.py
import unittest
from datetime import datetime
from src.data_pull.gdas_downloader import GDASDownloader

class TestGDASDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = GDASDownloader()

    def test_construct_url(self):
        date = datetime(2024, 10, 17)
        forecast_hour = 12
        expected_url = 'http://nomads.ncep.noaa.gov:80/dods/gdas_0p25/gdas20241017/gdas_0p25_12z'
        constructed_url = self.downloader.construct_url(asof_date=date, forecast_hour=forecast_hour)
        self.assertEqual(constructed_url, expected_url)
