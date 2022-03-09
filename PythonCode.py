#!/usr/bin/env python
# coding: utf-8

class program:
 
    
    def Calculate(number:int,divisor:int):
        result = number/divisor;
        return result


    def GetStatusValue(status:int):
        if status == -1 :
            print("faild")
        elif status == 1:
            print("success")      
        elif status == 0:
            print("invalid")
            
            
            
    def checkStatus():
        GetStatusValue(2,5)
        GetStatusValue("failed")
        
    
    def parameters(param1:int,param2:str,param3:chr,param4:int):
        return 1
    
    
    def unReachable(status:int):
        if status  == 0:
            return "failed";
                
        elif status == 0:
            return 0   # This line is unreachable
                   
        return "Pass"
                
        print("Exit")  # This line is unreachable
        return "Pass"  # This line is unreachable
          
            
            
    def Print(student):
        print("Student", student.name)
        
    
    def PrintName():
        try:
            print(x)
        except NameError:
            print("The 'try ' is finished")  
        except One:
              
        finally:
             print("The 'try ' is finished")                
