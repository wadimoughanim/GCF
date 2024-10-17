import os
import xarray as xr
from datetime import datetime
from src.data_pull.gfs_downloader import GFSDownloader
from src.data_pull.gdas_downloader import GDASDownloader

def download_noaa_opendap(data_type, date, cycle):
    if data_type == 'gfs':
        downloader = GFSDownloader()
    elif data_type == 'gdas':
        downloader = GDASDownloader()
    else:
        raise ValueError("Invalid data type. Please use 'gfs' or 'gdas'.")

    url = downloader.construct_url(asof_date=datetime.strptime(date, "%Y%m%d"), forecast_hour=int(cycle))
    print(f"Accessing data from: {url}")

    try:
        dataset = xr.open_dataset(url)
        print("Available variables in the dataset:")
        print(dataset.data_vars)

        output_path = os.path.join(downloader.data_dir, f"{data_type}_{date}_{cycle}z.nc")
        dataset.to_netcdf(output_path)
        print(f"Dataset saved locally at: {output_path}")

    except Exception as e:
        print(f"Error downloading the dataset from {url}: {e}")
