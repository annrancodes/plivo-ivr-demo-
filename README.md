 Plivo IVR Demo

This project demonstrates a simple IVR system using Plivo Voice API.

## Features
- Outbound call using Plivo
- Language selection
- Multi-level IVR
- Audio playback
- Call forwarding

## Tech Stack
Python, Flask, Plivo API, ngrok

## Running the Project

1. Install dependencies
pip install flask plivo

2. Start server
python app.py

3. Expose server
ngrok http 5000

4. Trigger call
python trigger_call.py
