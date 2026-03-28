# 10_forecast.py 
# Fig 9 — Actual trend + dashed forecast (2026–2030) with ±1SD band

import sys
sys.path.append('.')
from analysis.setup import *
from analysis.data_load import india_ts

x_hist = np.array(YEARS)
y_hist = india_ts['Overall'].values

slope, intercept, r, p, se = stats.linregress(x_hist, y_hist)

# Forecast 2026–2030
forecast_years = np.array([2026, 2027, 2028, 2029, 2030])
forecast_vals  = slope * forecast_years + intercept

# Residual SD for confidence band
y_pred_hist = slope * x_hist + intercept
sd_residual = (y_hist - y_pred_hist).std(ddof=2)

fig, ax = plt.subplots(figsize=(13, 6))

# Historical actual
ax.plot(x_hist, y_hist, color=INDIA_COLOR, marker='o', linewidth=2.5,
        markersize=7, label='Actual (2015–2025)', zorder=5)

# Fitted trend
ax.plot(x_hist, y_pred_hist, color='#7F8C8D', linewidth=1.2,
        linestyle=':', label='Fitted trend')

# Forecast line — connect from 2025
fc_x = np.concatenate([[2025], forecast_years])
fc_y = np.concatenate([[slope * 2025 + intercept], forecast_vals])
ax.plot(fc_x, fc_y, color=INDIA_COLOR, linewidth=2.5, linestyle='--',
        marker='D', markersize=7, label='Forecast (2026–2030)', zorder=5)

# ±1 SD band
ax.fill_between(fc_x, fc_y - sd_residual, fc_y + sd_residual,
                color=INDIA_COLOR, alpha=0.15, label='±1 SD band')

# Annotate forecast values
for yr, val in zip(forecast_years, forecast_vals):
    ax.text(yr, val + 0.3, f'{val:.2f}', ha='center',
            fontsize=8.5, color=INDIA_COLOR, fontweight='bold')

# Divider at 2025
ax.axvline(2025, color='#BDC3C7', linestyle='--', linewidth=1)
ax.text(2025.1, y_hist.min() + 0.3, 'Forecast ->',
        fontsize=8.5, color='#7F8C8D')

all_x = np.concatenate([x_hist, forecast_years])
ax.set_xticks(all_x)
ax.set_xticklabels([str(int(y)) for y in all_x], rotation=45)
ax.set_title('Fig 9: India Overall WTR Score — Actual & Forecast (2026–2030)\n'
             f'Linear model: ŷ = {slope:.4f}x + ({intercept:.2f}),  r = {r:.3f}',
             fontweight='bold', pad=12)
ax.set_xlabel('Year', labelpad=8)
ax.set_ylabel('Overall Score', labelpad=8)
ax.legend(fontsize=9)
ax.grid(alpha=0.25)

plt.tight_layout()
plt.savefig('analysis/charts/fig9_forecast.png')
plt.show()
print('Fig 9 saved -> analysis/charts/fig9_forecast.png')
for yr, val in zip(forecast_years, forecast_vals):
    print(f'   {yr}: {val:.2f}')