# 12_heatmap_all.py 
# Fig 11 — 25-country × 11-year heatmap with India row highlighted

import sys
sys.path.append('.')
from analysis.setup import *
from analysis.data_load import df_overall

# Sort by 2025 score
hm_df = df_overall[YEARS].copy()
hm_df = hm_df.sort_values(2025, ascending=False)

fig, ax = plt.subplots(figsize=(15, 9))

sns.heatmap(
    hm_df,
    cmap='YlOrRd',
    annot=True,
    fmt='.1f',
    linewidths=0.4,
    linecolor='white',
    cbar_kws={'label': 'Overall WTR Score', 'shrink': 0.7},
    annot_kws={'size': 7.5},
    ax=ax
)

# Highlight India row with orange border
india_row_idx = list(hm_df.index).index('India')
for col_idx in range(len(YEARS)):
    ax.add_patch(plt.Rectangle(
        (col_idx, india_row_idx), 1, 1,
        fill=False, edgecolor=INDIA_COLOR, lw=2.5, zorder=10
    ))

# Bold orange India y-tick label
for lbl in ax.get_yticklabels():
    if lbl.get_text() == 'India':
        lbl.set_color(INDIA_COLOR)
        lbl.set_fontweight('bold')

ax.set_title('Fig 11 (Bonus): Overall WTR Scores — 25 Countries × 2015–2025\n'
             '(Sorted by 2025 score, India row highlighted in orange)',
             fontweight='bold', pad=12)
ax.set_xlabel('Year', labelpad=8)
ax.set_ylabel('Country', labelpad=8)
ax.set_xticklabels(YEARS, rotation=45)

plt.tight_layout()
plt.savefig('analysis/charts/fig11_heatmap_all_countries.png')
plt.show()
print('Fig 11 saved -> analysis/charts/fig11_heatmap_all_countries.png')