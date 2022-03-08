#!/usr/bin/env python
# coding: utf-8

# ### Here I read the Python code as "codeFile" ,
# ### after that we will go through each line of the codeFile
# ### and then add it to the "stackCode" list . 
# ****************************************

# In[1]:


stackCode = []
with open('PythonCode.py', 'r') as codeFile:
    for line in codeFile:      
        stackCode.append(line)


# In[2]:


#print stackCode :
stackCode


# ### Get the start index for each function in the code
# ****************************************

# In[3]:


startIndexOfFunction = []
for line in stackCode:
    if ("def" in line):
        startIndexOfFunction.append(stackCode.index(line))       


# In[4]:


startIndexOfFunction
#If Result = > [1, 4, 11] >> thats mean that we have function start at index 1 , function start at index 4 and function start at index 11 . 


# ####  Here I have stored all the functions inside functionsList "PS : the start of some function is the end of another":
# ***********************
# 

# In[5]:


functionsList=[]
for i in range(0,len(startIndexOfFunction)):
    if(i==(len(startIndexOfFunction)-1)):
        functionsList.append(stackCode[startIndexOfFunction[i]:len(stackCode)])
        break;
    functionsList.append(stackCode[startIndexOfFunction[i]:startIndexOfFunction[i+1]])


# In[6]:


functionsList
#The result is list of list each list in the parent list contains one function. 


# ### Our Static Analyzer Tool :)
# *****************

# ## Check list functions implementation :
# ...................................................................................................................

# # 1. Divide by zero :
# ***
# 
# #### this function will check if the function which is passes to static analyzer
# #### have a division or not to applay TestDivideByZero function on it .
# ***
# 

# In[7]:


def divisionIsFound(function):
    for line in function:
        if "/" in line:
            return True
    return False


# ####  TestDivideByZero function will receive the function
# #### and It passes each line by it and stores the arithmetic sentences inside ArithmeticSentences list ,
# #### in addetion it will store the location of the arithmetic sentence relative to the code to be checked in the lineIndex list
# #### then it will  passes each Arithmetic Sentence ArithmeticSentences list to get the denominator 
# #### and check if the value of the denominator is not equal to zero before the arithmetic operation applied
# #### finally it will write the bug on  report file if it is found and its line .
# 

# In[8]:


def TestDivideByZero(function):
    ArithmeticSentences = []
    lineIndex=[]
    for line in function:
        if "/" in line:
            ArithmeticSentences.append(line)
            lineIndex.append(stackCode.index(line))
 
    flag=1
    for ArithmeticSentence in ArithmeticSentences:
            divisionSymbolIndex =  ArithmeticSentence.index("/")
            denominator = ArithmeticSentence[divisionSymbolIndex+1:len(ArithmeticSentence)-1]
            for i in range(0,function.index(ArithmeticSentence)):
                if "if("+denominator+" == 0)" not in function[i]:
                    flag=0
            if(flag==0):
                reportFile.write("devide by zero error ->" + denominator +"= 0 at line "+str(lineIndex[ArithmeticSentences.index(ArithmeticSentence)]+1) +"\n")


# # 2. Null pointer exception :
# ***
# 
# #### PointerIsFound function will check if the function which is passes to static analyzer
# #### have a dot  symbol on other word check if the function have a ponter call its proirties 
# #### or not to applay TestNullPointer function on it .
# ***
# 

# In[9]:


def PointerIsFound(function):
    for line in function:
        if "." in line:
            return True
    return False


# ###  Get variable Name ,  its index relative to the function itself + its index relative to the code to be checked :

# In[10]:


def GetObjectNameAndindex(function):
    objectName = ""
    for line in function: 
        if "." in line :
            indexOfDot= line.index(".");
            indexOfLineAtFunc = function.index(line)
            indexOfLineAtCode = stackCode.index(line)
            for i in range(indexOfDot-1, -1, -1):
                if(line[i] == " "):
                    break;
                else:
                    objectName+=line[i]
                    
    return(objectName[::-1],indexOfLineAtFunc,indexOfLineAtCode)


# #### TestNullPointer function will through on the passed function from index = 0 to the index of code which may caouse null pointer error . 
# #### to check if we have an if statment that chek if the variable ! = Null .

# In[11]:


def TestNullPointer(function,objectName,indexOfLine, indexOfLineAtCode):
    
    flag=1
    for i in range(0,indexOfLine):
        if "if("+objectName+" != None)" not in function[i]:
            flag=0
    if(flag==0):        
        reportFile.write("Null pointer exception ->" + objectName +" object = NULL at line "+ str(indexOfLineAtCode+1) +"\n" )
                


# ## implementation of our static analyzer  tool :

# #### Create reporte file to save the bygs :

# In[12]:


reportFile= open("Report.txt","w+")


# ### this StaticAnalyzerTool function will receive one function and check each line on it to see if it has any sentence that may cause any bug from the check list and if true it will call the tester functuin for this bug to print the details on text file .

# In[13]:


def StaticAnalyzerTool(function):
    
    if(divisionIsFound(function)==True):
        TestDivideByZero(function)
        
    if(PointerIsFound(function)==True):
        objectName,indexOfLine,indexOfLineAtCode = GetObjectNameAndindex(function)
        TestNullPointer(function,objectName,indexOfLine, indexOfLineAtCode)


# #### through on each function which is stored inside the functionaList , pass it to the Static Analyzer Fun to test it
# ***

# In[14]:


functionNumber = 1
for function in functionsList:
    reportFile.write("Bugs at function"+ str(functionNumber) +": \n" )
    StaticAnalyzerTool(function)
    functionNumber+=1


# In[15]:


reportFile.close()

