import re, os, glob
from cStringIO import StringIO
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams

dirpath = "/home/ashwin/Dropbox/Placement/day2_2013/"
htmlpath = dirpath+"Phase1-2013.html"

def pdfParse(filename):
    _input = file(filename, 'rb')
    _output = StringIO()
    
    manager = PDFResourceManager()
    
    converter = TextConverter(manager, _output, laparams = LAParams())
    process_pdf(manager, converter, _input)
    
    out = _output.getvalue().split("\n")
    
    #for index,line in enumerate(out):
    #    print "Line", index, line
    
    student = {}
    student['name'] = out[0]
    student['branch'] = out[1]
    if out[5] == "B.Tech.": # BTech student
        student['rollno'] = out[4]
        student['specialization'] = out[5]
    elif out[5] == "M.Tech.":
        student['rollno'] = out[4]
        student['specialization'] = out[5]
    else: # Dual Degree student
        student['rollno'] = out[5]
        student['specialization'] = out[3][16:]
    return student

def htmlRead():
    _htmlfile = file(htmlpath, 'r+')
    
    html = _htmlfile.read()
    _htmlfile.close()
    return html

def addLinks(student):
    html = htmlRead()
    
    for m in re.finditer(student['name'], html):
        pass
    try:
        print m
    except UnboundLocalError:
        stuName = student['name'].split(" ")
        if stuName.length() == 3:
            print stuName
        #for m in re.finditer(stuName[])
    
    filesearch = student['rollno']+'*'
    
    insertString = ""
    for filename in glob.glob(dirpath+filesearch):
        insertString = insertString + " <a href=\""+filename+"\">"+filename[-5]+"</a>"
    if html[m.end(0)+2:m.end(0)+8] == "<a href":
        insertString = ""
    #print insertString
    #print html[:m.end(0)]+insertString+html[m.end(0):]
    _htmlfile = file(dirpath+"Phase1-2013.html", 'w')
    _htmlfile.write(html[:m.end(0)]+insertString+html[m.end(0):])
    
def main():
    for filename in glob.glob(dirpath+"* - 1.pdf"): #But there is also a filetype of * - 1_001.pdf; Probably just a redundancy in files?
        print filename
        student = pdfParse(filename)
        addLinks(student)
    

if __name__ == "__main__":
    main()