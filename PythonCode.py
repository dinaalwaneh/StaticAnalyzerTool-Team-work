
class program:
 
    
    def Calculate(number:int,divisor:int):
        result = number/divisor;
        return result


    def GetStatusValue(status:int):
        if status == -1:
            print("fail")
        elif status >= 1:
            print("success")      
        elif status <= 0:
            print("invalid")
            
            
            
    def checkStatus():
        GetStatusValue(2,5)
        GetStatusValue("fail")
        
    
    def parameters(a:int,b:str,c:chr,d:int):
        return 1
    
    
    def unReachable(status:int):
        if status == 0:
            return "fail";
                
        elif status == 0:
            return 0   
                   
        return "Pass"
                
        print("Exit")   
        return "Pass"   
           
            
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
