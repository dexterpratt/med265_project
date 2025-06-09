class TranscriptViewer {
    constructor() {
        this.transcript = [];
        this.currentStep = 0;
        this.autoPlayInterval = null;
        this.isAutoPlaying = false;
        
        this.initializeElements();
        this.bindEvents();
        this.loadDemoTranscript();
    }

    initializeElements() {
        this.fileInput = document.getElementById('fileInput');
        this.uploadBtn = document.getElementById('uploadBtn');
        this.fileName = document.getElementById('fileName');
        this.noFileMessage = document.getElementById('noFileMessage');
        this.mainInterface = document.getElementById('mainInterface');
        this.controls = document.getElementById('controls');
        this.conversationContainer = document.getElementById('conversationContainer');
        this.patientInfoContent = document.getElementById('patientInfoContent');
        this.assessmentContent = document.getElementById('assessmentContent');
        this.prevBtn = document.getElementById('prevBtn');
        this.nextBtn = document.getElementById('nextBtn');
        this.autoPlayBtn = document.getElementById('autoPlayBtn');
        this.stepCounter = document.getElementById('stepCounter');
        this.progressFill = document.getElementById('progressFill');
    }

    bindEvents() {
        this.uploadBtn.addEventListener('click', () => this.fileInput.click());
        this.fileInput.addEventListener('change', (e) => this.handleFileUpload(e));
        this.prevBtn.addEventListener('click', () => this.previousStep());
        this.nextBtn.addEventListener('click', () => this.nextStep());
        this.autoPlayBtn.addEventListener('click', () => this.toggleAutoPlay());
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowLeft') this.previousStep();
            if (e.key === 'ArrowRight') this.nextStep();
            if (e.key === ' ') {
                e.preventDefault();
                this.toggleAutoPlay();
            }
        });
    }

    loadDemoTranscript() {
        try {
            console.log('Loading embedded demo transcript...');
            
            // Embedded demo content to avoid CORS issues
            const demoContent = `# VA Consultation O721 with MedSys AI Simulation

### DOCTOR:
Hello, Mr. [Patient]. Nice to meet you. I see you're here with your wife today?

### PATIENT:
Yes, this is my wife.

### DOCTOR:
Good to meet you both. Before we start, I want to let you know that our MedSys system is recording our conversation to help with note-taking. You can see on this screen here [gestures to shared display] what's being captured. MedSys, please show us the patient's current vitals and medications.

### [SHARED DISPLAY SHOWS]:
\`\`\`
PATIENT: [Patient Name]
DOB: [Date]
VITALS (taken by nurse at check-in):
- BP: 118/72
- HR: 86
- Temp: 97.8°F
- O2 Sat: 94%
- Weight: 132 lbs (recorded weight loss noted)

CURRENT MEDICATIONS:
- Fentanyl patch 50mcg/72hrs
- Dilaudid 2mg every 2hrs PRN pain
- Lidoderm patch daily
- Zyprexa 5mg at bedtime
- Ativan 0.5mg PRN anxiety
- Docusate sodium daily
- Suppositories PRN constipation

HOSPICE CARE: Enrolled [date], managed by [Provider]
\`\`\`

### [DOCTOR'S PRIVATE DISPLAY SHOWS]:
\`\`\`
STAGE IV LUNG CANCER
- Diagnosed: [Date]
- No surgical options - tumor near heart (3.2cm)
- Recent admission 12/25-1/2 for electrolyte imbalance
- Progressive decline with significant weight loss
- Recent pain control issues - inadequate relief with current regimen
- Oncology last seen: August, deemed not candidate for chemo/radiation
- Patient has upcoming Oncology appointment on Thursday

ALERT: Calcium levels were abnormal during last admission
ALERT: Pain management appears suboptimal based on last note
\`\`\`

### DOCTOR:
I see you were in the hospital with us in December through early January. How have you been feeling since then?

### PATIENT:
I've been having a lot of pain, mostly in my abdomen.

### DOCTOR:
Can you show me where the pain is?

### DOCTOR:
MedSys, note the patient is indicating left lower quadrant abdominal pain.

### [SHARED DISPLAY UPDATES]:
\`\`\`
CURRENT VISIT - KEY POINTS:
- Patient reports abdominal pain in left lower quadrant
- Pain not adequately controlled with current medications
- Pain described as constant with periods of increased intensity
\`\`\`

### WIFE:
He's been on Dilaudid every two hours, but it only seems to help for about 45 minutes. He's also using the Fentanyl patch, but his pain is still not controlled.

### DOCTOR:
I can feel a protrusion there. It appears to be a hernia. MedSys, add probable abdominal wall hernia to the assessment.

### [SHARED DISPLAY UPDATES]:
\`\`\`
ASSESSMENT:
- Probable abdominal wall hernia causing left lower quadrant pain
- Stage IV lung cancer (ongoing hospice care)
- Pain management needs adjustment
\`\`\`

### [DOCTOR'S PRIVATE DISPLAY UPDATES]:
\`\`\`
ASSESSMENT:
- Abdominal wall hernia, likely incisional from previous bowel surgery
- Low surgical candidacy due to advanced cancer state
- Pain management: Consider increasing Fentanyl patch to 100mcg/72hrs
- Consider changing Dilaudid to q1h instead of q2h
- Need to coordinate with Hospice provider regarding medication changes
\`\`\`

### DOCTOR:
I think we should check your electrolyte levels today. MedSys, please prepare lab orders for comprehensive metabolic panel.

### [SHARED DISPLAY UPDATES]:
\`\`\`
PLANNED ORDERS:
- Blood work to check electrolyte levels (comprehensive metabolic panel)
\`\`\`

### WIFE:
He's also been coughing up some green sputum recently, which is new.

### [SHARED DISPLAY UPDATES]:
\`\`\`
NEW SYMPTOMS:
- Green productive cough (new)
\`\`\`

### DOCTOR:
Thank you for mentioning that. MedSys, note that this is likely related to his underlying lung cancer.

### [SHARED DISPLAY UPDATES]:
\`\`\`
ASSESSMENT (updated):
- Probable abdominal wall hernia causing left lower quadrant pain
- Stage IV lung cancer with possible progression (new productive cough)
- Pain management needs adjustment
\`\`\`

### DOCTOR:
Let's discuss the plan for your pain management. MedSys, contact the pharmacy to see if we can modify the Dilaudid prescription to every 1 hour instead of every 2 hours.

### [SHARED DISPLAY UPDATES]:
\`\`\`
TREATMENT PLAN:
- Check electrolyte levels today
- Adjust pain medication: Consider Dilaudid every 1 hour instead of 2
- Discuss potential Fentanyl patch dose increase with Hospice
- Follow up with Oncology on Thursday as scheduled
\`\`\`

### PATIENT:
Can we also get the Lidoderm patches? We're almost out.

### DOCTOR:
MedSys, is Lidoderm patch on our formulary?

### [DOCTOR'S PRIVATE DISPLAY SHOWS]:
\`\`\`
FORMULARY ALERT: Lidoderm (lidocaine) patch is non-formulary. 
Requires special approval. Alternatives: None suitable for topical pain relief.
\`\`\`

### DOCTOR:
I see it's not on our regular medication list. MedSys, please note that we need to request a special approval for Lidoderm patches and also check on the nicotine patches the patient has been using.

### [SHARED DISPLAY UPDATES]:
\`\`\`
TREATMENT PLAN (updated):
- Check electrolyte levels today
- Adjust pain medication: Dilaudid every 1 hour instead of 2
- Discuss potential Fentanyl patch dose increase with Hospice
- Request special approval for Lidoderm patches
- Request nicotine patches
- Follow up with Oncology on Thursday as scheduled
\`\`\`

### WIFE:
I notice it doesn't mention his anxiety medications. He needs both the Ativan and Zyprexa to manage his anxiety.

### DOCTOR:
Thank you for catching that. MedSys, please add to the treatment plan that the patient should continue both Ativan as needed for anxiety and scheduled Zyprexa.

### [SHARED DISPLAY UPDATES]:
\`\`\`
MEDICATION PLAN:
- Continue Ativan as needed for anxiety
- Continue scheduled Zyprexa
- (Other medication adjustments as noted above)
\`\`\``;

            this.transcript = this.parseTranscript(demoContent);
            this.fileName.textContent = '0721_medsys_simulation.md (Demo)';
            this.showMainInterface();
            this.resetViewer();
            console.log('Demo transcript loaded successfully');
        } catch (error) {
            console.warn('Could not load demo transcript:', error.message);
            console.log('Demo file not found, showing upload interface');
            // If demo can't be loaded, show the normal upload interface
        }
    }

    async handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;

        try {
            const content = await this.readFile(file);
            this.transcript = this.parseTranscript(content);
            this.fileName.textContent = file.name;
            this.showMainInterface();
            this.resetViewer();
        } catch (error) {
            alert('Error reading file: ' + error.message);
        }
    }

    readFile(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (e) => resolve(e.target.result);
            reader.onerror = (e) => reject(new Error('Failed to read file'));
            reader.readAsText(file);
        });
    }

    parseTranscript(content) {
        console.log('Starting transcript parsing...');
        const lines = content.split('\n');
        const transcript = [];
        
        // First pass: extract all sections
        const sections = [];
        let currentSection = null;
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();
            
            // Debug: log lines that look like they might be speakers
            if (line.includes('DOCTOR:') || line.includes('PATIENT:') || line.includes('WIFE:')) {
                console.log(`Found potential speaker line ${i}: "${line}"`);
            }
            
            // Skip empty lines and headers (but NOT speaker lines that start with ###)
            if (!line || (line.startsWith('#') && !line.startsWith('###')) || line.startsWith('*[') || line.startsWith('---')) {
                continue;
            }
            
            // Check for speaker lines
            if (line.startsWith('### DOCTOR:') || line.startsWith('### PATIENT:') || line.startsWith('### WIFE:')) {
                if (currentSection) {
                    sections.push(currentSection);
                }
                
                currentSection = {
                    type: 'speaker',
                    line: line,
                    content: [],
                    lineNumber: i
                };
                console.log(`Created speaker section: ${line}`);
            }
            // Check for display lines
            else if (line.includes('[SHARED DISPLAY') || line.includes('[DOCTOR\'S PRIVATE DISPLAY')) {
                if (currentSection) {
                    sections.push(currentSection);
                }
                
                currentSection = {
                    type: 'display',
                    line: line,
                    content: [],
                    lineNumber: i
                };
                console.log(`Created display section: ${line}`);
            }
            // Add content to current section
            else if (currentSection) {
                currentSection.content.push(line);
            }
        }
        
        // Add final section
        if (currentSection) {
            sections.push(currentSection);
        }
        
        console.log('Found sections:', sections.length);
        
        // Second pass: process sections into transcript steps
        for (const section of sections) {
            if (section.type === 'speaker') {
                const speaker = this.extractSpeaker(section.line);
                const content = this.extractSpeakerContent(section.line, section.content);
                
                if (speaker && content.trim()) {
                    transcript.push({
                        type: 'dialogue',
                        speaker: speaker,
                        content: content.trim()
                    });
                    console.log(`Added dialogue: ${speaker} - "${content.trim().substring(0, 50)}..."`);
                }
            }
            else if (section.type === 'display') {
                const displayType = section.line.includes('SHARED') ? 'shared' : 'private';
                const content = this.extractDisplayContent(section.content);
                
                if (content.trim()) {
                    transcript.push({
                        type: 'display',
                        displayType: displayType,
                        content: content.trim()
                    });
                    console.log(`Added display: ${displayType} - "${content.trim().substring(0, 50)}..."`);
                }
            }
        }
        
        console.log('Final transcript length:', transcript.length);
        return transcript;
    }
    
    extractSpeaker(line) {
        if (line.startsWith('### DOCTOR:')) return 'doctor';
        if (line.startsWith('### PATIENT:')) return 'patient';
        if (line.startsWith('### WIFE:')) return 'wife';
        return null;
    }
    
    extractSpeakerContent(line, contentLines) {
        // Get content from the speaker line itself
        let content = '';
        if (line.startsWith('### DOCTOR:')) {
            content = line.substring(12).trim();
        } else if (line.startsWith('### PATIENT:')) {
            content = line.substring(13).trim();
        } else if (line.startsWith('### WIFE:')) {
            content = line.substring(10).trim();
        }
        
        // Add any following content lines (but not code blocks or new sections)
        for (const contentLine of contentLines) {
            if (contentLine.startsWith('```') || contentLine.startsWith('###')) {
                break;
            }
            if (contentLine.trim() && !contentLine.startsWith('*[')) {
                content += ' ' + contentLine.trim();
            }
        }
        
        return content;
    }
    
    extractDisplayContent(contentLines) {
        let inCodeBlock = false;
        const codeLines = [];
        
        for (const line of contentLines) {
            if (line.trim() === '```') {
                inCodeBlock = !inCodeBlock;
                continue;
            }
            
            if (inCodeBlock) {
                codeLines.push(line);
            }
        }
        
        return codeLines.join('\n');
    }

    showMainInterface() {
        this.noFileMessage.style.display = 'none';
        this.mainInterface.style.display = 'flex';
        this.controls.style.display = 'flex';
    }

    resetViewer() {
        this.currentStep = 0;
        this.conversationContainer.innerHTML = '';
        this.patientInfoContent.innerHTML = '<div class="placeholder-text">Patient information will appear here</div>';
        this.assessmentContent.innerHTML = '<div class="placeholder-text">Assessment information will appear here</div>';
        this.updateControls();
        this.updateProgress();
    }

    renderStep() {
        if (this.currentStep >= this.transcript.length) return;

        const step = this.transcript[this.currentStep];

        if (step.type === 'dialogue') {
            this.addConversationBubble(step.speaker, step.content);
        } else if (step.type === 'display') {
            this.updateDisplay(step.displayType, step.content);
        }

        this.updateControls();
        this.updateProgress();
        this.scrollToBottom();
    }

    addConversationBubble(speaker, content) {
        const turnDiv = document.createElement('div');
        turnDiv.className = `conversation-turn ${speaker}`;

        const avatar = document.createElement('div');
        avatar.className = `avatar ${speaker}`;
        
        // Set avatar icons
        const avatarIcons = {
            doctor: '👨‍⚕️',
            patient: '👨',
            wife: '👩'
        };
        avatar.textContent = avatarIcons[speaker] || '👤';

        const bubble = document.createElement('div');
        bubble.className = `speech-bubble ${speaker}`;

        const label = document.createElement('div');
        label.className = 'speaker-label';
        label.textContent = speaker.charAt(0).toUpperCase() + speaker.slice(1);

        const text = document.createElement('div');
        text.className = 'speech-text';
        text.textContent = content;

        bubble.appendChild(label);
        bubble.appendChild(text);

        if (speaker === 'doctor') {
            turnDiv.appendChild(avatar);
            turnDiv.appendChild(bubble);
        } else {
            turnDiv.appendChild(bubble);
            turnDiv.appendChild(avatar);
        }

        this.conversationContainer.appendChild(turnDiv);
    }

    updateDisplay(displayType, content) {
        // Determine which pane to update based on content
        const isPatientInfo = content.includes('PATIENT:') || content.includes('VITALS') || 
                             content.includes('MEDICATIONS') || content.includes('HOSPICE') ||
                             content.includes('PACIENTE:') || content.includes('SIGNOS VITALES') ||
                             content.includes('MEDICAMENTOS') || content.includes('CUIDADOS PALIATIVOS');

        const targetElement = isPatientInfo ? this.patientInfoContent : this.assessmentContent;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'display-content updated-content';
        contentDiv.textContent = content;

        targetElement.innerHTML = '';
        targetElement.appendChild(contentDiv);

        // Remove animation class after animation completes
        setTimeout(() => {
            contentDiv.classList.remove('updated-content');
        }, 500);
    }

    scrollToBottom() {
        this.conversationContainer.scrollTop = this.conversationContainer.scrollHeight;
    }

    nextStep() {
        if (this.currentStep < this.transcript.length) {
            this.renderStep();
            this.currentStep++;
        }
    }

    previousStep() {
        if (this.currentStep > 0) {
            this.currentStep--;
            this.replayToCurrentStep();
        }
    }

    replayToCurrentStep() {
        // Clear everything and replay up to current step
        this.conversationContainer.innerHTML = '';
        this.patientInfoContent.innerHTML = '<div class="placeholder-text">Patient information will appear here</div>';
        this.assessmentContent.innerHTML = '<div class="placeholder-text">Assessment information will appear here</div>';

        for (let i = 0; i < this.currentStep; i++) {
            const step = this.transcript[i];
            
            if (step.type === 'dialogue') {
                this.addConversationBubble(step.speaker, step.content);
            } else if (step.type === 'display') {
                // For replay, update display without animation
                const isPatientInfo = step.content.includes('PATIENT:') || step.content.includes('VITALS') || 
                                     step.content.includes('MEDICATIONS') || step.content.includes('HOSPICE') ||
                                     step.content.includes('PACIENTE:') || step.content.includes('SIGNOS VITALES') ||
                                     step.content.includes('MEDICAMENTOS') || step.content.includes('CUIDADOS PALIATIVOS');

                const targetElement = isPatientInfo ? this.patientInfoContent : this.assessmentContent;
                
                const contentDiv = document.createElement('div');
                contentDiv.className = 'display-content';
                contentDiv.textContent = step.content;

                targetElement.innerHTML = '';
                targetElement.appendChild(contentDiv);
            }
        }

        this.updateControls();
        this.updateProgress();
        this.scrollToBottom();
    }

    toggleAutoPlay() {
        if (this.isAutoPlaying) {
            this.stopAutoPlay();
        } else {
            this.startAutoPlay();
        }
    }

    startAutoPlay() {
        this.isAutoPlaying = true;
        this.autoPlayBtn.textContent = '⏸ Pause';
        this.autoPlayBtn.classList.add('playing');
        
        this.autoPlayInterval = setInterval(() => {
            if (this.currentStep >= this.transcript.length) {
                this.stopAutoPlay();
                return;
            }
            this.nextStep();
        }, 2000); // 2 seconds between steps
    }

    stopAutoPlay() {
        this.isAutoPlaying = false;
        this.autoPlayBtn.textContent = '▶ Auto Play';
        this.autoPlayBtn.classList.remove('playing');
        
        if (this.autoPlayInterval) {
            clearInterval(this.autoPlayInterval);
            this.autoPlayInterval = null;
        }
    }

    updateControls() {
        this.prevBtn.disabled = this.currentStep === 0;
        this.nextBtn.disabled = this.currentStep >= this.transcript.length;
        
        if (this.currentStep >= this.transcript.length && this.isAutoPlaying) {
            this.stopAutoPlay();
        }
    }

    updateProgress() {
        const total = this.transcript.length;
        const current = Math.min(this.currentStep, total);
        
        this.stepCounter.textContent = `Step ${current} of ${total}`;
        
        const percentage = total > 0 ? (current / total) * 100 : 0;
        this.progressFill.style.width = percentage + '%';
    }
}

// Initialize the application when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new TranscriptViewer();
});
