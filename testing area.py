def kwarg_dict(**kwargs):
    return kwargs

class Storage:
    def __init__(self,**kwargs):
        self._name = ""
        for key,value in kwargs.items():
            setattr(self,key,value)
            
    def __enter__(self):
        inst = Storage(**self.__dict__)
        return inst
    
    def __exit__(self,*_):
        pass
    
    def __format__(self, format_spec):
        to_repr = super().__getattribute__(format_spec)
        to_repr = str(to_repr)
        return to_repr
    
    @property
    def name(self):
        if self._name == "":
            for key,value in globals().items():
                if self.id == id(value):
                    self._name = key.replace("'","")
                    return self._name
                else: 
                    continue   
        else:
            return self._name  
            
class FakeGeneric:
    def __init__(self):
        pass
    
    def __getitem__(self,passed:type):
        def wrapper(value):
            if isinstance(value,passed):
                class new_object(passed):
                    
                    def __new__(cls,val:object):
                        cls._name = ""
                        return super().__new__(cls,val)
                    
                    
                    def operate(self,val:object):
                        for key,value in globals().items():
                            if self.id == id(value):
                                globals()[key] = new_object(val)
                                break
                        
                    @property
                    def name(self):
                        if self._name == "":
                            for key,value in globals().items():
                                if self.id == id(value):
                                    self._name = key.replace("'","")
                                    return self._name
                                else: 
                                    continue   
                        else:
                            return self._name                 
                            
                    @property  
                    def id(self):
                        return id(self)
                    
                    @property
                    def dict_view(self):
                        return self.__dict__
              
                return new_object(value)
            else:
                message = f"Expected type, {passed.__name__} but got {type(value).__name__}."
                raise TypeError(message)
        return wrapper

new = FakeGeneric()
del FakeGeneric

