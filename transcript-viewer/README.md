# MedSys Transcript Viewer

A standalone web application for viewing and stepping through MedSys simulation transcripts. This tool automatically loads a demo simulation and allows you to upload additional transcripts to experience them as interactive conversations with real-time updates to the MedSys display panels.

## Features

- **Auto-Loading Demo**: Automatically loads the included simulation on startup
- **File Upload**: Upload additional `.md` or `.txt` simulation transcript files
- **Interactive Playback**: Step through conversations turn by turn
- **Speech Bubbles**: Realistic conversation interface with doctor, patient, and family member bubbles
- **MedSys Display**: Live updates to patient information and assessment panels
- **Navigation Controls**: Previous/Next buttons, progress tracking, and auto-play functionality
- **Keyboard Shortcuts**: Arrow keys for navigation, spacebar for auto-play toggle
- **Responsive Design**: Works on desktop and mobile devices
- **Professional Styling**: Modern MedSys corporate branding with blue gradients

## Quick Start

1. **Open the Application**: Open `index.html` in any modern web browser
2. **Demo Loads Automatically**: The application will automatically load and display the included MedSys simulation
3. **Navigate**: Use the controls at the bottom to step through the conversation:
   - **← Previous**: Go back one step
   - **Next →**: Advance one step
   - **▶ Auto Play**: Automatically advance through steps (2-second intervals)
   - **Progress Bar**: Shows current position in the transcript

## Distribution

This application is designed to be distributed as a complete zip archive. Simply:
1. Zip the entire `transcript-viewer` folder
2. Recipients can unzip and open `index.html` in any browser
3. The demo will load automatically - no setup required!

## How to Use

### Automatic Demo
The application automatically loads the included `0721_medsys_simulation.md` when opened, so you can start exploring immediately.

### Upload Additional Files
1. Click "Upload Transcript" to select additional simulation files
2. The viewer will switch to your uploaded file
3. Use the same navigation controls to explore

### Navigation
- **← Previous**: Go back one step
- **Next →**: Advance one step
- **▶ Auto Play**: Automatically advance through steps (2-second intervals)
- **Progress Bar**: Shows current position in the transcript

## Keyboard Shortcuts

- **Left Arrow**: Previous step
- **Right Arrow**: Next step  
- **Spacebar**: Toggle auto-play

## Supported File Formats

The application supports MedSys simulation transcripts in Markdown format with the following structure:

- Speaker sections marked with `### DOCTOR:`, `### PATIENT:`, `### WIFE:`
- Display updates marked with `### [SHARED DISPLAY SHOWS]:` or `### [DOCTOR'S PRIVATE DISPLAY SHOWS]:`
- Display content enclosed in code blocks (```)

## Example Usage

1. Open `index.html` - the demo loads automatically
2. Click "Next →" to see the doctor's first statement appear in a speech bubble
3. Continue clicking "Next →" to see the conversation unfold and MedSys displays update
4. Use "Auto Play" to watch the entire simulation automatically
5. Use "← Previous" to review any part of the conversation

## Interface Layout

- **Left Side (40%)**: Conversation area with speech bubbles for each participant
- **Right Side (60%)**: MedSys display panels arranged side by side
  - **Left Panel** (Green): Patient information, vitals, medications
  - **Right Panel** (Blue): Assessment and clinical notes
- **Bottom**: Navigation controls and progress indicator

## Browser Compatibility

This application works with all modern web browsers including:
- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

## Technical Details

- **Pure HTML/CSS/JavaScript**: No external dependencies required
- **Client-side processing**: All file parsing happens in the browser
- **Responsive design**: Adapts to different screen sizes
- **Local storage**: No data is sent to external servers
- **Auto-loading**: Automatically fetches and loads the demo simulation
- **Graceful fallback**: Shows upload interface if demo file cannot be loaded

## Troubleshooting

**Demo doesn't load**: Ensure all files are in the correct structure and the browser allows local file access

**File won't upload**: Ensure the file is a `.md` or `.txt` file with proper MedSys simulation formatting

**Display not updating**: Check that display blocks in the transcript are properly formatted with code blocks (```)

**Conversation bubbles missing**: Verify that speaker lines start with `### DOCTOR:`, `### PATIENT:`, or `### WIFE:`

## File Structure

```
transcript-viewer/
├── index.html              # Main application file
├── styles.css              # Styling and layout  
├── script.js               # Application logic
├── README.md               # This documentation
├── sample_simulation.md    # Backup sample file
└── simulations/
    ├── 0721_medsys_simulation.md        # Auto-loaded demo
    └── 0721_medsys_spanish_simulation.md # Spanish version
```

## For Distribution

This application is designed to be easily distributed:

1. **Zip the entire transcript-viewer folder**
2. **Recipients unzip and open index.html**
3. **Demo loads automatically - no setup required!**

The application works entirely offline and requires no installation, server setup, or external dependencies.
