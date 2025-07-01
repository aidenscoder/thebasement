import sys
from typing import Callable,Any,Generic,TypeVar
from inspect import signature

def build(script:Callable[[],Any]):
    first_arg = ""
    parameters = signature(script).parameters
    for param in parameters.values():
        first_arg = param
        break
    specific = id(script)
    if first_arg.name == "main":
        
        for key,value in globals().items():
            if id(value) == specific:
                del globals()[key]
                returner = list(script(0))
                returner = returner[len(returner)-1]
                print(returner)
                if isinstance(returner,int):
                    sys.exit(int(returner or 0))
                else:
                    raise TypeError(f"Expected type int but got {type(returner).__name__}")
                break        
    
    elif first_arg.name == "If":
        if first_arg.default == True:
            script()
            
        for key,value in globals().items():
            if id(value) == specific:
                del globals()[key]
                break    
        
    elif first_arg.name == "While":
        while first_arg.default() == True:
            script()
            
        for key,value in globals().items():
            if id(value) == specific:
                del globals()[key]
                break    
    
    elif parameters["For"].name == "For":
        for item in parameters["For"].default:
            script(*item)
            
        for key,value in globals().items():
            if id(value) == specific:
                del globals()[key]
                break    
            

       
T = TypeVar('T') 

class val(Generic[T]):
    def __init__(self,val):
        self.val:T = val
        
    def __call__(self, val:T = None):
        if not isinstance(val,type(None)):
            self.val = val
        else:
            return self.val
        
class Struct:
    def __init__(self,*types:tuple[object]):
        self.types = types
        self.structures = {}
        
    def __call__(self,**kwargs):
        for key,value in kwargs.items():
            if value in self.types:
                self.structures[key] = value
            else:
                names = list(map(lambda x:x.__name__,self.types))
                raise TypeError(f"Expected types, {names} as a structure attribute but got {value.__name__}.")


