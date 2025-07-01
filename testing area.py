def kwarg_dict(**kwargs):
    return kwargs

class Storage:
    def __init__(self,**kwargs):
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
        self_id = id(self)
        for key,val in globals().items():
            if self_id == id(val):
                return key.replace("'","")
            else: continue
            
class FakeGeneric:
    def __init__(self):
        pass
    
    def __getitem__(self,passed:type):
        def wrapper(val):
            if isinstance(val,passed):
                class _(passed):
                    def __new__(cls,val:object):
                        return super().__new__(cls,val)
                    
                    def __init__(self):
                        self.type = passed.__name__.replace("'","")
                    
                    @property
                    def name(self):
                        self_id = id(self)
                        for key,val in globals().items():
                            if self_id == id(val):
                                return key.replace("'","")
                            else: continue
                            
                    @property  
                    def id(self):
                        return id(self)
                    
                    @property
                    def dict_view(self):
                        return self.__dict__
                    
  
            else:
                message = f"Expected type, {passed.__name__} but got {type(val).__name__}."
                raise TypeError(message)
        return wrapper

var = FakeGeneric()
del FakeGeneric
x = var[int](10)