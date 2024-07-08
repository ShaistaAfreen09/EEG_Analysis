# load_eeg_data.py
import mne
import pandas as pd

def load_eeg_data(file_paths):
    raw_data = []
    for file_path in file_paths:
        if file_path.endswith('.edf'):
            raw = mne.io.read_raw_edf(file_path, preload=True)
            raw_data.append(raw)
        elif file_path.endswith('.csv'):
            # Process your CSV file here, for example:
            df = pd.read_csv(file_path)
            # Further processing of CSV data if needed
            raw_data.append(df)
        else:
            print(f"Unsupported file type for {file_path}")

    return raw_data

if __name__ == "__main__":
    # Example usage
    file_paths = [
        r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject30_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject30_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject31_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject31_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject32_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject32_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject33_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject33_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject34_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject34_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject35_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject35_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject00_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject00_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject01_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject01_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject02_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject02_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject03_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject03_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject04_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject04_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject05_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject05_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject06_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject06_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject07_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject07_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject08_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject08_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject09_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject09_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject10_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject10_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject11_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject11_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject12_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject12_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject13_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject13_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject14_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject14_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject15_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject15_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject16_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject16_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject17_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject17_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject18_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject18_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject19_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject19_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject20_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject20_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject21_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject21_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject22_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject22_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject23_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject23_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject24_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject24_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject25_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject25_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject26_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject26_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject27_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject27_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject28_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject28_2.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject29_1.edf",
r"C:\Users\mohdm\OneDrive\Desktop\eeg_analysis\data\Subject29_2.edf"

    ]

    raw_data = load_eeg_data(file_paths)
    print(raw_data)
