# 03_global_rankings.py
# Fig 1 — Global Rankings 2025 (all 25 countries, India highlighted)

import sys
sys.path.append('.')
from analysis.setup_00 import *
from analysis.data_loader_01 import snap25, global_avg

fig, ax = plt.subplots(figsize=(14, 7))

colors = [INDIA_COLOR if c == 'India' else BAR_BASE for c in snap25['Country']]
bars = ax.bar(snap25['Country'], snap25['Score'], color=colors,
              edgecolor='white', linewidth=0.6, zorder=3)

# Rank label above each bar
for bar, row in zip(bars, snap25.itertuples()):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            f'#{int(row.Rank)}',
            ha='center', va='bottom', fontsize=7.5,
            color=INDIA_COLOR if row.Country == 'India' else '#555555',
            fontweight='bold' if row.Country == 'India' else 'normal')

# Annotate India bar
india_idx = snap25[snap25.Country == 'India'].index[0]
india_bar = bars[india_idx]
ax.annotate('India\n48.96',
            xy=(india_bar.get_x() + india_bar.get_width() / 2, 48.96),
            xytext=(india_bar.get_x() + india_bar.get_width() / 2 + 2.5, 54),
            fontsize=9, color=INDIA_COLOR, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=INDIA_COLOR, lw=1.5))

# Sample average line
ax.axhline(global_avg[2025], color='#333333', linestyle='--', linewidth=1.2)

patches = [
    mpatches.Patch(color=INDIA_COLOR, label='India'),
    mpatches.Patch(color=BAR_BASE,    label='Other countries'),
    Line2D([0], [0], color='#333333', linestyle='--',
           label=f'Sample avg ({global_avg[2025]:.2f})'),
]
ax.legend(handles=patches, fontsize=9, loc='upper right')

ax.set_title('IMD World Talent Ranking 2025 — Overall Scores (25-Country Sample)',
             fontweight='bold', pad=14)
ax.set_xlabel('Country', labelpad=8)
ax.set_ylabel('Overall Score (0–100)', labelpad=8)
ax.set_ylim(20, 75)
ax.set_xticklabels(snap25['Country'], rotation=45, ha='right', fontsize=8.5)
ax.grid(axis='y', alpha=0.3, zorder=0)

plt.tight_layout()
plt.savefig('analysis/charts/fig1_global_rankings_2025.png')
plt.show()
print('Fig 1 saved → analysis/charts/fig1_global_rankings_2025.png')