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
                reportFile.write("* devide by zero error ->" + denominator +"= 0 at line -> "+str(lineIndex[ArithmeticSentences.index(ArithmeticSentence)]+1) +"\n")


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


def TestNullPointer(function):
    VariableName,indexOfLine,indexOfLineAtCode = GetObjectNameAndindex(function)
    flag=1
    for i in range(0,indexOfLine):
        if "if("+VariableName+" != None)" not in function[i]:
            flag=0
    if(flag==0):        
        reportFile.write("* Null pointer exception :" + VariableName +" may = NULL at line -> "+ str(indexOfLineAtCode+1) +"\n" )
                


# # 3. Hiding/ burying exceptions :
# ***
# 
# #### GetStartIndexOfExcept function 
# ***
# 

# In[12]:


def GetStartIndexOfExcept():
    startIndexOfExcept = []
    for line in stackCode :
        if ("except" in line):
            startIndexOfExcept.append(stackCode.index(line))   
    return startIndexOfExcept


# In[13]:


#print start Index Of each Except
startIndexOfExcept = GetStartIndexOfExcept()
startIndexOfExcept


# #### GetExceptsList function will get all the blocks for exceps in the code :

# In[14]:


def GetExceptsList(startIndexOfExcept):
    exceptsList=[]
    for i in range(0,len(startIndexOfExcept)):
        if(i==(len(startIndexOfExcept)-1)):
            exceptsList.append(stackCode[startIndexOfExcept[i]:len(stackCode)])
            break;
        exceptsList.append(stackCode[startIndexOfExcept[i]:startIndexOfExcept[i+1]])
    return exceptsList


# In[15]:


exceptsList = GetExceptsList(startIndexOfExcept)


# #### TestHidingexception function will pass on eech except block at exceptsList an chick if it has an action or not :

# In[16]:


def TestHidingExcption():
    for line in exceptsList:        
        flag=0
        for i in range(1,len(line)):
            if((len(line[i]) - len(line[i].lstrip()))<=(len(line[0]) - len(line[0].lstrip()))):
                break;

            elif(not(line[i].strip()) or "#" in line[i] ) :
                flag=0
            else:
                flag=1
                break
            if(flag==0):
                reportFile.write("* Hiding/burying exceptions at line -> "+ str(startIndexOfExcept[exceptsList.index(line)]+1)+ "\n")


# # 4. Magic number :
# ***
# 
# #### Description
# ***
# 

# # 5. Do the attributes (e.g., data type and size) :
# ***
# 
# #### This function returns number and data type of function parameters 
# ***
# 

# In[17]:


def checkParamsProperties(function):
    parameters=function[function.index("(")+1: function.index(")")]
    parameters=parameters.split(",") 
    dataTypeOFParams=[]
    numberOfParams=len(parameters)
 
    for param in parameters: 
        dataTypeOFParams.append(param[param.index(':')+1:])
        
    return (dataTypeOFParams,numberOfParams)


# #### This function returns number and data type of function call arguments

# In[18]:


def checkArgumentProperties(function):
    parameters=function[function.index("(")+1: function.index(")")]
    parameters=parameters.split(",")
    numberOfParams=len(parameters)
    dataTypeOFParams=[]
    
    for param in parameters:
        if "'" in param:
            dataTypeOFParams.append("chr")   
        elif param.isdigit():
            dataTypeOFParams.append("int") 
        else:
            dataTypeOFParams.append("str")
    return (dataTypeOFParams,numberOfParams)


# ### this function check if there is function call and return list of function call

# In[19]:


def CheckIfThereFunctionCall(function):
    functionsCall=[]
    for functionCall in function:
        if functionCall==function[0]:
            continue
        if "(" and ")" in functionCall and "print" not in functionCall:
            functionsCall.append(functionCall)
            
    return functionsCall


# ## this function if  the arguments and parameters matched and write on report file

# In[20]:


def CheckIfSameParametersAndArrguments(function):
    
        functionsCall=CheckIfThereFunctionCall(function)
        for functionCall in functionsCall:
            functionCallName=functionCall[:functionCall.index("(")]
            functionCallName=functionCallName.replace(' ','')
            for i in functionsList:
                functionName=i[0][8 :i[0].index("(")]
                if functionCallName == functionName:
                    numOfFuncPar=checkParamsProperties(i[0])[1]
                    numOfCallFuncPar=checkArgumentProperties(functionCall)[1]
                    
                    typeOfFuncPar=checkParamsProperties(i[0])[0]
                    typeOfCallFuncPar=checkArgumentProperties(functionCall)[0]
                    
                    if numOfFuncPar!=numOfCallFuncPar:
                        reportFile.write("* Number of attributes of function call "+functionCall.replace(" ",'')+" at line -> "+str(stackCode.index(functionCall))+" did not match the number of parameters of the function \n")
                    
                    if typeOfFuncPar !=  typeOfCallFuncPar:
                        reportFile.write("* data type of attributes of function call "+functionCall.replace(" ",'')+" at line -> "+str(stackCode.index(functionCall))+" did not match the data type of parameters of the function \n")
                        


# # 6. no more than three parameters for the methods :
# ***
# 
# #### this function will check if the function which is passes to static analyzer
# have a function or not to applay TestNumOfParam function on it 
# ***
# 

# In[21]:


def funIsFound(function):    
    for line in function:
        if ("def" in line):
            return True   
    return False


# TestNumOfParam function will receive the "function"
# pass on line by line in the stackCode to check if i find word "def" --> it mean there is a function ,then store start function in each function and the index of it
# pass on line by line in startFun (which i storing the start function) ,then cheack if the "," found to count the number of parameters in function , if the count is more than two--> it mean there is more than three parameter in the function --> and this is my goal :)
# finally it will write the bug on report file if it is found and its line .

# In[22]:


def TestNumOfParam(function):
    startFun = []
    startIndexOfFunction = []
    for line in stackCode:
        if ("def" in line):
            startFun.append(line)      
            startIndexOfFunction.append(stackCode.index(line))  
    flag=1
    for line in startFun:
        if "," in line:
            count=line.count(",")
            if count>=3:
                flag=0
                break;
    if(flag==0):
        reportFile.write("* more than three parameters -> " + str((count+1))  + " parameters in function at line -> "+str(startIndexOfFunction[startFun.index(line)]+1) +"\n")         


# # 7. Unreachable code :
# ***
# 
# #### Description
# ***
# 

# ## implementation of our static analyzer  tool :

# #### Create reporte file to save the bygs :

# In[23]:


reportFile= open("Report.txt","w+")


# ### this StaticAnalyzerTool function will receive one function and check each line on it to see if it has any sentence that may cause any bug from the check list and if true it will call the tester functuin for this bug to print the details on text file .

# In[24]:


def StaticAnalyzerTool(function):
    
    if(divisionIsFound(function)==True):
        TestDivideByZero(function)
        
    if(PointerIsFound(function)==True):  
        TestNullPointer(function)
    
    #Magic number:
    
    
    if(CheckIfThereFunctionCall(function)):
        CheckIfSameParametersAndArrguments(function)
    
    #Unreachable code:
    


# #### through on each function which is stored inside the functionaList , pass it to the Static Analyzer Fun to test it
# ***

# In[25]:


functionNumber = 1
for function in functionsList:   
    StaticAnalyzerTool(function)
    functionNumber+=1
if(funIsFound(function)==True):
    TestNumOfParam(function)     
#Hiding/burying exceptions
TestHidingExcption()    


# In[26]:


reportFile.close()

