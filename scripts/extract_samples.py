#!/usr/bin/env python3
import json
import os
import random
import shutil

# Create analysis samples directory if it doesn't exist
os.makedirs('data/analysis_samples', exist_ok=True)
os.makedirs('data/analysis_samples/primock57', exist_ok=True)
os.makedirs('data/analysis_samples/va', exist_ok=True)

# Sample size for each dataset
SAMPLE_SIZE = 5

def extract_primock57_samples():
    """Extract random samples from the primock57 dataset"""
    
    source_dir = 'data/original_transcripts/primock57/primock57_md_notes'
    target_dir = 'data/analysis_samples/primock57'
    
    # Get all JSON files
    json_files = [f for f in os.listdir(source_dir) if f.endswith('.json')]
    
    # Select random samples
    selected_samples = random.sample(json_files, min(SAMPLE_SIZE, len(json_files)))
    
    # Copy selected files to the analysis samples directory
    for sample_file in selected_samples:
        source_path = os.path.join(source_dir, sample_file)
        target_path = os.path.join(target_dir, sample_file)
        
        # Read and save the file to track what we've sampled
        with open(source_path, 'r') as source_f:
            data = json.load(source_f)
            with open(target_path, 'w') as target_f:
                json.dump(data, target_f, indent=2)
    
    print(f"Extracted {len(selected_samples)} samples from primock57 dataset")
    return selected_samples

def extract_va_samples():
    """Extract random samples from the VA dataset"""
    
    source_dir = 'data/original_transcripts/va/va_transcripts/Transcripts'
    target_dir = 'data/analysis_samples/va'
    
    # Get all text files
    txt_files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]
    
    # Select random samples
    selected_samples = random.sample(txt_files, min(SAMPLE_SIZE, len(txt_files)))
    
    # Copy selected files to the analysis samples directory
    for sample_file in selected_samples:
        source_path = os.path.join(source_dir, sample_file)
        target_path = os.path.join(target_dir, sample_file)
        shutil.copy2(source_path, target_path)
    
    print(f"Extracted {len(selected_samples)} samples from VA dataset")
    return selected_samples

if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(42)
    
    # Extract samples
    primock57_samples = extract_primock57_samples()
    va_samples = extract_va_samples()
    
    # Save the list of extracted samples for reference
    with open('data/analysis_samples/sample_list.json', 'w') as f:
        json.dump({
            'primock57': primock57_samples,
            'va': va_samples
        }, f, indent=2)
    
    print("Sample extraction complete.")
