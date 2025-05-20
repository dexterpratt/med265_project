#!/usr/bin/env python3
"""
Script to analyze merged PriMock57 transcripts and compare them with doctor's notes.
This script:
1. Processes the merged transcripts from merge_primock_transcripts.py
2. Analyzes conversation patterns similar to VA transcript analysis
3. Compares transcript content with doctor's notes
4. Updates the summary.md with additional insights
"""

import os
import re
import json
import subprocess
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter, defaultdict
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Ensure NLTK resources are available
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Constants
INPUT_DIR = 'data/analysis_samples/primock57_combined'
PLOTS_DIR = 'data/analysis_samples/plots'
SUMMARY_FILE = 'data/summary.md'

# Create plots directory if it doesn't exist
os.makedirs(PLOTS_DIR, exist_ok=True)

class PrimockComparisonAnalyzer:
    """Analyzer for comparing PriMock57 transcripts and doctor's notes"""
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        # Medical terminology list
        self.medical_terms = set([
            'pain', 'symptom', 'diagnosis', 'treatment', 'medication', 'blood', 
            'pressure', 'test', 'doctor', 'patient', 'hospital', 'prescription',
            'fever', 'chronic', 'acute', 'allergy', 'dose', 'therapy', 'cough',
            'headache', 'nausea', 'fatigue', 'rash', 'inflammation', 'infection',
            'diabetes', 'hypertension', 'asthma', 'arthritis', 'cancer', 'heart',
            'lungs', 'kidney', 'liver', 'surgery', 'procedure', 'specialist',
            'referral', 'emergency', 'follow-up', 'history', 'examination',
            'chest', 'abdomen', 'throat', 'ear', 'eye', 'skin', 'joint', 'muscle'
        ])
    
    def run_merge_script(self):
        """Run the script to merge PriMock57 transcripts if needed"""
        if not os.path.exists(INPUT_DIR) or not os.listdir(INPUT_DIR):
            print("Merging PriMock57 transcripts...")
            subprocess.run(['python', 'scripts/merge_primock_transcripts.py'], check=True)
            print("Transcript merging completed.")
        else:
            print("Using existing merged transcripts.")
    
    def load_processed_samples(self):
        """Load the list of processed samples"""
        sample_file = os.path.join(INPUT_DIR, 'processed_samples.json')
        if not os.path.exists(sample_file):
            print("No processed samples found. Run merge_primock_transcripts.py first.")
            return None
        
        with open(sample_file, 'r') as f:
            return json.load(f)
    
    def analyze_transcript(self, transcript_path):
        """Analyze a merged transcript"""
        with open(transcript_path, 'r') as f:
            transcript = f.read()
        
        # Extract all turns
        turns = re.findall(r'(DOCTOR|PATIENT) .*?\n(.*?)\n\n', transcript, re.DOTALL)
        
        doctor_turns = [turn[1] for turn in turns if turn[0] == 'DOCTOR']
        patient_turns = [turn[1] for turn in turns if turn[0] == 'PATIENT']
        
        # Analyze turn counts and lengths
        turn_counts = {
            'doctor_turns': len(doctor_turns),
            'patient_turns': len(patient_turns),
            'total_turns': len(turns)
        }
        
        # Calculate turn lengths in words
        doctor_lengths = [len(word_tokenize(turn)) for turn in doctor_turns]
        patient_lengths = [len(word_tokenize(turn)) for turn in patient_turns]
        
        turn_lengths = {
            'avg_doctor_length': np.mean(doctor_lengths) if doctor_lengths else 0,
            'avg_patient_length': np.mean(patient_lengths) if patient_lengths else 0,
            'doctor_lengths': doctor_lengths,
            'patient_lengths': patient_lengths
        }
        
        # Question analysis
        doctor_questions = sum(turn.count('?') for turn in doctor_turns)
        patient_questions = sum(turn.count('?') for turn in patient_turns)
        
        questions = {
            'doctor_questions': doctor_questions,
            'patient_questions': patient_questions,
            'total_questions': doctor_questions + patient_questions
        }
        
        # Extract medical terms
        all_text = ' '.join(doctor_turns + patient_turns).lower()
        tokens = word_tokenize(all_text)
        medical_terms = [word for word in tokens if word in self.medical_terms]
        med_term_counts = Counter(medical_terms)
        
        # Return combined analysis
        return {
            'turn_counts': turn_counts,
            'turn_lengths': turn_lengths,
            'questions': questions,
            'medical_terms': dict(med_term_counts),
            'word_count': len(tokens)
        }
    
    def compare_transcript_with_note(self, transcript_path, doctor_note):
        """Compare transcript content with doctor's note"""
        with open(transcript_path, 'r') as f:
            transcript = f.read()
        
        # Extract all text from transcript
        # Extract all turns and get just the text (second group in each match)
        matches = re.findall(r'(DOCTOR|PATIENT) .*?\n(.*?)\n\n', transcript, re.DOTALL)
        turn_texts = [turn[1] for turn in matches]  # Extract just the text content
        transcript_text = ' '.join(turn_texts)
        transcript_tokens = word_tokenize(transcript_text.lower())
        
        # Extract text from doctor's note
        note_text = doctor_note.get('note', '')
        note_tokens = word_tokenize(note_text.lower())
        
        # Compare lengths
        transcript_length = len(transcript_tokens)
        note_length = len(note_tokens)
        compression_ratio = note_length / transcript_length if transcript_length > 0 else 0
        
        # Compare medical terms
        transcript_med_terms = [word for word in transcript_tokens if word in self.medical_terms]
        note_med_terms = [word for word in note_tokens if word in self.medical_terms]
        
        transcript_med_counts = Counter(transcript_med_terms)
        note_med_counts = Counter(note_med_terms)
        
        # Compare terms preserved in notes
        preserved_terms = set(transcript_med_counts.keys()) & set(note_med_counts.keys())
        unique_to_transcript = set(transcript_med_counts.keys()) - set(note_med_counts.keys())
        unique_to_note = set(note_med_counts.keys()) - set(transcript_med_counts.keys())
        
        # Check if highlights are mentioned in transcript
        highlights = doctor_note.get('highlights', [])
        highlight_mentions = {}
        
        for highlight in highlights:
            # Simplified check - just see if words from highlight appear in transcript
            highlight_tokens = word_tokenize(highlight.lower())
            non_stop_words = [word for word in highlight_tokens if word not in self.stop_words]
            
            # Count how many highlight terms are in the transcript
            found_count = sum(1 for word in non_stop_words if word in transcript_tokens)
            highlight_mentions[highlight] = found_count / len(non_stop_words) if non_stop_words else 0
        
        return {
            'transcript_length': transcript_length,
            'note_length': note_length,
            'compression_ratio': compression_ratio,
            'preserved_terms': list(preserved_terms),
            'unique_to_transcript': list(unique_to_transcript),
            'unique_to_note': list(unique_to_note),
            'highlight_mentions': highlight_mentions
        }
    
    def generate_comparison_plots(self, all_results):
        """Generate plots comparing transcripts and notes"""
        # Prepare data for plots
        consultation_ids = [result['consultation_id'] for result in all_results]
        transcript_lengths = [result['comparison']['transcript_length'] for result in all_results]
        note_lengths = [result['comparison']['note_length'] for result in all_results]
        compression_ratios = [result['comparison']['compression_ratio'] for result in all_results]
        
        # Plot 1: Transcript vs Note Length
        plt.figure(figsize=(10, 6))
        x = np.arange(len(consultation_ids))
        width = 0.35
        
        plt.bar(x - width/2, transcript_lengths, width, label='Transcript Word Count')
        plt.bar(x + width/2, note_lengths, width, label='Note Word Count')
        
        plt.ylabel('Word Count')
        plt.title('Transcript vs. Doctor\'s Note Length')
        plt.xticks(x, consultation_ids, rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        
        plt.savefig(os.path.join(PLOTS_DIR, 'transcript_vs_note_length.png'))
        plt.close()
        
        # Plot 2: Compression Ratio
        plt.figure(figsize=(10, 6))
        plt.bar(consultation_ids, compression_ratios, color='skyblue')
        plt.ylabel('Compression Ratio (Note/Transcript)')
        plt.title('Compression Ratio: Doctor\'s Note to Transcript')
        plt.xticks(rotation=45, ha='right')
        plt.axhline(y=np.mean(compression_ratios), color='r', linestyle='-', label='Mean Ratio')
        plt.legend()
        plt.tight_layout()
        
        plt.savefig(os.path.join(PLOTS_DIR, 'note_compression_ratio.png'))
        plt.close()
        
        # Plot 3: Medical Terms Preservation
        preserved_counts = [len(result['comparison']['preserved_terms']) for result in all_results]
        unique_transcript_counts = [len(result['comparison']['unique_to_transcript']) for result in all_results]
        unique_note_counts = [len(result['comparison']['unique_to_note']) for result in all_results]
        
        plt.figure(figsize=(10, 6))
        bottom = np.zeros(len(consultation_ids))
        
        p1 = plt.bar(consultation_ids, preserved_counts, label='Preserved Terms')
        bottom = np.array(preserved_counts)
        p2 = plt.bar(consultation_ids, unique_transcript_counts, bottom=bottom, label='Unique to Transcript')
        bottom = bottom + np.array(unique_transcript_counts)
        p3 = plt.bar(consultation_ids, unique_note_counts, bottom=bottom, label='Unique to Note')
        
        plt.ylabel('Number of Medical Terms')
        plt.title('Medical Term Distribution in Transcripts vs. Notes')
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        
        plt.savefig(os.path.join(PLOTS_DIR, 'medical_term_preservation.png'))
        plt.close()
    
    def update_summary(self, all_results):
        """Update the summary markdown file with comparison insights"""
        # Calculate aggregate statistics
        avg_compression = np.mean([r['comparison']['compression_ratio'] for r in all_results])
        avg_preserved_terms = np.mean([len(r['comparison']['preserved_terms']) for r in all_results])
        avg_unique_transcript = np.mean([len(r['comparison']['unique_to_transcript']) for r in all_results])
        avg_unique_note = np.mean([len(r['comparison']['unique_to_note']) for r in all_results])
        
        # Calculate highlight coverage
        all_highlights = [item 
                         for result in all_results 
                         for item in result['comparison']['highlight_mentions'].items()]
        highlight_coverage = sum(score for _, score in all_highlights) / len(all_highlights) if all_highlights else 0
        
        # Read current summary
        with open(SUMMARY_FILE, 'r') as f:
            current_summary = f.read()
        
        # Prepare new content
        new_content = "\n## PriMock57 Transcript vs. Note Comparison\n\n"
        
        # Overview section
        new_content += "### Overview of Transcript-Note Comparison\n\n"
        new_content += f"Analysis of {len(all_results)} paired transcripts and doctor's notes from the PriMock57 dataset shows:\n\n"
        new_content += f"- Doctor's notes contain approximately {avg_compression:.2%} of the words in the full transcript\n"
        new_content += f"- On average, {avg_preserved_terms:.1f} medical terms from the consultation are preserved in notes\n"
        new_content += f"- {avg_unique_transcript:.1f} medical terms mentioned in conversation don't appear in notes\n" 
        new_content += f"- {avg_unique_note:.1f} medical terms in notes weren't explicitly mentioned in conversation\n"
        new_content += f"- Key highlights in doctor's notes had {highlight_coverage:.2%} coverage in the transcripts\n\n"
        
        # Detailed findings
        new_content += "### Key Differences Between Transcripts and Notes\n\n"
        
        new_content += "1. **Information Density**:\n"
        new_content += "   - Transcripts contain patient narratives with repetition and conversational elements\n"
        new_content += "   - Doctor's notes extract and compress key medical information\n"
        new_content += "   - Notes organize information into standard clinical categories\n\n"
        
        new_content += "2. **Medical Terminology**:\n"
        new_content += "   - Doctors use everyday language with patients during consultations\n"
        new_content += "   - Notes translate patient descriptions into formal medical terms\n"
        new_content += "   - Some medical concepts in notes are inferred rather than explicitly discussed\n\n"
        
        new_content += "3. **Structure and Format**:\n"
        new_content += "   - Consultations follow a conversational flow with back-and-forth exchanges\n"
        new_content += "   - Notes follow standardized formats: presenting complaint, history, examination, assessment, plan\n"
        new_content += "   - Information from different parts of the conversation is reorganized in the notes\n\n"
        
        # Implications for ambient AI
        new_content += "### Implications for Ambient AI\n\n"
        
        new_content += "1. **Information Extraction**:\n"
        new_content += "   - AI systems need to identify clinically relevant information within casual conversation\n"
        new_content += "   - Contextual understanding is crucial for interpreting patient narratives\n\n"
        
        new_content += "2. **Translation of Terms**:\n"
        new_content += "   - AI should translate patient descriptions into appropriate medical terminology\n"
        new_content += "   - Systems need knowledge of equivalencies between everyday and clinical language\n\n"
        
        new_content += "3. **Inferred Knowledge**:\n"
        new_content += "   - Doctors sometimes document conclusions not explicitly stated in conversation\n"
        new_content += "   - AI systems would need similar reasoning capabilities to infer appropriate conclusions\n\n"
        
        new_content += "4. **Note Organization**:\n"
        new_content += "   - Information in conversation doesn't appear in chronological order in notes\n"
        new_content += "   - AI would need to reorganize content into clinical documentation format\n\n"
        
        # Insert before the conclusion but after the Enhanced Analysis section
        enhanced_section_pos = current_summary.find("## Enhanced Analysis")
        conclusion_pos = current_summary.find("## Conclusion")
        
        if enhanced_section_pos != -1 and conclusion_pos != -1:
            # If both Enhanced Analysis and Conclusion sections exist, insert after Enhanced Analysis
            insert_pos = conclusion_pos
            updated_summary = current_summary[:insert_pos] + new_content + current_summary[insert_pos:]
        elif conclusion_pos != -1:
            # If only Conclusion exists, insert before it
            updated_summary = current_summary[:conclusion_pos] + new_content + current_summary[conclusion_pos:]
        else:
            # If neither exists, append to the end
            updated_summary = current_summary + new_content
        
        # Write updated summary
        with open(SUMMARY_FILE, 'w') as f:
            f.write(updated_summary)
        
        print(f"Updated summary file with transcript-note comparison insights.")
    
    def run(self):
        """Run the full comparison analysis"""
        # Step 1: Ensure merged transcripts exist
        self.run_merge_script()
        
        # Step 2: Load processed samples
        processed_samples = self.load_processed_samples()
        if not processed_samples:
            return
        
        print(f"Analyzing {processed_samples['sample_count']} merged transcripts...")
        
        # Step 3: Analyze each consultation
        all_results = []
        
        for consultation_id in processed_samples['consultations']:
            transcript_path = os.path.join(INPUT_DIR, f"{consultation_id}_merged.txt")
            
            # Get doctor's note
            note_file = os.path.join('data/original_transcripts/primock57/primock57_md_notes', f"{consultation_id}.json")
            try:
                with open(note_file, 'r') as f:
                    doctor_note = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print(f"Warning: Could not load doctor's note for {consultation_id}")
                doctor_note = {}
            
            # Analyze transcript
            transcript_analysis = self.analyze_transcript(transcript_path)
            
            # Compare with note
            comparison = self.compare_transcript_with_note(transcript_path, doctor_note)
            
            all_results.append({
                'consultation_id': consultation_id,
                'transcript_analysis': transcript_analysis,
                'doctor_note': doctor_note,
                'comparison': comparison
            })
        
        # Step 4: Generate comparison plots
        self.generate_comparison_plots(all_results)
        
        # Step 5: Update summary
        self.update_summary(all_results)
        
        print("PriMock57 transcript and note comparison analysis complete.")


if __name__ == "__main__":
    analyzer = PrimockComparisonAnalyzer()
    analyzer.run()
