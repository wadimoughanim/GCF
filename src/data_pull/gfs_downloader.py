from src.data_pull.noaa_data_downloader import NOAADataDownloader

class GFSDownloader(NOAADataDownloader):
    def __init__(self):
        super().__init__('http://nomads.ncep.noaa.gov:80/dods/', 'gfs')
