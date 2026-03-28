# 11_radar_chart.py 
# Fig 10 — Radar/spider chart: India vs Switzerland vs 25-country avg

import sys
sys.path.append('.')
from analysis.setup_00 import *
from analysis.data_loader_01 import df_inv100, df_app100, df_rdy100

def get_scores_2025(country=None):
    if country:
        inv = df_inv100.loc[country, 2025]
        app = df_app100.loc[country, 2025]
        rdy = df_rdy100.loc[country, 2025]
    else:
        inv = df_inv100[2025].mean()
        app = df_app100[2025].mean()
        rdy = df_rdy100[2025].mean()
    return [inv, app, rdy]

india_r = get_scores_2025('India')
swiss_r = get_scores_2025('Switzerland')
avg_r   = get_scores_2025()

categories = ['Investment\n& Development', 'Appeal', 'Readiness']
N      = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

def close(lst):
    return lst + [lst[0]]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for vals, color, label in [
    (india_r, INDIA_COLOR, 'India'),
    (swiss_r, SWISS_COLOR, 'Switzerland (#1)'),
    (avg_r,   WORLD_COLOR, '25-Country Avg'),
]:
    ax.plot(angles, close(vals), color=color, linewidth=2.2,
            marker='o', markersize=7)
    ax.fill(angles, close(vals), color=color, alpha=0.12)
    for angle, val in zip(angles[:-1], vals):
        ax.text(angle, val + 3, f'{val:.1f}', ha='center', va='center',
                fontsize=8.5, color=color, fontweight='bold')

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10.5, fontweight='bold')
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80])
ax.set_yticklabels(['20', '40', '60', '80'], fontsize=8)
ax.grid(color='#BDC3C7', linewidth=0.7, linestyle='--')

handles = [
    mpatches.Patch(color=INDIA_COLOR, label='India',             alpha=0.8),
    mpatches.Patch(color=SWISS_COLOR, label='Switzerland (#1)',  alpha=0.8),
    mpatches.Patch(color=WORLD_COLOR, label='25-Country Avg',    alpha=0.8),
]
ax.legend(handles=handles, loc='upper right',
          bbox_to_anchor=(1.35, 1.15), fontsize=10)
ax.set_title('Fig 10 (Bonus): Pillar Comparison — India vs Switzerland vs Average (2025)',
             fontweight='bold', pad=20, fontsize=11)

plt.tight_layout()
plt.savefig('analysis/charts/fig10_radar_chart.png')
plt.show()
print('Fig 10 saved → analysis/charts/fig10_radar_chart.png')