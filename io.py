import json

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)
    

def read(list_of_classes):
    with open('data.json') as f:
        data = json.load(f)
        
    for cls in list_of_classes:
        name = cls.__name__
        
        objects = list()        
        for dicts in data[name]:
            objects.append(cls(**dicts))

def write(list_of_classes):

    # for a given class, store each instance's variables as a dict.
    # returns a list of the dicts.
    def class_read(cls):            
        instance_vars = []
        class_name = cls.__name__
        
        for instance in cls._registry:                 
            instance_vars.append(vars(instance))
                  
        return instance_vars

    # create a dictionary to hold all classes.
    # for every class, creates a list of class objects, using class_read()
    
    def json_builder():      
        all_classes = {}
        
        for cls in list_of_classes:
           all_classes[cls.__name__] = class_read(cls)
   
        with open('data.json', 'w') as f:
            json.dump(all_classes, f, indent=2)
            
    json_builder()
    
def create_new(list_of_classes):
    pass
    # before this module can be used to read and write to the json file,
    # a json file will need to be created.
    
