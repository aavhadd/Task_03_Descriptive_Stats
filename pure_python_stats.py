import sys
DATA_PATH = '2024_fb_ads_president_scored_anon.csv'
GROUP_KEYS = ['Page Id', 'Ad Id']

if len(sys.argv) > 1:
    DATA_PATH = sys.argv[1]
if len(sys.argv) > 2:
    GROUP_KEYS = sys.argv[2:]



import csv
import math
from collections import defaultdict, Counter

print(f"\nUSING FILE: {DATA_PATH}")
print(f"GROUPING BY: {GROUP_KEYS}")

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def load_data(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def identify_columns(rows):
    sample = rows[0]
    numeric_cols = [col for col in sample if any(
        kw in col.lower() for kw in ['count', 'likes', 'spend', 'impression', 'share', 'view', 'score', 'amount'])]
    categorical_cols = [col for col in sample if col not in numeric_cols]
    return numeric_cols, categorical_cols

def compute_stats(rows, numeric_cols, categorical_cols):
    result = {}

    # Numeric
    for col in numeric_cols:
        nums = [float(r[col]) for r in rows if is_float(r.get(col, ''))]
        if nums:
            mean = sum(nums) / len(nums)
            std = math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))
            result[col] = {
                'count': len(nums),
                'mean': mean,
                'min': min(nums),
                'max': max(nums),
                'std_dev': std
            }

    for col in categorical_cols:
        counter = Counter(r[col] for r in rows if r.get(col))
        result[col] = {
            'unique_count': len(counter),
            'most_common': counter.most_common(1)
        }

    return result

def groupby(rows, keys):
    grouped = defaultdict(list)
    for r in rows:
        key = tuple(r.get(k) for k in keys)
        grouped[key].append(r)
    return grouped

def main():
    rows = load_data(DATA_PATH)
    print(f"Loaded {len(rows)} rows.")

    numeric_cols, categorical_cols = identify_columns(rows)

    print("\n=== Overall ===")
    print(compute_stats(rows, numeric_cols, categorical_cols))

    print("\n=== Grouped ===")
    grouped = groupby(rows, GROUP_KEYS)
    for key, group in list(grouped.items())[:5]:  # limit output
        print(f"\nGroup: {key}")
        print(compute_stats(group, numeric_cols, categorical_cols))

if __name__ == '__main__':
    main()





