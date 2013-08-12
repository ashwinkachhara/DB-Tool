import re
from cStringIO import StringIO
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams



_input = file("09007032 - 1.pdf", 'rb')
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
    student['cpi'] = out[35] # 35 for a 2-page resume; 27 for a one-page resume
else: # Dual Degree student
    student['rollno'] = out[5]
    student['specialization'] = out[3][16:]
    student['cpi'] = out[34] # 34 for a 2-page resume; 28 for a one-page resume

print student