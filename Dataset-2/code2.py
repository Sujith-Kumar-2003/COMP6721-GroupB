import zipfile
import os

# Define the path to the ZIP file and the extraction directory
zip_file_path = r'C:\Users\sujib\Downloads\Dataset-2.zip'
extraction_path = r'C:\Users\sujib\Downloads\Dataset-2'

# Create the extraction directory if it doesn't exist
os.makedirs(extraction_path, exist_ok=True)

# Unzip the file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

print("Unzipped files to:", extraction_path)

#%%
import os
import csv

# Define the dataset path
dataset_path = r"C:\Users\sujib\Downloads\Dataset-2\Food Classification"
output_csv = os.path.join(dataset_path, "image_labels.csv")

# Collect image paths and labels
entries = []
for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if os.path.isdir(folder_path):  # Only process directories
        label = folder  # The folder name is the label
        for image_file in os.listdir(folder_path):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(folder_path, image_file)
                entries.append([image_path, label])

# Write to CSV
with open(output_csv, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["image_path", "label"])  # Column headers
    writer.writerows(entries)

print(f"CSV file created with {len(entries)} entries at: {output_csv}")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/sujib/Downloads/Dataset-2/Food Classification/image_labels.csv")
print(df.head(15))

df.shape

df.columns

df['label'].unique()

df['label'].nunique()


import matplotlib.pyplot as plt
category_counts = df['label'].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title('Count of Each Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.show()
df.shape