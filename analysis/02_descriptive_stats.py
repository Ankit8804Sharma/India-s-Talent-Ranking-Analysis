# 02_descriptive_stats.py 
# Fig 3 — Descriptive statistics styled table (India 2015–2025)

import sys
sys.path.append('.')
from analysis.setup import *
from analysis.data_load import india_ts

def desc_stats(series):
    s = series.dropna()
    return {
        'Mean'     : round(s.mean(), 3),
        'Median'   : round(s.median(), 3),
        'Std Dev'  : round(s.std(ddof=1), 3),
        'Variance' : round(s.var(ddof=1), 3),
        'Min'      : round(s.min(), 3),
        'Max'      : round(s.max(), 3),
        'Range'    : round(s.max() - s.min(), 3),
        'Skewness' : round(stats.skew(s), 3),
        'Kurtosis' : round(stats.kurtosis(s), 3),
    }

stat_rows = [
    ('Overall Score',    india_ts['Overall']),
    ('Investment & Dev', india_ts['Investment']),
    ('Appeal',           india_ts['Appeal']),
    ('Readiness',        india_ts['Readiness']),
]

stat_df = pd.DataFrame(
    {name: desc_stats(series) for name, series in stat_rows}
).T

fig, ax = plt.subplots(figsize=(13, 3.5))
ax.axis('off')

col_labels = ['Pillar / Score'] + list(stat_df.columns)
table_data = [[row] + list(stat_df.loc[row]) for row in stat_df.index]

tbl = ax.table(cellText=table_data, colLabels=col_labels,
               loc='center', cellLoc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(9.5)
tbl.scale(1, 1.7)

for j in range(len(col_labels)):
    tbl[0, j].set_facecolor('#2C3E50')
    tbl[0, j].set_text_props(color='white', fontweight='bold')

row_colors = ['#F2F4F4', '#FFFFFF', '#F2F4F4', '#FFFFFF']
for i, rc in enumerate(row_colors, start=1):
    for j in range(len(col_labels)):
        tbl[i, j].set_facecolor(rc)
    tbl[i, 0].set_text_props(fontweight='bold')

ax.set_title('Descriptive Statistics — India (2015–2025)',
             fontweight='bold', pad=12, fontsize=11, y=0.95)

plt.tight_layout()
plt.savefig('analysis/charts/fig3_descriptive_stats_table.png')
plt.show()
print('Fig 3 saved -> analysis/charts/fig3_descriptive_stats_table.png')
print(stat_df.to_string())