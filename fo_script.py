import sys
from typing import Callable,Any,Generic,TypeVar
from inspect import signature

def build(script:Callable[[],Any]):
    first_arg = ""
    for param in signature(script).parameters.values():
        first_arg = param
        break
    
    if first_arg.name == "main":
        specific = id(script)
        for key,value in globals().items():
            if id(value) == specific:
                del globals()[key]
                sys.exit(script(0))
                break        
    
    elif first_arg.name == "If":
        if first_arg.default == True:
            script()
        
    elif first_arg.name == "While":
        while first_arg.default == True:
            script()
       
T = TypeVar('T') 

class val(Generic[T]):
    def __init__(self,val):
        self.val:T = val
        
    def __call__(self, val:T = None):
        if not isinstance(val,type(None)):
            self.val = val
        else:
            return self.val
        

fun = lambda main:(
    tick := val[int](10),
    CD := lambda While=lambda:(tick() < 10):(
        tick(tick()+1),
        print(tick())
    ),build(CD)
       
            
    
);build(fun)