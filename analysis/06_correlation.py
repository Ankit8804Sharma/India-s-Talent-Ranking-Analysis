# 06_correlation.py 
# Fig 5 — Correlation heatmap + bar chart (side by side)

import sys
sys.path.append('.')
from analysis.setup import *
from analysis.data_load import india_ts

corr_matrix       = india_ts.corr()
corr_with_overall = corr_matrix['Overall'].drop('Overall')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left: Heatmap 
sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='RdYlGn',
            center=0, vmin=-1, vmax=1,
            linewidths=0.5, linecolor='white',
            square=True, cbar_kws={'shrink': 0.8},
            ax=ax1, annot_kws={'size': 11, 'weight': 'bold'})
ax1.set_title('Pillar Correlation Matrix (India 2015–2025)',
              fontweight='bold', pad=10)
ax1.set_xticklabels(['Overall', 'Investment', 'Appeal', 'Readiness'],
                    rotation=30, ha='right')
ax1.set_yticklabels(['Overall', 'Investment', 'Appeal', 'Readiness'],
                    rotation=0)

# Right: Bar chart 
bar_colors = [PILLAR_COLORS[1], PILLAR_COLORS[2], PILLAR_COLORS[3]]
bars = ax2.barh(corr_with_overall.index, corr_with_overall.values,
                color=bar_colors, edgecolor='white', linewidth=0.6)

for bar, val in zip(bars, corr_with_overall.values):
    ax2.text(val + (0.02 if val >= 0 else -0.02),
             bar.get_y() + bar.get_height() / 2,
             f'r = {val:.3f}',
             va='center', ha='left' if val >= 0 else 'right',
             fontsize=10.5, fontweight='bold')

ax2.axvline(0, color='#333333', linewidth=0.8)
ax2.set_xlim(-0.6, 1.1)
ax2.set_title('Correlation with Overall Score', fontweight='bold', pad=10)
ax2.set_xlabel('Pearson r', labelpad=8)
ax2.grid(axis='x', alpha=0.3)
ax2.text(0.98, 0.05, 'Readiness > Investment > Appeal',
         transform=ax2.transAxes, ha='right',
         fontsize=8.5, color='#555555', style='italic')

plt.suptitle('Fig 5: Correlation Analysis — India Pillar Scores',
             fontweight='bold', fontsize=12, y=1.01)
plt.tight_layout()
plt.savefig('analysis/charts/fig5_correlation.png')
plt.show()
print('Fig 5 saved -> analysis/charts/fig5_correlation.png')
print('\nCorrelations with Overall:')
print(corr_with_overall.to_string())