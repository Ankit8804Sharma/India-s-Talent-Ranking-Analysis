# 00_setup.py
# Global imports, style config, and colour palette
# Run this file first or import it at the top of every other script

import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import seaborn as sns
from scipy import stats
from scipy.stats import t as t_dist
import math
import os

# Style
plt.rcParams.update({
    'font.family'       : 'DejaVu Sans',
    'axes.spines.top'   : False,
    'axes.spines.right' : False,
    'figure.dpi'        : 150,
    'savefig.dpi'       : 200,
    'savefig.bbox'      : 'tight',
    'axes.titlesize'    : 13,
    'axes.labelsize'    : 11,
    'xtick.labelsize'   : 9,
    'ytick.labelsize'   : 9,
})

# Colours
INDIA_COLOR   = '#FF6B35'
WORLD_COLOR   = '#4A90D9'
SWISS_COLOR   = '#E63946'
PILLAR_COLORS = ['#2EC4B6', '#FF9F1C', '#E71D36', '#011627']
BAR_BASE      = '#B0C4DE'

# Output folder 
os.makedirs('analysis/charts', exist_ok=True)

# Constants 
EXCEL_FILE = 'IMD_WTR_Dataset.xlsx'
YEARS      = list(range(2015, 2026))