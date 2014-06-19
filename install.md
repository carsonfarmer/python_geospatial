# Installation Instructions 

## Required Steps
1. Install [Anaconda](http://continuum.io/downloads) (I'm using Anaconda-2.0.1 [64-Bit - Python 2.7])
2. Create a new virtual environment
```bash
conda create -n scipygis pandas ipython-notebook
source acivate scipygis
conda install pip
```
3. Install required packages
```bash
conda install matplotlib
conda install shapely
conda install fiona
pip install pyproj
pip install descartes
pip install rasterio
```
4. Install geopandas (important!)
```bash
pip install git+git://github.com/kjordahl/geopandas.git
```
5. Install (web)mapping packages
    * Cartopy (also for static maps)
```bash
pip install pyshp
pip install git+git://github.com/SciTools/cartopy.git
```
    * mplleaflet (for making slippy maps)
```bash
pip install git+git://github.com/mpld3/mplexporter.git
pip install git+git://github.com/jwass/mplleaflet.git
```
    * geojson.py for shooting data to the web!
```bash
pip install git+git://github.com/jwass/geojsonio.py.git
```

## Optional Steps

1. Basemap, a common package for making static maps
```bash
conda install basemap
```
2. Install `psycopg2` for interacting with PostGIS
```bash
pip install psycopg2
```

## Known issues

1. If you don't already have it, you'll need to install git
    * Linux: `sudo apt-get install git`
    * OSX:   `brew install git`
2. The `openpyxl` dependency of `pandas` produces a funny warning
    * ```python
    UserWarning: Installed openpyxl is not supported at this time. Use >=1.6.1 and <2.0.0
    ```
    * To fix this warning, try the following:
```bash
pip install openpyxl
pip uninstall openpyxl
pip install openpyxl==1.8.6 
```
3. On vanilla Ubuntu, you might need to install `g++` before installing `rasterio`:
```v
sudo apt-get install g++
```
4. On OSX (Mavericks), if you don't already have developer tools installed, `pip install pyproj` will 
probably fail (due to missing `gcc`) and then ask you if you want to install them, so click 'yes' and 
then rerun `pip install pyproj`.
5. Linux install before:
```bash
sudo add-apt-repository -y ppa:ubuntugis/ppa
sudo apt-get update -qq
sudo apt-get install -y gdal-bin libgdal-dev
```
6. OSX install before:
    * First install [`brew`](http://brew.sh/)
```bash
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
brew doctor
brew update
brew install gdal
```
7. If you don't already have it, you might need `cython`
```bash
conda install cython
```
