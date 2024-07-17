import markdown2, io
from xhtml2pdf import pisa

# Function to convert Markdown to HTML while preserving newlines
def convert_markdown_to_html_with_line_breaks(markdown_content):
    html_content = markdown2.markdown(markdown_content)
    return html_content

# Function to convert HTML to PDF
def convert_html_to_pdf(source_html, output_filename):
    result_file = io.BytesIO()
    pisa_status = pisa.CreatePDF(source_html, dest=result_file)
    result_file.seek(0)
    return result_file,pisa_status.err

def generate_pdf(text):
    markdown_content = text

    # Convert the markdown content to HTML
    html_content = convert_markdown_to_html_with_line_breaks(markdown_content)
    
    pdf_buffer, error = convert_html_to_pdf(html_content, "output.pdf")
    if error:
        raise Exception("Error generating PDF")
    return pdf_buffer 