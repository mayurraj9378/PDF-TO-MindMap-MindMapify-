import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
import streamlit.components.v1 as components

# Define the API key directly in the code
API_KEY = "Google API Key"

def configure_genai():
    """Configure the Gemini AI with the API key."""
    if not API_KEY:
        st.error("API Key is missing. Please provide a valid Google API key.")
        return False
    try:
        genai.configure(api_key=API_KEY)
        return True
    except Exception as e:
        st.error(f"Error configuring Google API: {str(e)}")
        return False

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file."""
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:  # Only add non-empty pages
                text += page_text + "\n"
        if not text.strip():
            st.warning("No text could be extracted from the PDF. Please ensure it's not scanned or image-based.")
            return None
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

# def get_available_model():
#     """Get the first available text model from the API."""
#     try:
#         models = genai.list_models()
#         available_models = [model.name for model in models if 'generateContent' in model.supported_generation_methods]
        
#         if not available_models:
#             st.error("No suitable generative models found in your account.")
#             return None
            
#         # For debugging - show available models
#         st.info(f"Available models: {', '.join(available_models)}")
        
#         # Try to find a Gemini model in the available models
#         preferred_models = [
#             'gemini-1.5-pro',
#             'gemini-1.5-flash',
#             'gemini-pro',
#             'gemini-pro-vision'
#         ]
        
#         for model_name in preferred_models:
#             for available_model in available_models:
#                 if model_name in available_model:
#                     return model_name
                    
#         # If no preferred model is found, use the first available one
#         return available_models[0]
#     except Exception as e:
#         st.error(f"Error listing models: {str(e)}")
#         return None

def create_mindmap_markdown(text):
    """Generate mindmap markdown using Gemini AI."""
    try:
        model_name = "gemini-1.5-flash"
        
        if not model_name:
            return None
            
        st.info(f"Using model: {model_name}")
        model = genai.GenerativeModel(model_name)
        
        max_chars = 30000
        if len(text) > max_chars:
            text = text[:max_chars] + "..."
            st.warning(f"Text was truncated to {max_chars} characters due to length limitations.")
        
        prompt = """
        Create a hierarchical markdown mindmap from the following text. 
        Use proper markdown heading syntax (# for main topics, ## for subtopics, ### for details).
        Focus on the main concepts and their relationships.
        Include relevant details and connections between ideas.
        Keep the structure clean and organized.
        
        Format the output exactly like this example:
        # Main Topic
        ## Subtopic 1
        ### Detail 1
        - Key point 1
        - Key point 2
        ### Detail 2
        ## Subtopic 2
        ### Detail 3
        ### Detail 4
        
        Text to analyze: {text}
        
        Respond only with the markdown mindmap, no additional text.
        """
        
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            }
        ]
        
        generation_config = {
            "temperature": 0.2,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
        }
        
        response = model.generate_content(
            prompt.format(text=text),
            safety_settings=safety_settings,
            generation_config=generation_config
        )
        
        if not response.text or not response.text.strip():
            st.error("Received empty response from Gemini AI")
            return None
            
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating mindmap: {str(e)}")
        return None

def create_markmap_html(markdown_content):
    """Create HTML with enhanced Markmap visualization."""
    markdown_content = markdown_content.replace('`', '\\`').replace('${', '\\${')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            #mindmap {{
                width: 100%;
                height: 600px;
                margin: 0;
                padding: 0;
            }}
        </style>
        <script src="https://cdn.jsdelivr.net/npm/d3@6"></script>
        <script src="https://cdn.jsdelivr.net/npm/markmap-view"></script>
        <script src="https://cdn.jsdelivr.net/npm/markmap-lib@0.14.3/dist/browser/index.min.js"></script>
    </head>
    <body>
        <svg id="mindmap"></svg>
        <script>
            window.onload = async () => {{
                try {{
                    const markdown = `{markdown_content}`;
                    const transformer = new markmap.Transformer();
                    const {{root}} = transformer.transform(markdown);
                    const mm = new markmap.Markmap(document.querySelector('#mindmap'), {{
                        maxWidth: 300,
                        color: (node) => {{
                            const level = node.depth;
                            return ['#2196f3', '#4caf50', '#ff9800', '#f44336'][level % 4];
                        }},
                        paddingX: 16,
                        autoFit: true,
                        initialExpandLevel: 2,
                        duration: 500,
                    }});
                    mm.setData(root);
                    mm.fit();
                }} catch (error) {{
                    console.error('Error rendering mindmap:', error);
                    document.body.innerHTML = '<p style="color: red;">Error rendering mindmap. Please check the console for details.</p>';
                }}
            }};
        </script>
    </body>
    </html>
    """
    return html_content

def main():
    st.set_page_config(page_title="Mindmapify - AI-Powered Mindmaps", layout="wide")

    # Sidebar
    with st.sidebar:
        st.title("📌 Mindmapify")
        st.write("*Convert PDFs into structured interactive mindmaps using AI.*")
        st.markdown("---")
        st.write("### 🔍 How it Works:")
        st.write("1️⃣ Upload a PDF file 📄")
        st.write("2️⃣ AI extracts key information 🤖")
        st.write("3️⃣ View interactive mindmap 📊")
        st.markdown("---")
        
        api_choice = st.radio("Select AI Provider:", ["Google Generative AI (requires key)", "Simple Generator (no API needed)"])
        
        if api_choice == "Google Generative AI (requires key)":
            api_key = st.text_input("Enter your Google API Key:", type="password", value=API_KEY)
           

    # Main app layout
    st.title("📚 Mindmapify - PDF to AI-Powered Mindmap")

    # Configure Google AI
    if api_choice == "Google Generative AI (requires key)" and not configure_genai():
        return

    # File upload
    uploaded_file = st.file_uploader("📂 Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        with st.spinner("🔄 Processing PDF..."):
            text = extract_text_from_pdf(uploaded_file)
            if text:
                st.success(f"✅ Successfully extracted {len(text)} characters from PDF")
                
                # Generate mindmap content based on selected method
                if api_choice == "Google Generative AI (requires key)" and API_KEY:
                    markdown_content = create_mindmap_markdown(text)
                    if not markdown_content:
                        st.warning("AI generation failed. Falling back to simple generator.")
                        markdown_content = generate_simple_mindmap(text)
                else:
                    markdown_content = generate_simple_mindmap(text)

                if markdown_content:
                    tab1, tab2 = st.tabs(["📊 Interactive Mindmap", "📝 Markdown View"])

                    with tab1:
                        html_content = create_markmap_html(markdown_content)
                        components.html(html_content, height=700, scrolling=True)

                    with tab2:
                        st.text_area("📝 Markdown Format", markdown_content, height=400)
                        st.download_button("⬇ Download Markdown", data=markdown_content, file_name="mindmap.md", mime="text/markdown")
                        st.download_button("⬇ Download HTML Mindmap", data=html_content, file_name="mindmap.html", mime="text/html")

def generate_simple_mindmap(text):
    """Generate a simple mindmap markdown as a fallback."""
    return f"# Main Topic\n## Subtopic 1\n### Detail 1\n- Key point 1\n- Key point 2\n## Subtopic 2\n### Detail 2"

if __name__ == "__main__":
    main()
