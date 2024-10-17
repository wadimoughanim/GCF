from src.data_pull.download_noaa_opendap import download_noaa_opendap

if __name__ == "__main__":
    data_type = input("Enter the data type (gfs/gdas): ").lower()
    date = input("Enter the date (YYYYMMDD): ")
    cycle = input("Enter the cycle (00, 06, 12, 18): ")

    download_noaa_opendap(data_type, date, cycle)
