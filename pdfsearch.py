#! /usr/bin/python

import os
import sys
import glob

rootfolder = str(sys.argv[1])
print "Root Folder: " + rootfolder

def get_search_arguments():
    search_list = sys.argv
    search_term = ""
    index = 2
    while index < len(search_list):
            search_term = search_term + " " + search_list[index]
            index += 1 
    print "Search Term: " + search_term
    return search_term

def recursive_search_pdf(file_path):
    for dirname in os.walk(file_path):
        for filename in glob.glob(os.path.join(dirname[0], '*.PDF')):
            print "Checking File: " + filename
            search = get_search_arguments()
            print "search: " + search
            if does_contain_search_term(search, filename):
                move_pdf_to_destination(search, filename)

def create_destination_folder_for_move(search_string):
    foldername = search_string.lower()
    print("Creating Destination Folder: " + foldername)
    os.popen("mkdir '" + foldername +"'")
    return foldername

def does_contain_search_term(search, filename):
    stream = os.popen("pdftotext " + filename + " - | grep -i '" + search + "'")
    output = stream.read()
    if output:
        print "Found Match: " + search
        return True
    else:
        print "No Match Found"
        return False

def move_pdf_to_destination(search, pdf_filename):
    foldername = create_destination_folder_for_move(search)
    print("Moving PDF File: " + pdf_filename + " to " + foldername)
    os.popen("mv '" + pdf_filename + "' '" + foldername + "'")

recursive_search_pdf(rootfolder)
