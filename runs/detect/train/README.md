# Industrial Machinery Repair Assistant

## Overview
Industrial Machinery Repair Assistant is an AI-powered application that detects welding defects from uploaded images using the YOLOv11 object detection model. The system identifies the defect type, confidence score, severity, possible causes, repair steps, and preventive measures through a Streamlit web interface.

---

## Features

- AI-based welding defect detection
- Detects:
  - Crack
  - Porosity
  - Spatters
  - Excess Reinforcement
  - Good Welding
- Displays confidence score
- Shows severity level
- Provides repair recommendations
- Suggests preventive measures
- User-friendly Streamlit interface

---

## Technologies Used

- Python
- YOLOv11 (Ultralytics)
- PyTorch
- Streamlit
- Roboflow
- Pillow (PIL)
- JSON

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Saruthi214/Industrial-Machinery-Repair-Assistant.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Project Structure

```
Industrial-Machinery-Repair-Assistant
│
├── app.py
├── repair_guide.json
├── requirements.txt
├── data.yaml
├── runs/
├── README.md
```

---

## Usage

1. Launch the Streamlit application.
2. Upload a welding image.
3. Click **Detect Defect**.
4. View:
   - Detected defect
   - Confidence score
   - Severity
   - Cause
   - Repair steps
   - Prevention tips

---

## Author

**Saruthi V**