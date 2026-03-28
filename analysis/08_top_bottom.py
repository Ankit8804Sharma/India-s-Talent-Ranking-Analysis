# 08_top_bottom.py 
# Fig 7 — Top 5 and Bottom 5 countries (2025)

import sys
sys.path.append('.')
from analysis.setup_00 import *
from analysis.data_loader_01 import snap25

top5    = snap25.head(5)
bottom5 = snap25.tail(5).sort_values('Rank', ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Top 5
colors_top = ['#F4D03F', '#BDC3C7', '#CD7F32', '#5DADE2', '#5DADE2']
bars_top   = ax1.barh(top5['Country'][::-1], top5['Score'][::-1],
                      color=colors_top[::-1], edgecolor='white')
for bar, (_, row) in zip(bars_top, top5[::-1].iterrows()):
    ax1.text(bar.get_width() + 0.3,
             bar.get_y() + bar.get_height() / 2,
             f'{row.Score:.2f}  (#{int(row.Rank)})',
             va='center', fontsize=9, fontweight='bold')
ax1.set_xlim(0, 80)
ax1.set_title('Top 5 Countries — 2025', fontweight='bold', color='#1A5276')
ax1.set_xlabel('Overall Score')
ax1.grid(axis='x', alpha=0.3)

# Bottom 5
colors_bot = ['#E74C3C', '#C0392B', '#A93226', '#922B21', '#7B241C']
bars_bot   = ax2.barh(bottom5['Country'], bottom5['Score'],
                      color=colors_bot, edgecolor='white')
for bar, (_, row) in zip(bars_bot, bottom5.iterrows()):
    ax2.text(bar.get_width() + 0.3,
             bar.get_y() + bar.get_height() / 2,
             f'{row.Score:.2f}  (#{int(row.Rank)})',
             va='center', fontsize=9, fontweight='bold')
ax2.set_xlim(0, 65)
ax2.set_title('Bottom 5 Countries — 2025', fontweight='bold', color='#922B21')
ax2.set_xlabel('Overall Score')
ax2.grid(axis='x', alpha=0.3)

plt.suptitle('Fig 7: Top 5 and Bottom 5 Countries in IMD WTR 2025',
             fontweight='bold', fontsize=12, y=1.02)
plt.tight_layout()
plt.savefig('analysis/charts/fig7_top5_bottom5.png')
plt.show()
print('Fig 7 saved → analysis/charts/fig7_top5_bottom5.png')