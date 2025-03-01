# PDF-TO-MindMap-MindMapify-
Mindmapify is an AI-powered web app built with Streamlit and Google Gemini, designed to convert PDFs into structured mind maps for better comprehension and visualization.
# Mindmapify – AI-Powered PDF to Mind Map Converter

Mindmapify is a Streamlit-based application that allows users to upload a PDF file, extract its text content, and generate a structured **mind map** using **Google Gemini AI**. This tool helps users visualize key insights from documents efficiently, making it ideal for students, researchers, and professionals.

## Features

- **PDF Upload**: Upload your PDF file to extract its text content.
- **AI-Powered Summarization**: Uses **Google Gemini AI** to analyze and summarize key insights.
- **Mind Map Generation**: Converts extracted content into a structured mind map.
- **Interactive Visualization**: Displays the generated mind map interactively with zoom, drag, and auto-layout features.
- **Markdown & Image Export**: Allows users to download the generated mind map in Markdown or image format.

## Installation

To run the app locally, follow the steps below:

### Prerequisites

- Python 3.7+
- Streamlit
- PyMuPDF (Fitz)
- Google Gemini AI API
- NetworkX & Plotly

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/mindmapify.git
cd mindmapify
```

### Step 2: Install required libraries

```bash
pip install -r requirements.txt
```

### Step 3: Set up Google API Key

Replace the placeholder API key in the code with your valid **Google Gemini API key**:

```python
API_KEY = "YOUR_GOOGLE_API_KEY"
```

### Step 4: Run the app

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`.

## How It Works

1. **PDF Upload & Extraction**: Users upload a PDF, and the app extracts text using PyMuPDF.
2. **AI Analysis**: Google Gemini AI processes and summarizes the content.
3. **Mind Map Generation**: The app organizes the extracted information into an interactive mind map.
4. **Visualization**: The mind map is rendered with **Markmap**, allowing interactive exploration.
5. **Download & Export**: Users can download the mind map in Markdown or image format for future use.

## Usage

1. **Upload PDF**: Click on "Choose a PDF file" and upload your document.
2. **Processing**: The AI extracts and organizes content into a structured mind map.
3. **View Mind Map**: The interactive visualization helps users explore the document structure.
4. **Export & Save**: Download the generated mind map for offline use.

## File Structure

```
mindmapify/
│
├── app.py                  # Main Streamlit app file
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── assets/                 # (Optional) Folder for assets, images, etc.
```

## Technologies Used

- **Streamlit** – For interactive web app development.
- **Google Gemini AI** – For AI-powered summarization and analysis.
- **PyMuPDF (Fitz)** – For extracting text from PDFs.
- **Markmap** – For rendering interactive mind maps.
- **NetworkX & Plotly** – For visualization and mind map structuring.
- **Python** – The core programming language for the app.

## Future Enhancements

- **Real-time Collaboration** – Enable multiple users to edit and interact with mind maps.
- **Handwritten Notes Recognition** – Integrate OCR to process handwritten PDFs.
- **NLP-Powered Q&A** – Ask AI-powered questions about the document.
- **Customizable Themes** – Personalize the mind map appearance.
- **Cloud Sync & Export Options** – Save mind maps across devices seamlessly.

## Contact

For any queries, suggestions, or collaborations, feel free to reach out:

📧 Email: [mrajgude2003@gmail.com](mailto:your.email@example.com)
📌 LinkedIn: [https://www.linkedin.com/in/mayurrajgude/](https://www.linkedin.com/in/yourprofile)
🐙 GitHub: [https://github.com/mayurraj9378](https://github.com/yourusername)

## License

This project is licensed under the MIT License.

---


