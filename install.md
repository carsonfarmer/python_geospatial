# Installation Instructions 

## Base Install

* Install [`Anaconda`](http://continuum.io/downloads) (I'm using Anaconda-2.1.0 [64-Bit - Python 2.7])
   * We're using `Anaconda` because it helps us to keep our `Python` environment clean and manageable. If you prefer, you can also use [`Canopy`](https://store.enthought.com/downloads/) or an another alternative `Python` environment.

* Create a new virtual environment (Skip this step on Windows, trust me, it'll be easier):

      ```bash
      conda create -n pygeo pandas ipython-notebook matplotlib
      source activate pygeo
      ```
* Install `pip` for later (`pip` allows us to install additional `Python` packages not available via `conda`:
      ```bash
      conda install pip
      ```

* If you don't already have it, you might need to install `cython`

      ```bash
      conda install cython
      ```

* Install required packages (on Windows, you might need to install [binaries from here](http://www.lfd.uci.edu/~gohlke/pythonlibs/) for `shapely`, `pyproj`, and `rasterio`).

      ```bash
      conda install shapely
      conda install fiona
      conda install PIL
      conda install pyproj
      conda install descartes
      pip install rasterio
      ```
  * You can use `pillow` in place of `PIL` if you like.
  * If any of the above commands cause an error, you can use `pip` instead (replace `PACKAGE` below with the package you are trying to install):

    ```bash
    pip install PACKAGE
    ```
  * or check to see if a `conda` package exists using `binstar`:

    ```bash
    conda install binstar
    binstar search -t conda PACKAGE
    ```
    * Make sure you find one for your OS. You can get more info about a package using the following command, which will also explain how to install the package:

      ```bash
      binstar show <USER/PACKAGE>
      ```
    * For example, I used the following to install `pyproj` on OSX:

      ```bash
      conda install --channel https://conda.binstar.org/asmeurer pyproj
      ```

* Install `geopandas` (important!)

      ```bash
      pip install geopandas
      ```

## (Web)mapping Packages

* Install `cartopy` (on Windows, use [binaries from here](http://www.lfd.uci.edu/~gohlke/pythonlibs/) for `cartopy`.)

    ```bash 
    pip install pyshp
    pip install cartopy
    ```

* Install `mplleaflet` (for making slippy maps). See the `Known Issues` below about install `git`.

    ```bash
    pip install git+git://github.com/mpld3/mplexporter.git
    pip install git+git://github.com/jwass/mplleaflet.git
    ```

* Install `geojson.py` for shooting data to the web!

    ```bash
    pip install git+git://github.com/jwass/geojsonio.py.git
    ```

## Optional Packages

* Install `basemap`, a common package for making static maps (I didn't install this):

    ```bash
    conda install basemap
    ```

* Install `psycopg2` for interacting with PostGIS (We don't need this, but I will do a demo with this):

    ```bash
    pip install psycopg2
    ```

## Install QGIS

* Go to the [official QGIS page](http://qgis.org/en/site/forusers/download.html) for details, or install via `brew` on OSX, `apt-get` on Linux, or `OSGeo4W` on Windows (Either way, this install will likely take quite a while).
  * I installed this on OSX via `homebrew` with:

    ```bash
    brew tap osgeo/osgeo4mac
    brew install qgis-26
    ```
  * On Linux, if you follow the `Linux Initial Setup` below first, you should be able to install QGIS with:

    ```bash
    sudo apt-get install qgis
    ```
    
  * On Windows, follow the instructions on the official QGIS page.

## Alternative Install Guide

* Here is the [install guide](https://github.com/kjordahl/SciPy2013#installation-instructions) from a [similar course](https://github.com/kjordahl/SciPy2013) last year.

## Known Issues

* In *some* cases, it may be better to `pip install shapely` than to `conda install shapely`, particularly when using `cartopy`.

### Linux Issues

* Initial Setup

    ```bash
    sudo apt-get install git
    sudo add-apt-repository -y ppa:ubuntugis/ppa
    sudo apt-get update -qq
    sudo apt-get install -y gdal-bin libgdal-dev
    ```

* On vanilla Ubuntu, you might need to install `g++` before installing `rasterio` and others:

      ```bash
      sudo apt-get install g++
      ```

### OS X Issues

* Initial Setup
   * First install [`brew`](http://brew.sh/): `ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`
   * Then update and install `gdal` (You might be able to skip this step if you `conda install fiona` [see above]).

      ```bash
      brew doctor
      brew update
      brew install git
      brew tap osgeo/osgeo4mac
      brew install gdal
      brew install qgis
      ```
      
* On Mavericks+ if you don't already have developer tools installed, `pip install pyproj` will 
probably fail (due to missing `gcc`) and then ask you if you want to install them, so click 'yes' and 
then rerun `pip install pyproj`.

* In *some* cases, importing `shapely` on OS X might fail while loading the GEOS library:
      ```bash
      OSError: Could not find library c or load any of its variants.
      ```
  * This can be fixed by using a newer version, or worked around by setting the following environment variable (add to your `.bash_profile`; see [this issue](https://github.com/cfarmer/python_geospatial/issues/3) for details):

      ```bash
      export DYLD_FALLBACK_LIBRARY_PATH=$(HOME)/lib:/usr/local/lib:/lib:/usr/lib
      ```

### Windows Issues

* Initial Setup
   * Download and install GDAL [from here](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal)
   * If you use this one, then you should also use the `fiona` binary from that site. Otherwise, you'll have to play around with system PATHs etc. Others have had success with [OSGeo4W](http://trac.osgeo.org/osgeo4w/), which includes many important libraries and their Python bindings.

* If you don't already have it, you'll need to install `git`:
    * Download and install git [from here](http://www.git-scm.com/downloads).
    * When installing, make sure you choose to "Use Git from the Windows Command Prompt" (You may also want to install optional Unix tools).
    * You can also download GitHub for Windows [here](https://windows.github.com/).

* On Windows, `source` is not needed when activating a virtual environment if you are using the Anaconda Command Prompt:  `activate scipygis`.
