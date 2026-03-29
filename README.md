# India in the Global Talent Race
### Statistical Analysis of the IMD World Talent Ranking (2015–2025)

This project grew out of a simple question: how does India actually perform in the global talent landscape, and what do the numbers really say beneath the surface-level rankings?

We took the IMD World Talent Ranking dataset, selected 25 countries and 15 indicators across 11 years, and rebuilt the entire scoring pipeline from scratch — standardisation, pillar aggregation, scaling — then ran proper statistical analysis on top of it. The goal was not just to report India's rank but to understand *why* it sits where it does and which factors matter most.

---

## What We Found

India ranked **15th out of 25** in 2025 with an overall score of 48.96, sitting just below the sample average of 49.94. Its best year was 2022, when it climbed to rank 8 with a score of 52.32 — a surge driven almost entirely by the Readiness pillar, which collapsed back down by 2024.

The most important statistical finding is that **Readiness is the dominant driver** of India's overall score (r = 0.856), while Investment & Development fluctuates the most (SD = 2.62) and Appeal consistently scores the lowest of the three pillars.

The indicator that stands out most starkly is female labour force participation — India's figure of 26.09% is nearly 18 percentage points below the 25-country average of 43.44%. That single gap is larger than any other indicator gap India has, and it drags down the Investment & Development pillar significantly.

The t-test confirmed that India's 2025 score is not statistically different from the world mean (T_calc = 0.705, T_crit = 2.069), which places India firmly in the middle tier — not an outlier in either direction. The linear forecast puts India at around 51.74 by 2030, assuming the current trend holds.

---

## Project Details

**Course:** AS1117 Probability and Statistics  
**Institution:** JK Lakshmipat University, Jaipur  
**Dataset:** 25 countries × 15 indicators × 11 years (2015–2025)  
**Errors corrected in raw data:** 35 (comma decimals, stray characters, whitespace in numbers)

---

## Repo Structure

```
India-s-Talent-Ranking-Analysis/
│
├── IMD_WTR_Dataset.xlsx       # Cleaned dataset — 18 tabs covering all pillars and indicators
├── IMD_WTR_Report.docx        # Full report with all tables, charts, and statistical workings
├── README.md
│
└── analysis/
    ├── setup.py               # Shared imports, matplotlib style, colour palette, constants
    ├── data_load.py           # Loads all Excel sheets and builds the core dataframes
    ├── 02_descriptive_stats.py
    ├── 03_global_rankings.py
    ├── 04_India_trends.py
    ├── 05_India_vs_global.py
    ├── 06_correlation.py
    ├── 07_regression.py
    ├── 08_top_bottom.py
    ├── 09_hypothesis_test.py
    ├── 10_forecast.py
    ├── 11_radar_chart.py      # Bonus — radar chart comparing India, Switzerland, sample avg
    ├── 12_heatmap_all.py      # Bonus — full 25-country × 11-year heatmap
    ├── run_all.py             # Runs the entire pipeline in one go
    └── charts/                # Auto-generated on first run, gitignored
```

---

## How to Run

Clone the repo and install dependencies:

```bash
git clone https://github.com/Ankit8804Sharma/India-s-Talent-Ranking-Analysis.git
cd India-s-Talent-Ranking-Analysis
pip install pandas numpy matplotlib seaborn scipy openpyxl
```

Run the full pipeline:

```bash
python analysis/run_all.py
```

All 11 charts will be saved to `analysis/charts/`. You can also run any individual script on its own — for example `python analysis/06_correlation.py` — since each one is self-contained.

---

## Charts Generated

| Script | Output | What it shows |
|--------|--------|---------------|
| 03_global_rankings.py | fig1 | All 25 countries ranked by 2025 score, India in orange |
| 04_India_trends.py | fig2 | India's 4 pillar scores from 2015 to 2025, 2022 peak marked |
| 02_descriptive_stats.py | fig3 | Descriptive stats table — mean, SD, skewness, kurtosis per pillar |
| 05_India_vs_global.py | fig4 | India vs sample average year by year, gap filled green/red |
| 06_correlation.py | fig5 | Correlation heatmap + bar chart showing Readiness dominates |
| 07_regression.py | fig6 | Regression scatter for each pillar with equation and r² |
| 08_top_bottom.py | fig7 | Switzerland #1 at 64.47, Venezuela last at 35.21 |
| 09_hypothesis_test.py | fig8 | t-distribution with T_calc = 0.705 inside acceptance region |
| 10_forecast.py | fig9 | Linear forecast to 2030 (51.74) with ±1SD confidence band |
| 11_radar_chart.py | fig10 | Radar chart — India trails Switzerland on all three pillars |
| 12_heatmap_all.py | fig11 | Full heatmap, India row highlighted, Nordic dominance visible |

---

## Statistical Methods

The analysis follows a clear pipeline. Raw indicator data was z-score standardised per indicator per year across all 25 countries, then averaged within each of the three IMD pillars (Investment & Development, Appeal, Readiness), scaled to 0–100, and averaged again to produce the overall score.

On top of that reconstructed index, we applied:

- Descriptive statistics (mean, median, standard deviation, variance, skewness, kurtosis)
- Pearson correlation to measure how strongly each pillar drives the overall score
- Simple linear regression for each pillar with R² and slope comparison
- Two-tailed t-test to check whether India's 2025 score is significantly different from the world mean (α = 0.05, df = 23)
- Linear extrapolation to forecast India's score through 2030

---

## Key Numbers at a Glance

| Metric | Value |
|--------|-------|
| India rank 2025 | 15 / 25 |
| India score 2025 | 48.96 |
| Sample average 2025 | 49.94 |
| India's best year | 2022 (score 52.32, rank 8) |
| Strongest pillar correlation | Readiness r = 0.856 |
| Largest indicator gap | Female labour force −17.35 pp |
| t-test result | Fail to reject H₀ (T_calc = 0.705) |
| Forecast 2030 | 51.74 |

---

## Data Source

IMD World Competitiveness Center — [World Talent Ranking](https://www.imd.org/centers/wcc/world-competitiveness-center/rankings/world-talent-ranking/)

Raw data was downloaded from the IMD portal. 35 errors were identified and corrected before any analysis was run.
