"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    length1=len(line1)
    length2=len(line2)
    
    if length1<=length2:
        length = length1
    else:
        length = length2
        
    if len(line1) == 0 and len(line2)== 0:
        return IDENTICAL
    
    if length!=0:        
        for index in range(0,length):
            if line1[index] != line2[index]:
                return index
    #if one of the line is prefix of the other
    if length1 != length2:
        return length
    else:
        return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if len(line1)<=len(line2):
        length_of_shorter_string = len(line1)
    else:
        length_of_shorter_string = len(line2)
        
    newline1 = line1.find("\n")
    newline2 = line2.find("\n")
    carriage1 = line1.find("\r")
    carriage2 = line2.find("\r")
        
    if idx>=0 and idx<=length_of_shorter_string and newline1==-1 and newline2==-1 and carriage1==-1 and carriage2==-1:
        formatted_line = line1 + "\n" + "="*idx + "^" + "\n" + line2 + "\n"
        return formatted_line
    else:
        return ""
    


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
    
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    
    if len(lines1)<=len(lines2):
        length = len(lines1)
    else:
        length = len(lines2)
    
    if len(lines1) == 0 and len(lines2) ==0:
        return (IDENTICAL, IDENTICAL)
    
    if length!=0:
        for index in range(0, length):
            if singleline_diff(lines1[index], lines2[index]) != -1:
                return (index , singleline_diff(lines1[index], lines2[index]))
            
    if len(lines1)!=len(lines2):
        return (length,0)
    elif len(lines1) == len(lines2):
        return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    openfile = open(filename,"rt")
    lines = openfile.readlines()
    lines1=[]
   
    for line in lines:
        lines1.append(line.rstrip())
        
    openfile.close()
    
    return lines1


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    
    
    (index, offset) = multiline_diff(list1, list2)
        
    if index==IDENTICAL and offset ==IDENTICAL:
        return "No differences\n"
    else:
        if index>=0 and index<len(list1) and index<len(list2):
            formatted_string = "Line " + str(index) + ":\n" + list1[index] + "\n" + "="*offset + "^\n" +  list2[index] + "\n"
            return formatted_string
        elif index >= len(list1) and index < len(list2):
            formatted_string = "Line " + str(index) + ":\n" +"\n"+ "\n" + "="*offset + "^\n" +  list2[index] + "\n"
            return formatted_string
        elif index >= len(list2) and index < len(list1):
            formatted_string = "Line " + str(index) + ":\n" +list1[index]+ "\n" + "="*offset + "^\n" +  "\n" 
            return formatted_string
       
