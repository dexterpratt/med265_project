# med265_final_project
This repo contains data and scripts relelvant to the MED 265 final project

The assignment is to specify a project to improve some aspect of clinical decision making, quality assessment, registry creation. 

We will not perform the project, just specify it.

The outputs are:

* 15-minute presentation + 5-10 min Q&A
* ~4-5 page write-up of the project

For the rest of this document, "project" refers to the hypothetical project that we will specify.

## Project Goals

## Current Plan of Action:

* Literature search to corroborate that this is a problem and get information to refine the problem statement.   
* Refine the problem statement  
* Literature review of ambient listening uses/technology  
* Literature review of medical interview AI  
* Decide goals for analysis of doctor-patient transcriptions  
* Role play interviews with ChatGPT or Claude or Gemini  
  * Guide this with results of transcripts?  
  * Role play selected, interesting transcripts?


# Project Title:

TBD

# Statement of problem:

Data entry during patient interactions causes several problems:

- Check in questions are repeated by doctors, wasting time  
- Impaired attention to the patient by doctors.  
- Impaired perception of engagement by patients  
- Errors and omission of data by doctors.

## Existing solution:

A recent approach is AI ambient listening. It transcribes notes while the doctor engages.

Some doctors find this very useful, timesaving, better engagement

Problems with ambient:

* Patient rejection, because:  
  * Patients may be concerned about some things they say being “on the record”  
  * General concerns about AI 

# Evidence-Based Literature Review and Synthesis:

## Literature Discussing the Problem

[Enhancing clinical documentation with ambient artificial intelligence: a quality improvement survey assessing clinician perspectives on work burden, burnout, and job satisfaction](https://pmc.ncbi.nlm.nih.gov/articles/PMC11843214/)

[Computers in the Exam Room: Differences in Physician–Patient Interaction May Be Due to Physician Experience \- PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1824776/)

[Effect of computer use on physician-patient communication using interviews: A patient perspective \- PubMed](https://pubmed.ncbi.nlm.nih.gov/30914186/)

[Patients’ perspectives and preferences toward telemedicine versus in-person visits: a mixed-methods study on 1226 patients | BMC Medical Informatics and Decision Making](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-023-02348-4#:~:text=The%20study%20compared%20patient%20preferences,successful%20design%20and%20implementation%20outcomes)

[How Commure’s Ambient AI Epic Integration is Transforming Multilingual Care at North East Medical Services \- Blog](https://www.commure.com/blog/how-commures-ambient-epic-integration-is-transforming-multilingual-care-at-north-east-medical-services)

## Primary Care Interview Transcripts

### PriMock57

[https://github.com/babylonhealth/primock57/tree/main](https://github.com/babylonhealth/primock57/tree/main)

The dataset consists of 57 mock medical primary care consultations held over 5 days by 7 Babylon clinicians and 57 Babylon employees acting as patients, using case cards with presenting complaints, symptoms, medical & general history etc.:

### Physician-patient transcripts with 4C coding analysis from the Contextualizing Care research program

This dataset consists of 405 transcriptions of audio recorded physician-patient interactions conducted at Veterans Health Administration (VHA) medical center primary care clinics. 

This is referred to as "VA" in this repo.

\<downloaded by Dexter\>

The recordings were collected utilizing concealed (except where indicated) audio recorders by patients. The protocol was approved by VHA Institutional Review Boards, and participating physicians and patients consented to participate in the study. The interactions were analyzed using Content Coding for Contextualization of Care ("4C"). An excel spreadsheet with the coding of the original audio of each transcript is included. All data has been de-identified. "xxx" indicates PHI was removed. "@@@" indicates transcriber did not understand audio. These transcripts are a resource to medical educators and research scientists seeking transcriptions of primary care encounters, as well as those interested in 4C coding in its early stages. Their acquisition was supported with research funding from the Department of Veterans Affairs, Veterans Health Administration, Office of Research and Development, Health Services Research & Development.

### A dataset of simulated patient-physician medical interviews with a focus on respiratory cases

Faiha Fareez 1,2, Tishya Parikh 1,2, Christopher Wavell 1,2, Saba Shahab 1,2, Meghan Chevalier 1,2, Scott Good 1,2, Isabella De Blasi 1,2, Rafik Rhouma 2,3,4, Christopher McMahon 2,3, Jean-Paul Lam 2,3, Thomas Lo 2, Christopher W Smith 1,2,✉  
Author information  
Article notes  
Copyright and License information  
PMCID: PMC9203765  PMID: 35710769

**Large download because the transcripts are bundled with the audio.** 

[https://springernature.figshare.com/articles/dataset/Collection\_of\_simulated\_medical\_exams/16550013?backTo=%2Fcollections%2FA\_dataset\_of\_simulated\_patient-physician\_medical\_interviews\_with\_a\_focus\_on\_respiratory\_cases%2F5545842\&file=30598530](https://springernature.figshare.com/articles/dataset/Collection_of_simulated_medical_exams/16550013?backTo=%2Fcollections%2FA_dataset_of_simulated_patient-physician_medical_interviews_with_a_focus_on_respiratory_cases%2F5545842&file=30598530)

# Project Aims

## Improvement Goals:

* ? increase participation?  
* ? improved perception of engagement, positive interaction?  
* ? more complete

## Proposed Approach:

We propose to extend existing AI ambient listening systems by the addition of realtime displays of information to achieve the following benefits. In an in-person patient-PCP visit, there would be two displays, one large display visible to both the patient and the doctor and another only visible to the doctor. In a virtual visit, the patient would see both the doctor and an information panel displaying the shared information. The AI would be extended to become an assistant agent that could accept instructions and and questions from the doctor. The level of its "presence" in the conversation.

The shared screen would display patient data in one panel, defaulting to current measurements, medications, and notes taken by a nurse before the doctor arrived, but able to display any data that the doctor requests. In the other panel, it would display a continually updating summary of the key points of the visit, information that the patient would see in their after visit summary paperwork. The language would be patient-friendly. 

The doctor's screen will display a continually updated, precise clinical summary. It would be the starting point for them to review and edit later to be their final notes. This is what the current ambient listening AI provides, but it would be dynamic so that they might catch issues in real-time that they could ask the agent to note.

The doctor could instruct the AI to remove or edit the patient-visible summary in realtime. We propose that this will give the patient confidence that they know what will be recorded and, by providing agency, give them a sense of agency.

The shared screen will also help note and correct ommisions or inaccuracies in the patient's records.  

The ability to get information in realtime, mediated by the agent, will decrease distraction and improve patient-doctor engagement beyond the improvements already provided by ambient listening.


* Shared display, realtime updates and edits  
* Enable consensus  
  * Edits, remove information  
  * Helps patient note omissions, prompts them for better details  
* Avoid realtime edits to control time? What about adding voice notes to ambient as a way capture revisions.  
* Its an agent, not just a recorder. We can choose the level of “presence”  
  * Doctors get to set preferences  
* Allowed to access past records? Could create better prompts if able to access

## Proposed Benefits:

* Improve transparency for ambient listening   
* Improve patient engagement without sacrificing note taking  
* Improve gap in knowledge for the patient  
* Can also facilitate multi-lingual communication

## Potential Problems:

* Takes more time if engagement is uncontrolled  
  * Could this be addressed by pre-filling?  
* Not a benefit to visually impaired

## Questions:

* Should we allow later view/comments by patient  
* Is patient transparency actually desirable or important?  
* Could the patient talk to the system before to pre-fill information?  
  * It is already on the shared screen  
  * Questions could be adaptive  
  * Like Google Amie but only gathers information.  
  * Might increase compliance  
- Cost of software \> cost of screens

# Project Methods

# Data Collection Plan

# Potential challenges/obstacles

# Timeline

Deployment in a pilot project  
If successful, what are scaling strategies?
