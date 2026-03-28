# 04_india_trends.py 
# Fig 2 — India's pillar score trends 2015–2025 (2022 peak annotated)

import sys
sys.path.append('.')
from analysis.setup import *
from analysis.data_load import india_ts

fig, ax = plt.subplots(figsize=(12, 6))

pillars  = ['Overall',       'Investment',              'Appeal',  'Readiness']
labels   = ['Overall Score', 'Investment & Development','Appeal',  'Readiness']
styles   = ['-',             '--',                      '-.',       ':']
markers  = ['o',             's',                       '^',        'D']

for col, lab, col_c, sty, mrk in zip(pillars, labels, PILLAR_COLORS, styles, markers):
    ax.plot(YEARS, india_ts[col].values, color=col_c, linestyle=sty,
            marker=mrk, markersize=6, linewidth=2, label=lab)

# Annotate 2022 peak
peak_val = india_ts.loc[2022, 'Overall']
ax.annotate(f'2022 Peak\n{peak_val:.2f}',
            xy=(2022, peak_val),
            xytext=(2020.3, peak_val + 1.8),
            fontsize=9, color=PILLAR_COLORS[0], fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=PILLAR_COLORS[0], lw=1.5))

ax.set_title("India's Pillar Score Trends (2015–2025)", fontweight='bold', pad=12)
ax.set_xlabel('Year', labelpad=8)
ax.set_ylabel('Score (0–100)', labelpad=8)
ax.set_xticks(YEARS)
ax.set_xticklabels(YEARS, rotation=45)
ax.grid(alpha=0.25)
ax.legend(fontsize=9, loc='lower right')
ax.set_ylim(35, 65)

plt.tight_layout()
plt.savefig('analysis/charts/fig2_india_pillar_trends.png')
plt.show()
print('Fig 2 saved -> analysis/charts/fig2_india_pillar_trends.png')