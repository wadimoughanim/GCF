# noaa_data_downloader.py
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class NOAADataDownloader:
    def __init__(self, base_url, data_type):
        self.base_url = base_url  # The base URL for GrADS Data Server (e.g., http://nomads.ncep.noaa.gov:80/dods/)
        self.data_type = data_type  # Set the data type (gfs or gdas)
        self.data_dir = os.path.join('data', data_type)  # Separate folder for each type (gfs, gdas)

        # Create the data directory if it doesn't exist
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def list_available_files(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                dds_links = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.dds')]
                if dds_links:
                    return dds_links
                else:
                    print("No .dds files found.")
                    return None
            else:
                print(f"Error listing files at {url}: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error accessing {url}: {e}")
            return None

    def construct_url(self, asof_date=None, forecast_hour=None):
        if asof_date and forecast_hour is not None:
            date_str = asof_date.strftime('%Y%m%d')
            forecast_str = f"{forecast_hour:02d}"
            return f'{self.base_url}{self.data_type}_0p25/{self.data_type}{date_str}/{self.data_type}_0p25_{forecast_str}z'
        else:
            current_date = datetime.utcnow().strftime('%Y%m%d')
            return f'{self.base_url}{self.data_type}_0p25/{self.data_type}{current_date}/'
