# 05_india_vs_global.py 
# Fig 4 — India vs global average (2015–2025) with filled gap

import sys
sys.path.append('.')
from analysis.setup_00 import *
from analysis.data_loader_01 import india_ts, global_avg

india_overall = india_ts['Overall'].values
global_vals   = global_avg[YEARS].values

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(YEARS, india_overall, color=INDIA_COLOR, marker='o', linewidth=2.5,
        markersize=7, label='India')
ax.plot(YEARS, global_vals, color=WORLD_COLOR, marker='s', linewidth=2.5,
        linestyle='--', markersize=7, label='Sample Average (25 countries)')

# Fill — green when India above, red when below
ax.fill_between(YEARS, india_overall, global_vals,
                where=(india_overall >= global_vals),
                interpolate=True, alpha=0.2, color='#2ECC71',
                label='India above avg')
ax.fill_between(YEARS, india_overall, global_vals,
                where=(india_overall < global_vals),
                interpolate=True, alpha=0.2, color='#E74C3C',
                label='India below avg')

# Annotate 2022 peak
ax.annotate(f'2022: India peaks\nat {india_overall[7]:.2f}',
            xy=(2022, india_overall[7]),
            xytext=(2020, india_overall[7] + 1.5),
            fontsize=8.5, color=INDIA_COLOR, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=INDIA_COLOR))

# Annotate 2025 gap
gap_2025 = global_vals[-1] - india_overall[-1]
ax.annotate(f'Gap: −{gap_2025:.2f}',
            xy=(2025, (india_overall[-1] + global_vals[-1]) / 2),
            fontsize=9, color='#C0392B', ha='right')

ax.set_title('India vs Sample Average — Overall WTR Score (2015–2025)',
             fontweight='bold', pad=12)
ax.set_xlabel('Year', labelpad=8)
ax.set_ylabel('Overall Score', labelpad=8)
ax.set_xticks(YEARS)
ax.set_xticklabels(YEARS, rotation=45)
ax.grid(alpha=0.25)
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig('analysis/charts/fig4_india_vs_global_avg.png')
plt.show()
print('Fig 4 saved → analysis/charts/fig4_india_vs_global_avg.png')