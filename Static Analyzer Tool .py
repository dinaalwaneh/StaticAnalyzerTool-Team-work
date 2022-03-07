#!/usr/bin/env python
# coding: utf-8

# ### Here I read the Python code and then stored it in the "codeFile" variable,
# ### after that we will go through each line of the codeFile so that this line is not empty or contains a comment,
# ### and then add it to the "stackCode" . 
# ****************************************

# In[1]:


stackCode = []
with open('PythonCode.py', 'r') as codeFile:
    for line in codeFile:
        line = line.strip()
        if line and "#" not in line:
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
#Result = > [1, 4, 11] >> thats mean that we have function start at index 1 , function start at index 4 and function start at index 11 . 


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

# #### Create reporte file to save the bygs :

# In[7]:


reportFile= open("Report.txt","w+")


# In[8]:


def StaticAnalyzerFun(function):
    
    if(divisionIsFound(function)==True):
        TestDivideByZero(function)


# ### this dunction will check if the function which is passes to static analyzer
# ### have a division or not to applay TestDivideByZero function on it .
# ***
# 

# In[9]:


def divisionIsFound(function):
    for line in function:
        if "/" in line:
            return True
    return False


# ###  TestDivideByZero will receive the function
# ### and It passes each line by it and stores the arithmetic sentences inside ArithmeticSentences list , 
# ### then it will  passes each Arithmetic Sentence ArithmeticSentences list to get the denominator 
# ### and check if the value of the denominator is not equal to zero before the arithmetic operation applied
# ### finally it will write the bug on  report file if it is found .
# 

# In[10]:


def TestDivideByZero(function):
    
    ArithmeticSentences = [] 
    for line in function:
        if "/" in line:
            ArithmeticSentences.append(line)
    
 
    for ArithmeticSentence in ArithmeticSentences:
        divisionSymbolIndex =  ArithmeticSentence.index("/")
        denominator = ArithmeticSentence[divisionSymbolIndex+1:len(ArithmeticSentence)-1]
        for i in range(0,function.index(ArithmeticSentence)):
            if "if("+denominator+" == 0)" not in function[i]:
                 reportFile.write("devide by zero error -> " + denominator +" = 0 ")


# ### Pass over each function which is stored inside the functionsList , and pass to the  StaticAnalyzerFun to test it
# ***

# In[11]:


for function in functionsList:
    StaticAnalyzerFun(function)


# In[12]:


reportFile.close()

