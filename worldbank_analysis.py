import pandas as pd
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Load final dataset
df = pd.read_csv(project_folder / "Data" / "final_wdi_dashboard.csv")

# Keep only real countries
df = df[df["Region"].notna()]

# Save
output_path = project_folder / "Data" / "worldbank_dashboard_final.csv"
df.to_csv(output_path, index=False)

print("="*60)
print("FINAL ANALYSIS DATASET")
print(df.shape)

print(df.head())

print(f"\nSaved to:\n{output_path}")