from paperThinRest import httpLayer

def generateExampleFromSchema(schema,indent=''):
    result = ''
    if schema['type']=='object':
        def required(field):
            if schema.get('required') is None:
                return False
            return field in schema['required']
         
        result += indent+"{\n"
        newIndent = indent+"    "
        for field,spec in schema['properties'].items():
            result += newIndent+field+": "+spec['type']+('[R]' if required(field) else '')+"\n"
        
        result += indent+"}\n"
    return result

def example(schema):
    def decorator(func):
        func.exampleSchema = schema
        return func
    return decorator
        
        
def generateDocs(packageName):
    module = __import__(packageName)
    
    class App:
        def errorhandler(self,*args,**kwargs):
            return lambda *args,**kwargs:1
        
        def add_url_rule(self,path,methods,endpoint,view_func):
            print ','.join(methods)," ",path
            doc = view_func.baseMethod.__doc__
            if doc is None:
                doc = "No documentation"

            print doc.strip()
            print 
                
            if hasattr(view_func.baseMethod, 'jsonSchema'):
                print "example request:"
                print generateExampleFromSchema(view_func.baseMethod.jsonSchema)
            
            if hasattr(view_func.baseMethod, 'exampleSchema'):
                print "example response:"
                print generateExampleFromSchema(view_func.baseMethod.exampleSchema)
            
            print
            
    
    app = App()
    httpLayer.registerRoutes(app)


if __name__ == '__main__':
    generateDocs('exampleApi.resources')