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
        import psycopg2
        import mpl_toolkits.basemap
    except ImportError, err:
        print("Error: " + unicode(err))
        print("This is not a required package. "
              "See Known Issues for additional information:\n"
              "https://github.com/carsonfarmer/python_geospatial/blob/master/"
              "install.md#known-issues")
        import sys
        sys.exit(0)

print("Everything looks good!")
