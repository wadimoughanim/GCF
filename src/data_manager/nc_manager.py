import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class NCManager:
    def __init__(self, nc_path):
        self.nc_path = nc_path
        self.ds = self._load_ds(nc_path)

    def _load_ds(self, nc_path: str) -> xr.Dataset:
        return xr.open_dataset(nc_path)
    
    def list_variables(self):
        return list(self.ds.data_vars)

    def plot_variable(self, variable_name, time_idx=0, level=None):
        """
        Plot a variable at a given time and optional level.
        """
        data = self.ds[variable_name]
        if level:
            data_at_level = data.sel(lev=level).isel(time=time_idx)
        else:
            data_at_level = data.isel(time=time_idx)
        
        data_at_level.plot()
        plt.show()

    def plot_time_series(self, variable_name, lat, lon, level=None):
        """
        Plot the time evolution of a variable at a fixed location (lat/lon) and optional level.
        """
        data = self.ds[variable_name].sel(lat=lat, lon=lon, method='nearest')
        if level is not None:
            data_at_location = data.sel(lev=level)
        else:
            data_at_location = data
        
        plt.figure(figsize=(8, 6))
        data_at_location.plot()
        plt.title(f'{variable_name} time series at lat: {lat}, lon: {lon}')
        plt.show()

    def _diaporama_map_matplotlib(self, variable_name, level=None):
        """
        Create a diaporama with a slider in matplotlib. Ensures consistent axis limits and figure size.
        """
        data = self.ds[variable_name]
        if level is not None:
            data_at_level = data.sel(lev=level)
        else:
            data_at_level = data

        fig, ax = plt.subplots(figsize=(8, 6))
        plt.subplots_adjust(bottom=0.25)
        initial_time = 0
        data_at_time = data_at_level.isel(time=initial_time)
        im = data_at_time.plot(ax=ax, add_colorbar=False)

        # Keep axis limits and colorbar consistent
        vmin, vmax = data_at_time.min(), data_at_time.max()
        colorbar = fig.colorbar(im, ax=ax)

        ax_time = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
        slider = Slider(ax_time, 'Time', 0, len(data_at_level['time']) - 1, valinit=initial_time, valstep=1)

        def update(val):
            time_idx = int(slider.val)
            data_at_time = data_at_level.isel(time=time_idx)

            # Clear the previous plot
            ax.clear()

            # Plot the data with consistent axis limits and a single colorbar
            im = data_at_time.plot(ax=ax, vmin=vmin, vmax=vmax, add_colorbar=False)
            
            # Update the colorbar
            colorbar.update_normal(im)

            ax.set_title(f'{variable_name} at time index {time_idx}')
            fig.canvas.draw_idle()

        slider.on_changed(update)
        plt.show()

    def visualize(self, variable_name, lat=None, lon=None, level=None, time_idx=None):
        """
        Global method to decide what to visualize based on inputs.
        If lat/lon are provided, it plots time series. If time_idx is provided, it plots the map at that time.
        Otherwise, it plots a diaporama of maps across time.
        """
        if lat is not None and lon is not None:
            # Plot time series at specific lat/lon
            self.plot_time_series(variable_name, lat, lon, level)
        elif time_idx is not None:
            # Plot specific time index
            self.plot_variable(variable_name, time_idx, level)
        else:
            # Create diaporama for map over time using matplotlib slider
            self._diaporama_map_matplotlib(variable_name, level)

if __name__ == '__main__':
    path = r'D:\GCF\data\gfs\gfs_20241017_00z.nc'
    data_manager = NCManager(path)
    
    # List available variables
    # print(data_manager.list_variables())
    
    # Use the global visualize function to plot maps, time series, or diaporama
    variable = 'tmp2m'
    
    # For time evolution at specific lat/lon (time series)
    data_manager.visualize(variable_name=variable, lat=30, lon=50)

    # For diaporama (evolving maps across time)
    data_manager.visualize(variable_name=variable)

    # For static map at a specific time
    data_manager.visualize(variable_name=variable, time_idx=0)
