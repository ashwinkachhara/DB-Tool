Resume-DB-Tool
==============

Given a set of resumes (IITB Header format) [<rollno> - x.pdf; x is some number from 0 - 8], this script parses the header and extracts data about the student.
This data (specifically the name) is then used to link the resumes to a page downloaded from Placement Blog.

The webpage contains names of all students selected in a particular company. The script searches for a student name and
adds the links to all the resume files associated to that student.

-Right now using absolute file paths (specific to my laptop)
-Some errors due to name spelling differences in the webpage and in the resume

Correctly matching about 70% of the cases
