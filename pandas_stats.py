
import sys
import pandas as pd

DATA_PATH = '2024_fb_ads_president_scored_anon.csv'
GROUP_KEYS = ['Page Id', 'Ad Id']

if len(sys.argv) > 1:
    DATA_PATH = sys.argv[1]
if len(sys.argv) > 2:
    GROUP_KEYS = sys.argv[2:]

print(f"\nUSING FILE: {DATA_PATH}")
print(f"GROUPING BY: {GROUP_KEYS}")

df = pd.read_csv(DATA_PATH)

print("\n=== Overall Describe ===")
print(df.describe(include='all'))

print("\n=== Categorical Columns ===")
for col in df.select_dtypes(include='object').columns:
    print(f"\n{col}:")
    print("Unique:", df[col].nunique())
    print("Most Common:", df[col].value_counts().head(1))

print("\n=== Grouped Describe ===")
if all(k in df.columns for k in GROUP_KEYS):
    grouped = df.groupby(GROUP_KEYS).describe()
    print(grouped)
else:
    print(f"WARNING: Not all group keys found in columns! Columns = {list(df.columns)}")





