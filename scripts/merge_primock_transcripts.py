#!/usr/bin/env python3
"""
Script to merge PriMock57 doctor and patient TextGrid files into combined transcripts.
This script:
1. Selects sample consultation pairs (doctor and patient files)
2. Merges them into chronological transcripts similar to VA format
3. Saves the combined transcripts for analysis
4. Creates a comparison with doctor's notes for the same consultations
"""

import os
import re
import json
import random
import shutil
from collections import namedtuple

# Constants
SAMPLE_SIZE = 3  # Number of consultations to sample
PRIMOCK_DIR = 'data/original_transcripts/primock57'
TRANSCRIPT_DIR = os.path.join(PRIMOCK_DIR, 'primock57_transcripts')
NOTES_DIR = os.path.join(PRIMOCK_DIR, 'primock57_md_notes')
OUTPUT_DIR = 'data/analysis_samples/primock57_combined'

# Create output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define a structure to hold an utterance
Utterance = namedtuple('Utterance', ['speaker', 'start_time', 'end_time', 'text'])

def parse_textgrid(file_path, speaker_type):
    """
    Parse a TextGrid file and extract utterances
    
    Args:
        file_path: Path to the TextGrid file
        speaker_type: 'doctor' or 'patient'
        
    Returns:
        List of Utterance objects
    """
    utterances = []
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all intervals in the TextGrid file
    intervals_pattern = r'intervals \[(\d+)\]:\s+xmin = ([\d.]+)\s+xmax = ([\d.]+)\s+text = "(.*?)"'
    matches = re.findall(intervals_pattern, content, re.DOTALL)
    
    for match in matches:
        _, start_time, end_time, text = match
        # Skip empty utterances
        if text.strip() and text.strip() != '""':
            # Clean up the text
            cleaned_text = text.strip().replace("<UNIN/>", "").replace("<UNIN>", "")
            cleaned_text = re.sub(r'<UNSURE>(.*?)</UNSURE>', r'\1', cleaned_text)
            
            if cleaned_text:
                utterances.append(Utterance(
                    speaker=speaker_type.upper(),
                    start_time=float(start_time),
                    end_time=float(end_time),
                    text=cleaned_text
                ))
    
    return utterances

def merge_transcripts(doctor_file, patient_file):
    """
    Merge doctor and patient TextGrid files into a single transcript
    
    Args:
        doctor_file: Path to doctor's TextGrid file
        patient_file: Path to patient's TextGrid file
        
    Returns:
        String containing the merged transcript
    """
    # Extract consultation ID from the filename
    match = re.search(r'(day\d+_consultation\d+)', doctor_file)
    consultation_id = match.group(1) if match else "unknown_consultation"
    
    # Parse both files
    doctor_utterances = parse_textgrid(doctor_file, 'doctor')
    patient_utterances = parse_textgrid(patient_file, 'patient')
    
    # Combine and sort by start time
    all_utterances = doctor_utterances + patient_utterances
    all_utterances.sort(key=lambda u: u.start_time)
    
    # Generate transcript in VA-like format
    transcript = f"Date of Encounter: Simulated Consultation (PriMock57)\n"
    transcript += f"Consultation ID: {consultation_id}\n\n"
    
    for utterance in all_utterances:
        # Skip empty or unintelligible utterances
        if not utterance.text or utterance.text == '""':
            continue
            
        transcript += f"{utterance.speaker} {consultation_id}\n"
        transcript += f"{utterance.text}\n\n"
    
    return transcript, consultation_id

def get_doctor_note(consultation_id):
    """
    Get the doctor's note for a specific consultation
    
    Args:
        consultation_id: ID of the consultation
        
    Returns:
        Dictionary containing the doctor's note data
    """
    note_file = os.path.join(NOTES_DIR, f"{consultation_id}.json")
    
    try:
        with open(note_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Warning: Could not load doctor's note for {consultation_id}")
        return None

def create_comparison_file(transcript, doctor_note, consultation_id):
    """
    Create a file comparing the transcript with the doctor's note
    
    Args:
        transcript: The merged transcript text
        doctor_note: The doctor's note data
        consultation_id: ID of the consultation
        
    Returns:
        String containing the comparison
    """
    if not doctor_note:
        return f"No doctor's note available for {consultation_id}"
    
    comparison = f"# Comparison: Transcript vs. Doctor's Note for {consultation_id}\n\n"
    
    # Add presenting complaint section
    comparison += "## Presenting Complaint\n\n"
    comparison += f"**Patient's words in transcript:**\n"
    
    # Extract the first few patient utterances to capture the presenting complaint
    patient_utterances = re.findall(r'PATIENT.*?\n(.*?)\n\n', transcript, re.DOTALL)
    first_utterances = "\n".join(patient_utterances[:3])
    comparison += f"{first_utterances}\n\n"
    
    comparison += f"**Doctor's note - Presenting Complaint:**\n"
    comparison += f"{doctor_note.get('presenting_complaint', 'Not recorded')}\n\n"
    
    # Add clinical note section
    comparison += "## Clinical Documentation\n\n"
    comparison += f"**Doctor's Full Note:**\n"
    comparison += f"{doctor_note.get('note', 'Not recorded')}\n\n"
    
    # Add highlights section
    comparison += "## Key Highlights\n\n"
    comparison += "**Doctor's Highlights:**\n"
    for highlight in doctor_note.get('highlights', []):
        comparison += f"- {highlight}\n"
    
    return comparison

def main():
    # Get all consultation pairs
    file_pattern = re.compile(r'(day\d+_consultation\d+)_(doctor|patient)\.TextGrid')
    consultation_files = {}
    
    for filename in os.listdir(TRANSCRIPT_DIR):
        if filename.endswith('.TextGrid'):
            match = file_pattern.match(filename)
            if match:
                consultation_id, speaker_type = match.groups()
                if consultation_id not in consultation_files:
                    consultation_files[consultation_id] = {}
                consultation_files[consultation_id][speaker_type] = os.path.join(TRANSCRIPT_DIR, filename)
    
    # Filter only consultations with both doctor and patient files
    complete_consultations = {
        cid: files for cid, files in consultation_files.items()
        if 'doctor' in files and 'patient' in files
    }
    
    # Select random samples
    if len(complete_consultations) > SAMPLE_SIZE:
        # Use a fixed seed for reproducibility
        random.seed(42)
        sample_ids = random.sample(list(complete_consultations.keys()), SAMPLE_SIZE)
        samples = {cid: complete_consultations[cid] for cid in sample_ids}
    else:
        samples = complete_consultations
    
    print(f"Selected {len(samples)} consultations for processing")
    
    # Process each sample
    results = []
    for consultation_id, files in samples.items():
        doctor_file = files['doctor']
        patient_file = files['patient']
        
        print(f"Merging {consultation_id}...")
        transcript, cid = merge_transcripts(doctor_file, patient_file)
        
        # Save merged transcript
        transcript_path = os.path.join(OUTPUT_DIR, f"{consultation_id}_merged.txt")
        with open(transcript_path, 'w') as f:
            f.write(transcript)
        
        # Get doctor's note and create comparison
        doctor_note = get_doctor_note(consultation_id)
        comparison = create_comparison_file(transcript, doctor_note, consultation_id)
        
        # Save comparison
        comparison_path = os.path.join(OUTPUT_DIR, f"{consultation_id}_comparison.md")
        with open(comparison_path, 'w') as f:
            f.write(comparison)
        
        results.append({
            'consultation_id': consultation_id,
            'transcript_path': transcript_path,
            'comparison_path': comparison_path,
            'doctor_note': doctor_note
        })
    
    # Save list of processed samples
    with open(os.path.join(OUTPUT_DIR, 'processed_samples.json'), 'w') as f:
        json.dump({
            'sample_count': len(results),
            'consultations': [r['consultation_id'] for r in results]
        }, f, indent=2)
    
    print(f"Successfully processed {len(results)} consultations.")
    print(f"Merged transcripts and comparisons saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
