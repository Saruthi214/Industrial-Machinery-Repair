# Industrial Machinery Repair Assistant

## Overview
Industrial Machinery Repair Assistant is an AI-powered computer vision application that detects welding defects from images using a YOLOv11 model. The system classifies defects, predicts their severity, and provides repair and prevention recommendations through an interactive Streamlit web interface.

## Problem Statement
Manual inspection of welds is time-consuming, inconsistent, and requires experienced inspectors. Small defects may be overlooked, leading to machinery failure, increased maintenance costs, and safety risks.

## Solution
The application automatically detects welding defects using deep learning and provides:
- Defect classification
- Confidence score
- Severity level
- Cause of the defect
- Repair steps
- Prevention recommendations

## Features
- Upload welding images
- AI-based defect detection (YOLOv11)
- Confidence score visualization
- Severity assessment
- Repair recommendations
- Prevention guidelines
- Modern Streamlit UI

## Technologies Used
- Python
- YOLOv11 (Ultralytics)
- OpenCV
- Pillow (PIL)
- Streamlit
- JSON
- Computer Vision
- Deep Learning

## Project Structure

```
Industrial-Machinery-Repair/
│
├── app.py
├── repair_guide.json
├── best.pt
├── requirements.txt
├── README.md
├── runs/
└── ...
```

## Installation

```bash
git clone https://github.com/Saruthi214/Industrial-Machinery-Repair.git
cd Industrial-Machinery-Repair
pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. Launch the Streamlit application.
2. Upload a welding image.
3. Click **Detect Defect**.
4. View the detected defect, confidence score, severity, repair steps, and prevention methods.

## Author

Saruthi V
B.E. Computer Science and Engineering
