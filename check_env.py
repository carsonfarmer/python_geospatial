import warnings
import sys

with warnings.catch_warnings(record=True) as w:

    try:
        import numpy
        import pandas
        import scipy
        import sqlite3
    except ImportError, err:
        print("\nError: " + unicode(err))
        print("If you are getting this error, you probably need to:\n"
              "1) Install Anaconda (I'm using Anaconda-2.0.1 [Python 2.7])\n"
              "2) Create a new virtual environment:\n"
              "   $ conda create -n scipygis pandas ipython-notebook\n"
              "3) Activate your virtual environment:\n"
              "   $ source acivate scipygis")
        sys.exit(0)
    try:
        import matplotlib
        import shapely
        import fiona
        import mpl_toolkits.basemap
    except ImportError, err:
        print("\nError: " + unicode(err))
        print("If you are getting this error, you probably need to\n"
              "   $ conda install %s" % unicode(err)[unicode(err).rfind(" ")+1:])
        sys.exit(0)

    try:
        import rasterio
        import pyproj
        import descartes
    except ImportError, err:
        print("\nError: " + unicode(err))
        print("If you are getting this error, you probably need to\n"
              "1) Check that you have installed pip:\n"
              "   $ conda install pip\n"
              "2) Try installing the missing package via:\n"
              "   $ pip install %s" % unicode(err)[unicode(err).rfind(" ")+1:])

        print("If you are on Linux, you may need to install `g++`, and on OSX "
              "you'll probably need to install the developer tools.")
        sys.exit(0)

    try:
        import geopandas
        import shapefile
        import cartopy
        import mplexporter
        import mplleaflet
        import geojsonio
    except ImportError, err:
        print("\nError: " + unicode(err))
        print("If you are getting this error, you probably need to "
              "make sure Git is installed, and then try to\n"
              "`pip install` the library according to the instructions.\n"
              "See Known Issues for additional information: "
              "https://github.com/cfarmer/python_geospatial/blob/master/install.md#known-issues")

    try:
        import psycopg2
    except ImportError, err:
        print("\nError: " + unicode(err))
        print("You don't really need it,"
              " but if you want it, you might need to first "
              "install PostGIS, then \n   $ pip install psycopg2\n"
              "See Known Issues for additional information: "
              "https://github.com/cfarmer/python_geospatial/blob/master/install.md#known-issues")

    if len(w) > 0:
        for i in w:
            if "openpyxl" in unicode(i.message):
                print("\nPandas is installed, but you have a dependency issue. "
                      "To fix this, try the following:\n"
                      "   $ pip install openpyxl\n"
                      "   $ pip uninstall openpyxl\n"
                      "   $ pip install openpyxl==1.8.6\n"
                      "See Known Issues for additional information: "
                      "https://github.com/cfarmer/python_geospatial/blob/master/install.md#known-issues")
        sys.exit(0)

print("Everything looks good!")
