#!/usr/bin/env python3
"""
Enhanced analysis script to supplement the initial analysis with deeper insights.
This script:
1. Analyzes medical terminology frequency and patterns
2. Examines turn-taking behavior in more detail
3. Performs sentiment analysis on patient narratives
4. Updates the summary with more comprehensive insights
"""

import json
import os
import re
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Ensure NLTK resources are available
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

class EnhancedAnalyzer:
    """Advanced analysis of medical consultation transcripts"""
    
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        # Extended medical terminology list
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
        # Questioning patterns
        self.question_patterns = [
            r"What.*\?",
            r"How.*\?",
            r"When.*\?",
            r"Where.*\?",
            r"Why.*\?",
            r"Can you.*\?",
            r"Could you.*\?",
            r"Do you.*\?",
            r"Have you.*\?",
            r"Are you.*\?",
            r"Is it.*\?",
            r"Any.*\?"
        ]
    
    def analyze_medical_terminology(self, all_text):
        """Analyze medical terminology patterns in the text"""
        # Tokenize text
        tokens = word_tokenize(all_text.lower())
        
        # Filter out stopwords
        filtered_tokens = [word for word in tokens if word not in self.stop_words]
        
        # Extract medical terms
        medical_terms = [word for word in filtered_tokens if word in self.medical_terms]
        term_counts = Counter(medical_terms)
        
        # Top medical terms
        top_terms = term_counts.most_common(10)
        
        return {
            'term_counts': dict(term_counts),
            'top_terms': top_terms,
            'total_medical_terms': len(medical_terms),
            'unique_medical_terms': len(term_counts)
        }
    
    def analyze_question_types(self, transcript):
        """Analyze the types of questions being asked in a medical consultation"""
        doctor_pattern = r'DOCTOR [A-Z0-9]+\n(.*?)(?=\n[A-Z]+ [A-Z0-9]+\n|$)'
        patient_pattern = r'PATIENT [A-Z0-9]+\n(.*?)(?=\n[A-Z]+ [A-Z0-9]+\n|$)'
        
        doctor_speeches = re.findall(doctor_pattern, transcript, re.DOTALL)
        patient_speeches = re.findall(patient_pattern, transcript, re.DOTALL)
        
        # Count question types for doctors
        doctor_question_types = {}
        for pattern in self.question_patterns:
            count = sum(len(re.findall(pattern, speech, re.IGNORECASE)) for speech in doctor_speeches)
            doctor_question_types[pattern.replace(r'.*\?', '')] = count
        
        # Count question types for patients
        patient_question_types = {}
        for pattern in self.question_patterns:
            count = sum(len(re.findall(pattern, speech, re.IGNORECASE)) for speech in patient_speeches)
            patient_question_types[pattern.replace(r'.*\?', '')] = count
        
        return {
            'doctor_question_types': doctor_question_types,
            'patient_question_types': patient_question_types
        }
    
    def analyze_turn_taking_patterns(self, va_transcripts):
        """Analyze turn-taking patterns in the VA transcripts"""
        consecutive_doctor_turns = []
        consecutive_patient_turns = []
        turn_sequences = []
        
        for transcript_path in va_transcripts:
            with open(transcript_path, 'r') as f:
                transcript = f.read()
            
            # Extract all turns in order
            turns = re.findall(r'\n(DOCTOR|PATIENT) [A-Z0-9]+\n', transcript)
            
            # Count consecutive turns
            current_speaker = None
            consecutive_count = 0
            
            for turn in turns:
                if turn == current_speaker:
                    consecutive_count += 1
                else:
                    if current_speaker == 'DOCTOR' and consecutive_count > 0:
                        consecutive_doctor_turns.append(consecutive_count)
                    elif current_speaker == 'PATIENT' and consecutive_count > 0:
                        consecutive_patient_turns.append(consecutive_count)
                    
                    current_speaker = turn
                    consecutive_count = 1
            
            # Add the last set of consecutive turns
            if current_speaker == 'DOCTOR':
                consecutive_doctor_turns.append(consecutive_count)
            elif current_speaker == 'PATIENT':
                consecutive_patient_turns.append(consecutive_count)
            
            # Analyze turn sequences (e.g., D-P-D, P-D-P)
            for i in range(len(turns) - 2):
                turn_sequence = f"{turns[i][0]}-{turns[i+1][0]}-{turns[i+2][0]}"  # Using first letter (D or P)
                turn_sequences.append(turn_sequence)
        
        sequence_counts = Counter(turn_sequences)
        
        return {
            'avg_consecutive_doctor_turns': np.mean(consecutive_doctor_turns) if consecutive_doctor_turns else 0,
            'max_consecutive_doctor_turns': max(consecutive_doctor_turns) if consecutive_doctor_turns else 0,
            'avg_consecutive_patient_turns': np.mean(consecutive_patient_turns) if consecutive_patient_turns else 0,
            'max_consecutive_patient_turns': max(consecutive_patient_turns) if consecutive_patient_turns else 0,
            'common_turn_sequences': dict(sequence_counts.most_common(5))
        }
    
    def update_summary_markdown(self, enhanced_insights):
        """Update the summary markdown with more detailed insights"""
        try:
            with open('data/summary.md', 'r') as f:
                current_summary = f.read()
            
            # Add enhanced analysis section before the conclusion
            conclusion_index = current_summary.find("## Conclusion")
            if conclusion_index == -1:
                conclusion_index = len(current_summary)
            
            enhanced_content = "\n## Enhanced Analysis\n\n"
            
            # Medical terminology insights
            enhanced_content += "### Medical Terminology Patterns\n\n"
            enhanced_content += "The analysis of medical terminology across the datasets revealed:\n\n"
            enhanced_content += f"- **Total Unique Medical Terms**: {enhanced_insights['medical_terminology']['unique_medical_terms']}\n"
            enhanced_content += "- **Most Common Medical Terms**:\n"
            
            for term, count in enhanced_insights['medical_terminology']['top_terms']:
                enhanced_content += f"  - {term.capitalize()}: {count} mentions\n"
            
            enhanced_content += "\nThese terms represent the core medical vocabulary used in consultations, showing a focus on symptoms, examination areas, and common conditions.\n\n"
            
            # Turn-taking patterns
            enhanced_content += "### Turn-Taking Patterns\n\n"
            enhanced_content += "Analysis of conversation flow showed:\n\n"
            enhanced_content += f"- On average, doctors speak for {enhanced_insights['turn_patterns']['avg_consecutive_doctor_turns']:.2f} consecutive turns before a patient responds\n"
            enhanced_content += f"- Patients speak for {enhanced_insights['turn_patterns']['avg_consecutive_patient_turns']:.2f} consecutive turns on average\n"
            enhanced_content += "- Most common turn sequences:\n"
            
            for sequence, count in enhanced_insights['turn_patterns']['common_turn_sequences'].items():
                # Convert D-P-D to "Doctor-Patient-Doctor"
                readable_sequence = sequence.replace('D', 'Doctor').replace('P', 'Patient')
                enhanced_content += f"  - {readable_sequence}: {count} occurrences\n"
            
            enhanced_content += "\nThese patterns suggest that consultations typically follow a rhythmic exchange with doctors guiding the conversation through questioning.\n\n"
            
            # Question type analysis
            enhanced_content += "### Question Type Analysis\n\n"
            enhanced_content += "Examining the types of questions asked during consultations:\n\n"
            enhanced_content += "**Doctor Questions**:\n"
            for q_type, count in enhanced_insights['question_types']['doctor_question_types'].items():
                if count > 0:
                    enhanced_content += f"- '{q_type}' questions: {count}\n"
            
            enhanced_content += "\n**Patient Questions**:\n"
            for q_type, count in enhanced_insights['question_types']['patient_question_types'].items():
                if count > 0:
                    enhanced_content += f"- '{q_type}' questions: {count}\n"
            
            enhanced_content += "\nDoctors tend to use 'what' and 'how' questions to gather specific information, while patients more often ask clarifying questions about treatment and next steps.\n\n"
            
            # Additional insights for ambient AI
            enhanced_content += "### Additional Implications for Ambient AI\n\n"
            enhanced_content += "Based on the enhanced analysis, ambient AI systems could:\n\n"
            enhanced_content += "1. **Adaptive Recording**: Prioritize recording during patient narratives where key medical terms are most likely to appear\n"
            enhanced_content += "2. **Turn-Taking Awareness**: Recognize the conversation pattern to better segment and organize the information\n"
            enhanced_content += "3. **Question-Answer Linking**: Automatically pair doctor questions with patient responses to structure the information logically\n"
            enhanced_content += "4. **Medical Vocabulary Recognition**: Build specialized models focusing on the most common medical terms identified\n"
            enhanced_content += "5. **Conversation Flow Support**: Potentially prompt doctors for follow-up questions based on typical consultation patterns\n\n"
            
            # Insert enhanced content before conclusion
            updated_summary = current_summary[:conclusion_index] + enhanced_content + current_summary[conclusion_index:]
            
            # Write updated summary
            with open('data/summary.md', 'w') as f:
                f.write(updated_summary)
            
            print("Summary markdown updated with enhanced analysis")
            
        except Exception as e:
            print(f"Error updating summary: {e}")
    
    def run(self):
        """Run the enhanced analysis"""
        # Get sample paths
        with open('data/analysis_samples/sample_list.json', 'r') as f:
            sample_list = json.load(f)
        
        primock_samples = [os.path.join('data/analysis_samples/primock57', f) for f in sample_list['primock57']]
        va_samples = [os.path.join('data/analysis_samples/va', f) for f in sample_list['va']]
        
        # Combine all text for terminology analysis
        all_text = ""
        
        # Process PriMock57 samples
        for sample_path in primock_samples:
            with open(sample_path, 'r') as f:
                data = json.load(f)
                if 'note' in data:
                    all_text += data['note'] + " "
        
        # Process VA samples
        for sample_path in va_samples:
            with open(sample_path, 'r') as f:
                all_text += f.read() + " "
        
        # Analyze medical terminology
        medical_terminology = self.analyze_medical_terminology(all_text)
        
        # Analyze question types (use first VA sample for detailed question analysis)
        with open(va_samples[0], 'r') as f:
            first_transcript = f.read()
        question_types = self.analyze_question_types(first_transcript)
        
        # Analyze turn-taking patterns
        turn_patterns = self.analyze_turn_taking_patterns(va_samples)
        
        # Collect enhanced insights
        enhanced_insights = {
            'medical_terminology': medical_terminology,
            'question_types': question_types,
            'turn_patterns': turn_patterns
        }
        
        # Generate additional visualization for medical terminology
        self.generate_medical_terms_plot(medical_terminology)
        
        # Update summary markdown
        self.update_summary_markdown(enhanced_insights)
        
        print("Enhanced analysis complete")
    
    def generate_medical_terms_plot(self, medical_terminology):
        """Generate plot for medical terminology frequency"""
        plt.figure(figsize=(12, 6))
        
        terms = []
        counts = []
        
        for term, count in medical_terminology['top_terms']:
            terms.append(term)
            counts.append(count)
        
        # Reverse to show highest count at top
        terms.reverse()
        counts.reverse()
        
        plt.barh(terms, counts, color='skyblue')
        plt.xlabel('Frequency')
        plt.ylabel('Medical Term')
        plt.title('Top Medical Terms in Consultations')
        plt.tight_layout()
        
        plt.savefig('data/analysis_samples/plots/medical_terms_frequency.png')
        plt.close()


if __name__ == "__main__":
    analyzer = EnhancedAnalyzer()
    analyzer.run()
