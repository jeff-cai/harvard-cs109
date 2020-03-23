#IPython is what you are using now to run the notebook
import IPython
print("IPython version:      {} (need at least 3.0.0)".format(IPython.__version__))

# Numpy is a library for working with Arrays
import numpy as np
print("Numpy version:        {} (need at least 1.9.1)".format(np.__version__))

# SciPy implements many different numerical algorithms
import scipy as sp
print("SciPy version:        {} (need at least 0.15.1)".format(sp.__version__))

# Pandas makes working with data tables easier
import pandas as pd
print("Pandas version:       {} (need at least 0.16.2)".format(pd.__version__))

# Module for plotting
import matplotlib
print("Mapltolib version:    {} (need at least 1.4.1)".format(matplotlib.__version__))

# SciKit Learn implements several Machine Learning algorithms
import sklearn
print("Scikit-Learn version: {} (need at least 0.16.1)".format(sklearn.__version__))

# Requests is a library for getting data from the Web
import requests
print("requests version:     {} (need at least 2.0.0)".format(requests.__version__))

#BeautifulSoup is a library to parse HTML and XML documents
import bs4
print("BeautifulSoup version:{} (need at least 4.4)".format(bs4.__version__))

import pyquery
print("Loaded PyQuery")


import seaborn as sns
print("Seaborn version: {}".format(sns.__version__))
