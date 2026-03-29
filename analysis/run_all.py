# run_all.py 
# Runs the full analysis pipeline in order
# Usage: python analysis/run_all.py

import subprocess
import sys

scripts = [
    'analysis/02_descriptive_stats.py',
    'analysis/03_global_rankings.py',
    'analysis/04_India_trends.py',
    'analysis/05_India_vs_global.py',
    'analysis/06_correlation.py',
    'analysis/07_regression.py',
    'analysis/08_top_bottom.py',
    'analysis/09_hypothesis_test.py',
    'analysis/10_forecast.py',
    'analysis/11_radar_chart.py',
    'analysis/12_heatmap_all.py',
]

print('Running full IMD WTR analysis pipeline...\n')
for script in scripts:
    print(f'▶ {script}')
    result = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f'  Done')
    else:
        print(f'  Error:\n{result.stderr}')
        break

print('\nAll charts saved to analysis/charts/')