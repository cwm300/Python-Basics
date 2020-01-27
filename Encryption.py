# funtion takes pdf and creates new encrypted version

def encrypt():
    import PyPDF2
    pdf_name = input("Enter PDF file name: ")
    pdf_final = pdf_name + ".pdf"
    pdf_file = open(pdf_final, "rb")
    
    # Create reader and writer object
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    pdfWriter = PyPDF2.PdfFileWriter()
    
    # Add all pages to writer (accepted answer results into blank pages)
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))
        
    # Encrypt with your password
    global user_pass
    user_pass = input("Create a password: ")
    while len(user_pass) < 8:
        print("Password must be at least 8 characters")
        user_pass = input("Create a password: ")        
        
    pdfWriter.encrypt(user_pass)
    
    # Write it to an output file. (you can delete unencrypted version now)
    resultPdf = open(pdf_name + "_secure" + ".pdf", "wb")
    pdfWriter.write(resultPdf)
    resultPdf.close()

    
def main():
    encrypt()
main()


