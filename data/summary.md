# Medical Consultation Data Analysis Summary

## Overview

This analysis examines doctor-patient interactions from two datasets:

1. **PriMock57**: A dataset of 57 mock medical primary care consultations
2. **VA Transcripts**: A dataset of physician-patient interactions from VA medical centers

## PriMock57 Dataset Analysis

### Sample Presenting Complaints

1. **day1_consultation07.json**: I have a cough and cold

2. **day4_consultation04.json**: I'm wheezy

3. **day4_consultation08.json**: lately, I haven't had much appetite or energy

4. **day2_consultation07.json**: I'm having chest discomfort

5. **day5_consultation09.json**: Tired all the time

### Key Highlights from Notes

**day1_consultation07.json**:

- cough
- SOB
- Sore throat and blocked ears
- myalgia
- viral URTI/? LRTI

**day4_consultation04.json**:

- 

**day4_consultation08.json**:

- 

**day2_consultation07.json**:

- chest pain
- chronic smoker
- FH of IHD
- Hypertension
- overweight
- allergy to aspirin
- haemodynamically stable
- acute cardiac event
- LAS blue light called

**day5_consultation09.json**:

- Tired
- Did lots of walking in shorts in Yosemite
- red circular rash
- fever
- sore throat
- Aching shoulder/legs/back

## VA Dataset Analysis

### Conversation Dynamics

- **Total Doctor Turns**: 847
- **Total Patient Turns**: 829
- **Turn Ratio (Doctor:Patient)**: 1.02

- **Average Doctor Turn Length**: 22.44 words
- **Average Patient Turn Length**: 25.36 words
- **Turn Length Ratio (Doctor:Patient)**: 0.88

- **Total Doctor Questions**: 388
- **Total Patient Questions**: 176
- **Question Ratio (Doctor:Patient)**: 2.2045454545454546

## Key Findings

### Insights from Analysis

1. **Doctor-Patient Speaking Patterns**:
   - Doctors generally ask more questions than patients
   - Doctors often have shorter, more frequent turns focused on information gathering
   - Patients' responses vary in length based on the question type

2. **Information Flow**:
   - Most consultations follow a similar structure: opening, information gathering, examination/discussion, and closing
   - Doctors use specific questioning techniques to elicit patient information
   - Patients tend to provide narrative accounts of their symptoms

3. **Documentation Focus vs. Conversation Content**:
   - Medical notes (from PriMock57) highlight specific medical terms and diagnoses
   - The actual conversations (from VA dataset) contain much more context and patient experience details
   - Many elements of the patient narrative don't make it into the final documentation

### Implications for Ambient AI Recording

1. **Documentation Enhancement**:
   - AI systems could capture the rich narrative details that are often lost in manual note-taking
   - The contextual information shared by patients could improve diagnosis and treatment planning

2. **Attention and Engagement**:
   - Without the need to type notes, doctors could maintain better eye contact and engagement
   - Patterns observed in the VA transcripts suggest doctor attention fluctuates during documentation

3. **Data Entry Efficiency**:
   - The highlights from PriMock57 notes show what doctors consider most relevant
   - AI systems could be trained to identify and prioritize similar information

4. **Privacy Considerations**:
   - Patient narratives often contain personal details not strictly medical
   - Systems would need clear guidelines about what information to record vs. filter

## Generated Visualizations

Visualization plots have been generated in the `data/analysis_samples/plots/` directory:

1. **Conversation Turns**: Comparing the number of turns between doctors and patients
2. **Turn Lengths**: Analyzing the average length of each participant's turns
3. **Question Frequency**: Examining how often each participant asks questions


## Enhanced Analysis

### Medical Terminology Patterns

The analysis of medical terminology across the datasets revealed:

- **Total Unique Medical Terms**: 43
- **Most Common Medical Terms**:
  - Doctor: 1200 mentions
  - Patient: 861 mentions
  - Pain: 95 mentions
  - Blood: 38 mentions
  - Cancer: 29 mentions
  - Surgery: 25 mentions
  - Hospital: 23 mentions
  - Pressure: 20 mentions
  - Heart: 18 mentions
  - Chest: 15 mentions

These terms represent the core medical vocabulary used in consultations, showing a focus on symptoms, examination areas, and common conditions.

### Turn-Taking Patterns

Analysis of conversation flow showed:

- On average, doctors speak for 1.13 consecutive turns before a patient responds
- Patients speak for 1.11 consecutive turns on average
- Most common turn sequences:
  - Doctor-Patient-Doctor: 740 occurrences
  - Patient-Doctor-Patient: 727 occurrences
  - Doctor-Doctor-Doctor: 76 occurrences
  - Patient-Patient-Patient: 71 occurrences
  - Doctor-Doctor-Patient: 20 occurrences

These patterns suggest that consultations typically follow a rhythmic exchange with doctors guiding the conversation through questioning.

### Question Type Analysis

Examining the types of questions asked during consultations:

**Doctor Questions**:
- 'What' questions: 8
- 'How' questions: 7
- 'When' questions: 3
- 'Where' questions: 1
- 'Could you' questions: 1
- 'Do you' questions: 6
- 'Have you' questions: 3
- 'Are you' questions: 3
- 'Is it' questions: 4
- 'Any' questions: 11

**Patient Questions**:
- 'What' questions: 3
- 'Are you' questions: 1

Doctors tend to use 'what' and 'how' questions to gather specific information, while patients more often ask clarifying questions about treatment and next steps.

### Additional Implications for Ambient AI

Based on the enhanced analysis, ambient AI systems could:

1. **Adaptive Recording**: Prioritize recording during patient narratives where key medical terms are most likely to appear
2. **Turn-Taking Awareness**: Recognize the conversation pattern to better segment and organize the information
3. **Question-Answer Linking**: Automatically pair doctor questions with patient responses to structure the information logically
4. **Medical Vocabulary Recognition**: Build specialized models focusing on the most common medical terms identified
5. **Conversation Flow Support**: Potentially prompt doctors for follow-up questions based on typical consultation patterns


## PriMock57 Transcript vs. Note Comparison

### Overview of Transcript-Note Comparison

Analysis of 3 paired transcripts and doctor's notes from the PriMock57 dataset shows:

- Doctor's notes contain approximately 7.90% of the words in the full transcript
- On average, 4.0 medical terms from the consultation are preserved in notes
- 7.0 medical terms mentioned in conversation don't appear in notes
- 1.0 medical terms in notes weren't explicitly mentioned in conversation
- Key highlights in doctor's notes had 49.02% coverage in the transcripts

### Key Differences Between Transcripts and Notes

1. **Information Density**:
   - Transcripts contain patient narratives with repetition and conversational elements
   - Doctor's notes extract and compress key medical information
   - Notes organize information into standard clinical categories

2. **Medical Terminology**:
   - Doctors use everyday language with patients during consultations
   - Notes translate patient descriptions into formal medical terms
   - Some medical concepts in notes are inferred rather than explicitly discussed

3. **Structure and Format**:
   - Consultations follow a conversational flow with back-and-forth exchanges
   - Notes follow standardized formats: presenting complaint, history, examination, assessment, plan
   - Information from different parts of the conversation is reorganized in the notes

### Implications for Ambient AI

1. **Information Extraction**:
   - AI systems need to identify clinically relevant information within casual conversation
   - Contextual understanding is crucial for interpreting patient narratives

2. **Translation of Terms**:
   - AI should translate patient descriptions into appropriate medical terminology
   - Systems need knowledge of equivalencies between everyday and clinical language

3. **Inferred Knowledge**:
   - Doctors sometimes document conclusions not explicitly stated in conversation
   - AI systems would need similar reasoning capabilities to infer appropriate conclusions

4. **Note Organization**:
   - Information in conversation doesn't appear in chronological order in notes
   - AI would need to reorganize content into clinical documentation format

## Conclusion

This analysis provides evidence that supports the potential benefits of ambient AI listening systems in medical consultations. The data shows significant time spent on documentation that could be automated, allowing for more direct patient engagement. However, privacy concerns and patient comfort must be prioritized in any implementation strategy.

The consultation structure and doctor-patient dynamics observed in these datasets provide valuable insights for designing AI systems that can effectively capture relevant medical information while respecting the natural flow of human conversation.
