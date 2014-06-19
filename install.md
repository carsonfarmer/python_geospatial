# Installation Instructions 

## Base Install

* Install [Anaconda](http://continuum.io/downloads) (I'm using Anaconda-2.0.1 [64-Bit - Python 2.7])

* Create a new virtual environment
```bash
conda create -n scipygis pandas ipython-notebook
source acivate scipygis
conda install pip
```

* If you don't already have it, you might need to install `cython`
```bash
conda install cython
```

* Install required packages
```bash
conda install matplotlib
conda install shapely
conda install fiona
pip install pyproj
pip install descartes
pip install rasterio
```

* Install geopandas (important!)
```bash
pip install git+git://github.com/kjordahl/geopandas.git
```

## (Web)mapping Packages

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

## Optional Packages

* Install `basemap`, a common package for making static maps
```bash
conda install basemap
```

* Install `psycopg2` for interacting with PostGIS
```bash
pip install psycopg2
```

## Known Issues

* Linux Initial Setup
```bash
sudo add-apt-repository -y ppa:ubuntugis/ppa
sudo apt-get update -qq
sudo apt-get install -y gdal-bin libgdal-dev
```

* OSX Initial Setup:
    * First install [`brew`](http://brew.sh/)
```bash
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```
   * Then update and install `gdal`
```
brew doctor
brew update
brew install gdal
```

* If you don't already have it, you'll need to install `git`
    * Linux: `sudo apt-get install git`
    * OSX:   `brew install git`

* The `openpyxl` dependency of `pandas` may produce a funny warning: `UserWarning: Installed openpyxl is not supported at this time. Use >=1.6.1 and <2.0.0`

   * To fix this warning, try the following:
```bash
pip install openpyxl
pip uninstall openpyxl
pip install openpyxl==1.8.6 
```

* On vanilla Ubuntu, you might need to install `g++` before installing `rasterio`:
```
sudo apt-get install g++
```

* On OSX (Mavericks), if you don't already have developer tools installed, `pip install pyproj` will 
probably fail (due to missing `gcc`) and then ask you if you want to install them, so click 'yes' and 
then rerun `pip install pyproj`.
