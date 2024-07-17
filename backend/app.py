from flask import Flask, request, jsonify,send_file
from main import analyse_text
import io, docx2txt, os
from flask_cors import CORS
from pdf import generate_pdf

app = Flask(__name__)
CORS(app) 
 
@app.route('/test', methods=['POST'])
def handle_post():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
 
    file = request.files['file']
 
    # If user does not select a file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
 
    if file:
        file_ext = os.path.splitext(file.filename)[1].lower()
        
        # Check if the file is a .docx file
        if file_ext != '.docx':
            return jsonify({"message": "File type not allowed, only .docx files are allowed"}), 400
        
        stream = io.BytesIO()
        file.save(stream)
        stream.seek(0)
 
        # Use docx2txt to extract text from DOCX file
        text = docx2txt.process(stream)
 
        # Analyze the extracted text
        analysis_result = analyse_text(text)
        
        #print(analysis_result)
        
        pdf_buffer = generate_pdf(analysis_result)
        # Return the analysis result
        
        return send_file(pdf_buffer, mimetype='application/pdf', as_attachment=True, download_name='analysis_result.pdf')
 
    return jsonify({"message": "Please try after few minutes"}), 500
 
if __name__ == '__main__':
    app.run(debug=True)
 
 