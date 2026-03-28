# 09_hypothesis_test.py 
# Fig 8 — t-distribution curve with rejection/acceptance regions
# H₀: India 2025 score = world mean   H₁: India 2025 ≠ world mean (two-tailed)

import sys
sys.path.append('.')
from analysis.setup_00 import *

# Test parameters 
india_score = 48.959
world_mean  = 49.943
sigma       = 6.84
n           = 24
df_val      = n - 1                                      # 23
t_calc      = (india_score - world_mean) / (sigma / math.sqrt(n))
alpha       = 0.05
t_crit      = t_dist.ppf(1 - alpha / 2, df=df_val)      # ≈ 2.069

fig, ax = plt.subplots(figsize=(12, 5.5))

x = np.linspace(-4.5, 4.5, 1000)
y = t_dist.pdf(x, df=df_val)

ax.plot(x, y, color='#2C3E50', linewidth=2)

# Acceptance region
x_acc = x[(x >= -t_crit) & (x <= t_crit)]
ax.fill_between(x_acc, t_dist.pdf(x_acc, df=df_val),
                color='#2ECC71', alpha=0.25,
                label='Acceptance Region (α = 0.05)')

# Rejection tails
for x_rej, lbl in [(x[x <= -t_crit], 'Rejection Region'),
                   (x[x >=  t_crit], None)]:
    ax.fill_between(x_rej, t_dist.pdf(x_rej, df=df_val),
                    color='#E74C3C', alpha=0.35,
                    label=lbl if lbl else '_nolegend_')

# Critical value lines
for tc, lbl in [(-t_crit, f'−t_crit = {-t_crit:.3f}'),
                ( t_crit, f'+t_crit = +{t_crit:.3f}')]:
    ax.axvline(tc, color='#E74C3C', linestyle='--', linewidth=1.3)
    ax.text(tc, max(y) * 0.72, lbl, ha='center', fontsize=8.5,
            color='#E74C3C', fontweight='bold')

# T_calc marker
y_calc = t_dist.pdf(t_calc, df=df_val)
ax.axvline(t_calc, color=INDIA_COLOR, linewidth=2)
ax.plot(t_calc, y_calc, 'o', color=INDIA_COLOR, markersize=10, zorder=6)
ax.annotate(f'T_calc = {t_calc:.3f}\n(India 2025)',
            xy=(t_calc, y_calc),
            xytext=(t_calc + 0.7, y_calc + 0.02),
            fontsize=9, color=INDIA_COLOR, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=INDIA_COLOR))

# Decision box
ax.text(0, max(y) * 0.45,
        f'FAIL TO REJECT H₀\n'
        f'|T_calc| = {abs(t_calc):.3f} < T_crit = {t_crit:.3f}\n'
        f"India's score is NOT significantly\ndifferent from world mean",
        ha='center', va='center', fontsize=9,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#EBF5FB',
                  edgecolor='#2C3E50', linewidth=1.5))

ax.set_title(f'Fig 8: Two-Tailed t-Test — India 2025 vs Sample Mean\n'
             f'H₀: μ_India = μ_world   |   df={df_val}, α={alpha}',
             fontweight='bold', pad=12)
ax.set_xlabel('t-value', labelpad=8)
ax.set_ylabel('Probability Density', labelpad=8)
ax.legend(fontsize=9)
ax.set_xlim(-4.5, 4.5)
ax.grid(alpha=0.2)

plt.tight_layout()
plt.savefig('analysis/charts/fig8_ttest_distribution.png')
plt.show()
print(f'Fig 8 saved → analysis/charts/fig8_ttest_distribution.png')
print(f'    T_calc = {t_calc:.4f},  T_crit = ±{t_crit:.4f},  df = {df_val}')