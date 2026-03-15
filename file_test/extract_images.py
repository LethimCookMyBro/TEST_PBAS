import fitz  # PyMuPDF
import docx
import os
import io
from PIL import Image

folder = r"c:\Users\User\Downloads\PBAS\file_test"
img_folder = os.path.join(folder, "images")
os.makedirs(img_folder, exist_ok=True)

# Extract images from PDFs - render each page as image
pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
for pdf_file in sorted(pdf_files):
    pdf_name = pdf_file.replace('.pdf', '')
    pdf_img_folder = os.path.join(img_folder, pdf_name)
    os.makedirs(pdf_img_folder, exist_ok=True)
    
    print(f"--- Extracting pages from: {pdf_file} ---")
    try:
        doc = fitz.open(os.path.join(folder, pdf_file))
        for i, page in enumerate(doc):
            # Render page as image at 2x resolution for clarity
            mat = fitz.Matrix(2, 2)
            pix = page.get_pixmap(matrix=mat)
            img_path = os.path.join(pdf_img_folder, f"page_{i+1:02d}.png")
            pix.save(img_path)
        print(f"  Rendered {len(doc)} pages as images")
        doc.close()
    except Exception as e:
        print(f"  ERROR: {e}")

# Extract images from DOCX files
docx_files = [f for f in os.listdir(folder) if f.endswith('.docx')]
for docx_file in sorted(docx_files):
    docx_name = docx_file.replace('.docx', '')
    docx_img_folder = os.path.join(img_folder, docx_name)
    os.makedirs(docx_img_folder, exist_ok=True)
    
    print(f"--- Extracting images from: {docx_file} ---")
    try:
        doc = docx.Document(os.path.join(folder, docx_file))
        img_count = 0
        for rel in doc.part.rels.values():
            if "image" in rel.reltype:
                img_count += 1
                img_data = rel.target_part.blob
                ext = rel.target_part.content_type.split('/')[-1]
                if ext == 'jpeg':
                    ext = 'jpg'
                img_path = os.path.join(docx_img_folder, f"image_{img_count:02d}.{ext}")
                with open(img_path, 'wb') as f:
                    f.write(img_data)
        print(f"  Extracted {img_count} images")
    except Exception as e:
        print(f"  ERROR: {e}")

print("\nDone! All images extracted.")
