# 07_regression.py 
# Fig 6 — Regression scatter plots (3 pillars vs overall)

import sys
sys.path.append('.')
from analysis.setup_00 import *
from analysis.data_loader_01 import india_ts

fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

pillar_pairs = [
    ('Investment', 'Investment & Development', PILLAR_COLORS[1]),
    ('Appeal',     'Appeal',                   PILLAR_COLORS[2]),
    ('Readiness',  'Readiness',                PILLAR_COLORS[3]),
]

for ax, (col, label, color) in zip(axes, pillar_pairs):
    x = india_ts[col].values
    y = india_ts['Overall'].values

    slope, intercept, r, p, se = stats.linregress(x, y)
    x_line = np.linspace(x.min() - 0.5, x.max() + 0.5, 100)
    y_line = slope * x_line + intercept

    ax.scatter(x, y, color=color, s=70, zorder=5,
               edgecolors='white', linewidth=0.8)
    ax.plot(x_line, y_line, color='#333333', linewidth=1.8, zorder=4)

    # Year labels on each point
    for xi, yi, yr in zip(x, y, YEARS):
        ax.annotate(str(yr)[2:], (xi, yi),
                    textcoords='offset points',
                    xytext=(4, 4), fontsize=7, color='#555555')

    # Equation box
    sign    = '+' if intercept >= 0 else '−'
    eq_str  = (f'ŷ = {slope:.3f}x {sign} {abs(intercept):.2f}\n'
               f'r = {r:.3f},  r² = {r**2:.3f}')
    ax.text(0.05, 0.93, eq_str,
            transform=ax.transAxes, fontsize=8.5,
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#F8F9FA',
                      edgecolor=color, linewidth=1.5))

    ax.set_title(f'{label} → Overall', fontweight='bold')
    ax.set_xlabel(label)
    ax.set_ylabel('Overall Score')
    ax.grid(alpha=0.2)

plt.suptitle('Fig 6: Regression of Each Pillar vs Overall Score (India 2015–2025)',
             fontweight='bold', fontsize=12, y=1.02)
plt.tight_layout()
plt.savefig('analysis/charts/fig6_regression_scatter.png')
plt.show()
print('Fig 6 saved → analysis/charts/fig6_regression_scatter.png')