import pandas as pd
import numpy as np

# Load the reference spectra for noble gases
references = {
    'Argon Mercury': pd.read_csv('argon_mercury_reference.csv'),
    'Argon Pure': pd.read_csv('argon_pure_reference.csv'),
    'Helium': pd.read_csv('helium_reference.csv'),
    'Krypton': pd.read_csv('krypton_reference.csv'),
    'Xenon': pd.read_csv('xenon_reference.csv')
}

# Get the filename for the measured spectral data CSV from user input
measured_data_filename = input("Enter the filename for the measured spectral data CSV: ")

# Load the measured spectral data
try:
    measured_data = pd.read_csv(measured_data_filename)
except FileNotFoundError:
    print(f"Error: File '{measured_data_filename}' not found.")
    exit()

# Calculate the similarity scores between measured and reference spectra
similarity_scores = {}
for gas, reference in references.items():
    similarity = np.corrcoef(measured_data['Intensity'], reference['Intensity'])[0, 1]
    similarity_scores[gas] = similarity

# Set a threshold for identification (you can adjust this based on your data)
identification_threshold = 0.9

# Identify gas based on similarity score
identified_gas = max(similarity_scores, key=similarity_scores.get)
max_similarity = similarity_scores[identified_gas]

# Print the identified gas and its similarity score
print(f"Identified gas: {identified_gas} (Similarity: {max_similarity:.2f})")
