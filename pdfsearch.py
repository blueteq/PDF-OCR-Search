import os
import sys
import glob

rootfolder = str(sys.argv[1])
print "Root Folder: " + rootfolder
search = str(sys.argv[2])
print "search: " + search

def recursive_search_pdf(file_path):
    for dirname in os.walk(file_path):
        for file_path in glob.glob(os.path.join(dirname[0], '*.PDF')):
            print "Checking File: " + file_path
            if does_contain_search_term(search, file_path):
                move_pdf_to_destination(search, file_path)

def create_destination_folder_for_move(search_string):
    foldername = search_string.lower()
    print("Creating Destination Folder: " + foldername)
    os.popen("mkdir -p " + foldername)
    return foldername

def does_contain_search_term(search, filename):
    stream = os.popen("pdftotext " + filename + " - | grep -i " + search)
    output = stream.read()
    if output:
        return True
    else:
        print "No Match Found"
        return False

def move_pdf_to_destination(search, pdf_filename):
    foldername = create_destination_folder_for_move(search)
    print("Moving File: " + foldername)
    os.popen("mv " + pdf_filename + " " + foldername)

recursive_search_pdf(rootfolder)
