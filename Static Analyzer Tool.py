#!/usr/bin/env python
# coding: utf-8

# ### Here I read the Python code and then stored it in the "codeFile" variable, after that we will go through each line of the codeFile so that this line is not empty or contains a comment, and then add it to the "stackCode" . 
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

# In[5]:


startIndexOfFunction = []
for line in stackCode:
    if ("def" in line):
        startIndexOfFunction.append(stackCode.index(line))       


# In[6]:


startIndexOfFunction
#Result = > [1, 4, 11] >> thats mean that we have function start at index 1 , function start at index 4 and function start at index 11 . 


# ####  Here I have stored all the functions inside functionsList "PS : the start of some function is the end of another":
# ***********************
# 

# In[7]:


functionsList=[]
for i in range(0,len(startIndexOfFunction)):
    if(i==(len(startIndexOfFunction)-1)):
        functionsList.append(stackCode[startIndexOfFunction[i]:len(stackCode)])
        break;
    functionsList.append(stackCode[startIndexOfFunction[i]:startIndexOfFunction[i+1]])


# In[8]:


functionsList
#The result is list of list each list in the parent list contains one function :

