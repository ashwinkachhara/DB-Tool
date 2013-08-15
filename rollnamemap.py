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
    try:
        process_pdf(manager, converter, _input)
    except:
        _input = file(dirpath+filename[-16:-6]+" 4.pdf", 'rb')
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
        if out[5] == "":
            student['rollno'] = out[6]
        else:
            student['rollno'] = out[5]
        student['specialization'] = out[3][16:]
#    if student['name'] == "Prageet Sharma":
#        for index,line in enumerate(out):
#            print "Line", index, line
    return student

def htmlRead():
    _htmlfile = file(htmlpath, 'r+')
    
    html = _htmlfile.read()
    _htmlfile.close()
    return html

def addLinks(student):
    html = htmlRead()
    mStart = 0
    mEnd = 0
    for x in re.finditer(student['name'], html):
        mStart = x.start(0)
        mEnd = x.end(0)
    try:
        print x#, student['name'], student['rollno']
    except UnboundLocalError:
        stuName = student['name'].split(" ")
        if len(stuName) == 3:
            search = stuName[1]+" "+stuName[0]
            print search
            for x in re.finditer(search, html):
                mEnd = x.end(0)
                mStart = x.start(0)
    print mStart, mEnd
    filesearch = student['rollno']+'*'
    insertString = ""
    for filename in glob.glob(dirpath+filesearch):
        #print filename
        insertString = insertString + " <a href=\""+filename+"\">"+filename[-5]+"</a>"
    if html[mEnd+2:mEnd+8] == "<a href":
        insertString = ""
    #print insertString
    #print html[:m.end(0)]+insertString+html[m.end(0):]
    if mStart != mEnd:
        _htmlfile = file(dirpath+"Phase1-2013.html", 'w')
        _htmlfile.write(html[:mEnd]+insertString+html[mEnd:])
    
def main():
    for filename in glob.glob(dirpath+"* - 1.pdf"): #But there is also a filetype of * - 1_001.pdf; Probably just a redundancy in files?
        print filename
        student = pdfParse(filename)
        addLinks(student)
    

if __name__ == "__main__":
    main()