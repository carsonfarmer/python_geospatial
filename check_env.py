import warnings

with warnings.catch_warnings(record=True) as w:

    # Main stuff
    import numpy
    import pandas
    import scipy
    import sqlite3
    import matplotlib
    import shapely
    import fiona
    import rasterio
    import pyproj
    import descartes
    import geopandas
    import shapefile
    import cartopy
    import mplexporter
    import mplleaflet
    import geojsonio

    # Optional stuff
    try:
        import mpl_toolkits.basemap
        import psycopg2
    except ImportError, err:
        print("Error: " + unicode(err))
        print("This is not a required package.\n")
        print("See Known Issues for additional information: "
              "https://github.com/cfarmer/python_geospatial/blob/master/install.md#known-issues")

    if len(w) > 0:
        for i in w:
            if "openpyxl" in unicode(i.message):
                print("\nPandas is installed, but you might have a dependency issue. "
                      "To fix this, try the following:\n"
                      "   $ pip install openpyxl\n"
                      "   $ pip uninstall openpyxl\n"
                      "   $ pip install openpyxl==1.8.6\n"
                      "See Known Issues for additional information: "
                      "https://github.com/cfarmer/python_geospatial/blob/master/install.md#known-issues")
        import sys
        sys.exit(0)

print("Everything looks good!")
