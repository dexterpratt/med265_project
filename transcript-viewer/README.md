# MedSys Transcript Viewer

A standalone web application for viewing and stepping through MedSys simulation transcripts. This tool allows you to upload simulation transcripts and experience them as an interactive conversation with real-time updates to the MedSys display panels.

## Features

- **File Upload**: Upload `.md` or `.txt` simulation transcript files
- **Interactive Playback**: Step through conversations turn by turn
- **Speech Bubbles**: Realistic conversation interface with doctor, patient, and family member bubbles
- **MedSys Display**: Live updates to patient information and assessment panels
- **Navigation Controls**: Previous/Next buttons, progress tracking, and auto-play functionality
- **Keyboard Shortcuts**: Arrow keys for navigation, spacebar for auto-play toggle
- **Responsive Design**: Works on desktop and mobile devices

## How to Use

1. **Open the Application**: Open `index.html` in any modern web browser
2. **Upload a Transcript**: Click "Upload Transcript" and select a simulation file
3. **Navigate**: Use the controls at the bottom to step through the conversation:
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

1. Load the included sample file (`sample_simulation.md`) or any MedSys simulation transcript
2. Click "Next →" to see the doctor's first statement appear in a speech bubble
3. Continue clicking "Next →" to see the conversation unfold and MedSys displays update
4. Use "Auto Play" to watch the entire simulation automatically
5. Use "← Previous" to review any part of the conversation

## Interface Layout

- **Left Side**: Conversation area with speech bubbles for each participant
- **Right Side**: MedSys display panels
  - **Top Panel** (Green): Patient information, vitals, medications
  - **Bottom Panel** (Blue): Assessment and clinical notes
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

## Troubleshooting

**File won't upload**: Ensure the file is a `.md` or `.txt` file with proper MedSys simulation formatting

**Display not updating**: Check that display blocks in the transcript are properly formatted with code blocks (```)

**Conversation bubbles missing**: Verify that speaker lines start with `### DOCTOR:`, `### PATIENT:`, or `### WIFE:`

## File Structure

```
transcript-viewer/
├── index.html      # Main application file
├── styles.css      # Styling and layout
├── script.js       # Application logic
└── README.md       # This documentation
```

To use the application, simply open `index.html` in a web browser - no installation or setup required.
