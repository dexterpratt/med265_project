#!/usr/bin/env python3
"""
Master script to run the complete medical consultation data analysis pipeline.
This script:
1. Extracts samples from both datasets
2. Merges PriMock57 transcripts into a format similar to VA transcripts
3. Analyzes both datasets individually 
4. Performs enhanced analysis of conversation patterns
5. Compares PriMock57 transcripts with doctor's notes
6. Generates a comprehensive summary and visualizations

All results are saved to data/summary.md and visualizations in data/analysis_samples/plots/
"""

import os
import subprocess
import sys
import time

def main():
    print("Starting comprehensive medical consultation data analysis pipeline...")
    
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Make all scripts executable
    scripts = [
        "extract_samples.py",
        "analyze_samples.py",
        "enhanced_analysis.py",
        "merge_primock_transcripts.py",
        "analyze_primock_comparison.py"
    ]
    
    for script in scripts:
        script_path = os.path.join(scripts_dir, script)
        if os.path.exists(script_path):
            os.chmod(script_path, 0o755)
    
    # Define execution order with descriptions
    execution_steps = [
        {
            "name": "Extract Samples", 
            "script": "extract_samples.py",
            "description": "Extracting random samples from both VA and PriMock57 datasets"
        },
        {
            "name": "Basic Analysis", 
            "script": "analyze_samples.py",
            "description": "Performing basic analysis of conversation dynamics"
        },
        {
            "name": "Enhanced Analysis", 
            "script": "enhanced_analysis.py",
            "description": "Conducting enhanced analysis of medical terminology and turn-taking patterns"
        },
        {
            "name": "Merge PriMock57 Transcripts", 
            "script": "merge_primock_transcripts.py",
            "description": "Merging PriMock57 doctor and patient files into complete transcripts"
        },
        {
            "name": "Analyze PriMock57 Transcript-Note Comparison", 
            "script": "analyze_primock_comparison.py",
            "description": "Comparing PriMock57 transcripts with doctor's notes"
        }
    ]
    
    # Run each script in sequence
    for step in execution_steps:
        script_path = os.path.join(scripts_dir, step["script"])
        
        if not os.path.exists(script_path):
            print(f"Warning: Script {step['script']} not found. Skipping this step.")
            continue
        
        print(f"\n=== {step['name']}: {step['description']} ===")
        
        try:
            # Note that we're running the scripts with the virtual environment's Python
            # if it exists, otherwise with the system Python
            if os.path.exists('env/bin/python'):
                python_exec = 'env/bin/python'
            else:
                python_exec = sys.executable
                
            subprocess.run([python_exec, script_path], check=True)
            print(f"{step['name']} completed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error in {step['name']}: {e}")
            choice = input("Continue with next step? (y/n): ")
            if choice.lower() != 'y':
                return 1
    
    print("\n=== Analysis pipeline completed successfully! ===")
    print("Results are available in:")
    print("- Summary report: data/summary.md")
    print("- Visualizations: data/analysis_samples/plots/")
    print("- Merged PriMock57 transcripts: data/analysis_samples/primock57_combined/")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
