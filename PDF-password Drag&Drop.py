#  PDF password protection with Python, Serjik.
#
#  pip install PyPDF2

from PyPDF2 import PdfReader, PdfWriter
import getpass, os , sys


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print('''
    ----------------------------------------------------------
           Welcome to Serjik's PDF password encryption!       
    ---------------------------------------------------------- 
          \n''')
    
    if len(sys.argv) > 1:
        full_file = sys.argv[1]
        file_name = os.path.basename(full_file)
        path = full_file[: -len(file_name)]
        new_file = path + 'Pass_' + file_name
        
        if file_name[-4 :].lower() == '.pdf':
            print ('Encrypting the PDF file: ', file_name , '\n')
        else:
            print (f'Error:   {file_name} Is Not a PDF file! \n\n\nPress Enter to Exit!')
            input()
            exit()
    else:
        print("Please drag and drop a PDF file onto this App.")
        input("\nPress Enter to Exit!")
        exit()


    try:
        with open(full_file, "rb") as in_file:
            pdf_pass = getpass.getpass("Please enter new password: ")
            pdf_pass_conf = getpass.getpass("Please confirm the password: ")
            if (pdf_pass == pdf_pass_conf):
                input_pdf = PdfReader(in_file)

                output_pdf = PdfWriter()
                output_pdf.append_pages_from_reader(input_pdf)
                output_pdf.encrypt(pdf_pass)

                with open(new_file, "wb") as out_file:
                    output_pdf.write(out_file)
                print("\nNew password protected PDF has been created:\n   Pass_" + file_name )
            else:
                print("The password didn't match!")

    except Exception as e:
        print(e)

    finally:
        input('\n Good Bye.')    
    
if __name__ == '__main__':
    main()