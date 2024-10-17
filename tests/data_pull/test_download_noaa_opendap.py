import unittest
from unittest.mock import patch, MagicMock
from src.data_pull.download_noaa_opendap import download_noaa_opendap

class TestDownloadNOAAOpenDAP(unittest.TestCase):
    @patch('src.data_pull.gfs_downloader.GFSDownloader.construct_url')
    @patch('xarray.open_dataset')
    def test_download_gfs(self, mock_open_dataset, mock_construct_url):
        # Mock URL construction
        mock_construct_url.return_value = 'http://fakeurl.com'
        
        # Mock dataset returned by xarray.open_dataset
        mock_dataset = MagicMock()
        mock_dataset.data_vars = ['TMP', 'UGRD']
        mock_open_dataset.return_value = mock_dataset

        # Test GFS download
        download_noaa_opendap('gfs', '20241017', '00')

        # Check that xarray.open_dataset was called
        mock_open_dataset.assert_called_once_with('http://fakeurl.com')

    @patch('src.data_pull.gdas_downloader.GDASDownloader.construct_url')
    @patch('xarray.open_dataset')
    def test_download_gdas(self, mock_open_dataset, mock_construct_url):
        # Mock URL construction
        mock_construct_url.return_value = 'http://fakeurl.com'
        
        # Mock dataset returned by xarray.open_dataset
        mock_dataset = MagicMock()
        mock_dataset.data_vars = ['TMP', 'UGRD']
        mock_open_dataset.return_value = mock_dataset

        # Test GDAS download
        download_noaa_opendap('gdas', '20241017', '12')

        # Check that xarray.open_dataset was called
        mock_open_dataset.assert_called_once_with('http://fakeurl.com')


if __name__ == "__main__":
    unittest.main()
