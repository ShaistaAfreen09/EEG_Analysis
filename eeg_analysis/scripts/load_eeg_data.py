# load_eeg_data.py
import mne

def load_eeg_data(file_paths):
    raw_data = []
    for file_path in file_paths:
        raw = mne.io.read_raw_edf(file_path, preload=True)
        raw_data.append(raw)
    return raw_data
