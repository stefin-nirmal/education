"""
Script to generate scripts/education_cleaning.ipynb and execute it.
"""
import nbformat as nbf
import os
import pandas as pd
import numpy as np

nb = nbf.v4.new_notebook()

cells = []

# Title & Overview
cells.append(nbf.v4.new_markdown_cell("""# EduVision_DV - Higher Education Performance Analytics
## Module 2: Data Cleaning & Transformation Notebook (`education_cleaning.ipynb`)
**Deliverables:** `university_cleaned.csv`, `education_cleaning.ipynb`  
**Objectives:**
1. Inspect schema, detect anomalies, check completeness
2. Remove any duplicate records
3. Standardize university names and country names
4. Normalize ranking indicators across QS and Times Higher Education (THE)
5. Ensure missing values are strictly below 2% (Evaluation requirement)
"""))

# Cell 1: Imports
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import os

print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
"""))

# Cell 2: Load raw data
cells.append(nbf.v4.new_code_cell("""raw_data_path = '../data/university_raw_data.csv'
if not os.path.exists(raw_data_path):
    raw_data_path = 'data/university_raw_data.csv'

df_raw = pd.read_csv(raw_data_path)
print(f"Loaded Raw Dataset: {df_raw.shape[0]:,} rows, {df_raw.shape[1]} columns")
df_raw.head()
"""))

# Cell 3: Data Integrity and Duplicate Inspection
cells.append(nbf.v4.new_code_cell("""# Check for duplicate entries
initial_count = len(df_raw)
duplicates = df_raw.duplicated(subset=['university_name', 'year', 'subject_area']).sum()
print(f"Number of duplicate records found: {duplicates}")

df_cleaned = df_raw.drop_duplicates(subset=['university_name', 'year', 'subject_area']).copy()
print(f"Records after deduplication: {len(df_cleaned):,}")
"""))

# Cell 4: Standardization of Names and Countries
cells.append(nbf.v4.new_code_cell("""# Standardize text fields
df_cleaned['university_name'] = df_cleaned['university_name'].astype(str).str.strip()
df_cleaned['country'] = df_cleaned['country'].astype(str).str.strip()
df_cleaned['region'] = df_cleaned['region'].astype(str).str.strip()
df_cleaned['subject_area'] = df_cleaned['subject_area'].astype(str).str.strip()

# Country Name Standardizations mapping
country_std_map = {
    'USA': 'United States',
    'US': 'United States',
    'UK': 'United Kingdom',
    'U.K.': 'United Kingdom',
    'Korea': 'South Korea',
    'Republic of Korea': 'South Korea',
    'Russian Federation': 'Russia'
}
df_cleaned['country'] = df_cleaned['country'].replace(country_std_map)

print("Unique Regions:", df_cleaned['region'].unique())
print("Top 10 Countries by Count:\\n", df_cleaned['country'].value_counts().head(10))
"""))

# Cell 5: Missing Values Assessment
cells.append(nbf.v4.new_code_cell("""# Missing value assessment
missing_counts = df_cleaned.isnull().sum()
total_cells = df_cleaned.size
missing_cells = missing_counts.sum()
missing_pct = (missing_cells / total_cells) * 100

print("Missing values per column:\\n", missing_counts)
print(f"\\nOverall Missing Data Percentage: {missing_pct:.4f}%")
assert missing_pct < 2.0, "Missing data threshold exceeded (>2%)!"
"""))

# Cell 6: Metric Normalization and Harmonization
cells.append(nbf.v4.new_code_cell("""# Metric Normalization
# Harmonize QS and THE overall scores
# Harmonized score = 0.5 * QS + 0.5 * THE
df_cleaned['overall_score_harmonized'] = (
    0.5 * df_cleaned['overall_score_qs'] + 0.5 * df_cleaned['overall_score_the']
).round(2)

# Global unified rank based on harmonized score
df_cleaned['global_rank'] = df_cleaned.groupby('year')['overall_score_harmonized'].rank(
    ascending=False, method='min'
).astype(int)

# Validate Score ranges (0 - 100)
score_cols = [
    'overall_score_qs', 'overall_score_the', 'overall_score_harmonized',
    'academic_reputation_score', 'employer_reputation_score',
    'citations_per_faculty_score', 'industry_income_score'
]

for col in score_cols:
    df_cleaned[col] = df_cleaned[col].clip(lower=0.0, upper=100.0).round(2)

print("Score range validation completed successfully.")
"""))

# Cell 7: Export Cleaned Dataset
cells.append(nbf.v4.new_code_cell("""output_clean_path = '../data/university_cleaned.csv'
if not os.path.exists(os.path.dirname(output_clean_path)):
    output_clean_path = 'data/university_cleaned.csv'

df_cleaned.to_csv(output_clean_path, index=False)
print(f"Successfully exported cleaned dataset to: {output_clean_path}")
print(f"Shape: {df_cleaned.shape}")
"""))

nb.cells = cells

# Save notebook
notebook_path = "c:/Users/stefi/Desktop/education/scripts/education_cleaning.ipynb"
with open(notebook_path, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Wrote {notebook_path}")
