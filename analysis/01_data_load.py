# 01_data_load.py
# Loads all sheets from the Excel dataset and builds core dataframes
# Import this in every analysis script to get clean, ready-to-use data

from analysis.setup_00 import *

def load_sheet(sheet_name, index_col=0):
    """Load a sheet, drop trailing None columns, set index."""
    df = pd.read_excel(EXCEL_FILE, sheet_name=sheet_name, index_col=index_col)
    df = df.loc[:, df.columns.notna()]
    return df

# Core score sheets 
df_overall  = load_sheet('Overall_Score')
df_inv      = load_sheet('Investment & Development')
df_app      = load_sheet('Appeal')
df_ready    = load_sheet('Readiness')
df_rank     = load_sheet('Ranking')
df_india    = load_sheet('India')

# 0-100 scaled pillar sheets (for radar chart)
df_inv100   = load_sheet('Investment_Development_0-100')
df_app100   = load_sheet('Appeal_0-100')
df_rdy100   = load_sheet('Readiness_0-100')

# India time series 
india_ts = df_india.T.copy()
india_ts.index = india_ts.index.astype(int)
india_ts.columns = ['Overall', 'Investment', 'Appeal', 'Readiness']

# Global average per year 
global_avg = df_overall[YEARS].mean(axis=0)

# 2025 snapshot (all 25 countries, sorted by rank) 
snap25 = pd.DataFrame({
    'Country' : df_overall.index,
    'Score'   : df_overall[2025].values,
    'Rank'    : df_rank[2025].values
}).sort_values('Rank').reset_index(drop=True)

if __name__ == '__main__':
    print(f'Data loaded — {len(df_overall)} countries, {YEARS[0]}–{YEARS[-1]}')
    print(f'   India 2025: Overall={india_ts.loc[2025,"Overall"]:.3f}, '
          f'Rank={int(snap25[snap25.Country=="India"].Rank.values[0])}')