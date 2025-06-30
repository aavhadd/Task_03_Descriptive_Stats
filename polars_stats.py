import sys
import polars as pl

DATA_PATH = '2024_fb_ads_president_scored_anon.csv'
GROUP_KEYS = ['Page Id', 'Ad Id']

if len(sys.argv) > 1:
    DATA_PATH = sys.argv[1]
if len(sys.argv) > 2:
    GROUP_KEYS = sys.argv[2:]

print(f"\nUSING FILE: {DATA_PATH}")
print(f"GROUPING BY: {GROUP_KEYS}")

df = pl.read_csv(DATA_PATH)

print("\n=== Overall Describe ===")
print(df.describe())

for col in df.columns:
    if df[col].dtype == pl.Utf8:
        print(f"\n{col} Unique: {df[col].n_unique()}")
        vc = df[col].value_counts().sort('count', descending=True)
        print(vc.head(1))

if all(k in df.columns for k in GROUP_KEYS):
    print("\n=== Grouped Stats ===")

    numeric_cols = [col for col in df.columns if df[col].dtype.is_numeric()]

    agg_exprs = []
    for col in numeric_cols:
        agg_exprs.extend([
            pl.col(col).mean().alias(f"{col}_mean"),
            pl.col(col).min().alias(f"{col}_min"),
            pl.col(col).max().alias(f"{col}_max"),
            pl.col(col).std().alias(f"{col}_std")
        ])

    grouped = df.group_by(GROUP_KEYS).agg(agg_exprs)
    print(grouped)

else:
    print(f"WARNING: Not all group keys found in columns! Columns = {list(df.columns)}")
