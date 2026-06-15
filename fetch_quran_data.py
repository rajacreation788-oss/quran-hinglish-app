import kagglehub
import pandas as pd
import json
import os

# Download latest version
print("Downloading Quran dataset from Kaggle...")
path = kagglehub.dataset_download("imrankhan197/the-quran-dataset")
print("Path to dataset files:", path)

# List all files in the dataset
print("\nFiles in dataset:")
for file in os.listdir(path):
    print(f"  - {file}")

# Load and process the data
try:
    # Try to find the main Quran CSV file
    csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
    print(f"\nFound CSV files: {csv_files}")
    
    if csv_files:
        # Load the first CSV (usually contains main Quran data)
        df = pd.read_csv(os.path.join(path, csv_files[0]))
        print(f"\nDataset shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        print(f"\nFirst few rows:")
        print(df.head())
        
        # Convert to our format
        quran_data = []
        
        # Group by Surah
        for surah_num, surah_group in df.groupby('Surah'):
            surah_name = surah_group.iloc[0].get('Surah_Name', f'Surah {surah_num}')
            
            ayats = []
            for _, row in surah_group.iterrows():
                ayat_entry = {
                    'id': int(row.get('Ayah', row.get('Verse', 1))),
                    'h': row.get('Text_English', row.get('English_Translation', '')),  # Hinglish/English
                    'a': row.get('Text_Arabic', row.get('Arabic', ''))  # Arabic
                }
                ayats.append(ayat_entry)
            
            surah_entry = {
                'surahName': surah_name,
                'surahNumber': int(surah_num),
                'ayats': ayats
            }
            quran_data.append(surah_entry)
        
        # Save to JSON
        output_file = 'quran_data.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(quran_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Successfully created {output_file}")
        print(f"Total Surahs: {len(quran_data)}")
        print(f"Sample: {json.dumps(quran_data[0], ensure_ascii=False, indent=2)[:500]}...")
        
except Exception as e:
    print(f"Error processing dataset: {e}")
    print("Please check the CSV file structure and column names")
