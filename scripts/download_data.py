
#!/usr/bin/env python3
"""Download the Retail Sales Dataset from Kaggle using kagglehub.

Usage:
    python scripts/download_data.py

The dataset is downloaded via kagglehub and copied into `data/raw/`
for use by the analysis notebooks.

Requires:
    pip install kagglehub
"""

import shutil
from pathlib import Path

import kagglehub


def main():
    # 1. Download the latest version of the dataset
    print("Downloading dataset...")
    path = kagglehub.dataset_download("mohammadtalib786/retail-sales-dataset")
    print(f"Downloaded to: {path}")

    # 2. Locate the CSV file inside the downloaded folder
    src = Path(path)
    csv_files = list(src.rglob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV file found in {path}")

    # 3. Copy it into the project's raw data folder
    raw_dir = Path(__file__).resolve().parents[1] / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    for csv in csv_files:
        dest = raw_dir / csv.name
        shutil.copy2(csv, dest)
        print(f"Saved: {dest}")

    print("Dataset ready for analysis in data/raw/")


if __name__ == "__main__":
    main()
