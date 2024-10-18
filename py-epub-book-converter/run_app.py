import os
import subprocess

# Run Streamlit script using subprocess
def run_streamlit():
    streamlit_file = "py_epub_reader/epub_convertor.py"
    subprocess.Popen(["streamlit", "run", streamlit_file])

if __name__ == "__main__":
    run_streamlit()