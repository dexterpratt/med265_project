#!/usr/bin/env python3
"""
Runs the full analysis pipeline for medical consultation data.
This script:
1. Extracts samples from both datasets (primock57 and VA)
2. Analyzes the samples and generates visualizations
3. Creates a summary report in Markdown format
"""

import os
import subprocess
import sys
import time

def main():
    print("Starting medical consultation data analysis pipeline...")
    
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the scripts to run
    extract_script = os.path.join(scripts_dir, "extract_samples.py")
    analyze_script = os.path.join(scripts_dir, "analyze_samples.py")
    
    # Make the scripts executable
    os.chmod(extract_script, 0o755)
    os.chmod(analyze_script, 0o755)
    
    # Step 1: Extract samples from datasets
    print("\n=== Step 1: Extracting samples from datasets ===")
    try:
        subprocess.run([sys.executable, extract_script], check=True)
        print("Sample extraction completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting samples: {e}")
        return 1
    
    # Brief pause to ensure files are written
    time.sleep(1)
    
    # Step 2: Analyze samples and generate report
    print("\n=== Step 2: Analyzing samples and generating report ===")
    try:
        subprocess.run([sys.executable, analyze_script], check=True)
        print("Sample analysis completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error analyzing samples: {e}")
        return 1
    
    print("\n=== Analysis pipeline completed successfully! ===")
    print("Results are available in:")
    print("- Sample files: data/analysis_samples/")
    print("- Visualizations: data/analysis_samples/plots/")
    print("- Summary report: data/summary.md")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
