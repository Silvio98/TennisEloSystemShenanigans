"""Tennis Elo System Shenanigans."""
import os
os.environ['KAGGLEHUB_CACHE'] = r'C:\Users\silvi\Documents\TennisELO\TennisEloSystemShenanigans\Datasets'
import kagglehub
from kagglehub import KaggleDatasetAdapter

def download_Dataset():
    """Download the tennis dataset."""
    path = kagglehub.dataset_download("dissfya/atp-tennis-2000-2023daily-pull")
    return path


def main() -> None:
    print("Tennis Elo System is running.")
    print("Downloading Dataset.")
    download_Dataset()
    print("Dataset Downloaded.")

if __name__ == "__main__":
    main()