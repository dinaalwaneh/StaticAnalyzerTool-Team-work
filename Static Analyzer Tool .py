#!/usr/bin/env python
# coding: utf-8

# ### Here I read the Python code and then stored it in the "codeFile" variable,
# ### after that we will go through each line of the codeFile so that this line is not empty or contains a comment,
# ### and then add it to the "stackCode" . 
# ****************************************

# In[1]:


stackCode = []
with open('q3.py', 'r') as codeFile:
    for line in codeFile:
        line = line.strip()
        if line and "#" not in line:
            stackCode.append(line)


# In[2]:


#print stackCode :
stackCode



# ### Get the start index for each function in the code
# ### & Get the start function in the code

# ****************************************

# In[3]:


startIndexOfFunction = []
startFun = []
for line in stackCode:
    if ("def" in line):
        startIndexOfFunction.append(stackCode.index(line))   
        startFun.append(line)          


# In[4]:


startIndexOfFunction
#Result = > [1, 4, 11] >> thats mean that we have function start at index 1 , function start at index 4 and function start at index 11 . 



# In[4]:
startFun
#Result = > The first line in each function ,,,ex: "def Calculate(self, number,  divisor):"


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
        
    if(PointerIsFound(function)==True):
        objectName,indexOfLine = GetObjectNameAndindex(function)
        TestNullPointer(function,objectName,indexOfLine)
        


# ### this function will check if the function which is passes to static analyzer
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
                 reportFile.write("devide by zero error -> " + denominator +" = 0\n")


# ### this function will check if the function which is passes to static analyzer
# ### have a dot  symbol on other word check if the function have a ponter call its proirties 
# ### or not to applay TestNullPointer function on it .
# ***
# 

# In[11]:


def PointerIsFound(function):
    for line in function:
        if "." in line:
            return True
    return False


# ###  Get pointer Name and its index :

# In[12]:


def GetObjectNameAndindex(function):
    objectName = ""
    for line in function: 
        if "." in line :
            indexOfDot= line.index(".");
            indexOfLine = function.index(line);
            for i in range(indexOfDot-1, -1, -1):
                if(line[i] == " "):
                    break;
                else:
                    objectName+=line[i]
                    
    return(objectName[::-1],indexOfLine)
                    


# ### TestNullPointer function will through on the passed function from index = 0 to the index of pointer 
# ### to check if we have an if statment that chek if the pointer ! = Null .

# In[13]:


def TestNullPointer(function,objectName,indexOfLine):
    for i in range(0,indexOfLine):
        if "if("+objectName+" != None)" not in function[i]:
                 reportFile.write("Null pointer exception ->" + objectName +" object = None \n" )


# ### Pass over each function which is stored inside the functionsList , and pass to the  StaticAnalyzerFun to test it
# ***

# In[14]:


functionNumber = 1
for function in functionsList:
    reportFile.write("Bugs at function"+ str(functionNumber) +": \n" )
    StaticAnalyzerFun(function)
    functionNumber+=1


# In[15]:  

# ###Function to make sure there are no more than three parameters for the functions

def NumOfParam(function):
    for line in startFun:
        if "," in line:
            count=line.count(",")
            if count>=3:
                return "not allowed"
            
            
# In[16]:
NumOfParam(startFun)    
    
    
    
# In[17]:


reportFile.close()

