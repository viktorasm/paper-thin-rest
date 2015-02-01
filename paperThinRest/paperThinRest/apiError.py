class ApiErrorException(Exception):
    def __init__(self,message=None,status=400):
        self.status = status
        self.message = message
        self.errors = []
        
        
    def responseObject(self):
        return {'message':self.message,'errors':self.errors,'status':self.status}
    
    
    def jsonValidationFailed(self,err):
        self.validationFailed()
        self.fieldError('.'.join(err.path), err.message)
        
        return self
    
    def fieldError(self,field,message):
        self.errors.append({'field':field,'message':message})
        return self
        

    def validationFailed(self):
        '''
        configure values to describe a failed validation
        '''
        
        self.message = 'Validation failed'
        self.status = 400
        return self
    
    def invalidRequest(self):
        '''
        configure values to describe general problem with the request
        '''
        
        self.message = 'Invalid request'
        self.status = 400
        return self
    
    def resourceNotFound(self):
        '''
        REST resource was not found
        '''
        self.message = 'Resource not found'
        self.status = 404
        return self
    
    def notImplemented(self):
        self.message = 'not implemented'
        self.status = 500
        return self
    
    def notSupported(self):
        self.message = 'not supported'
        self.status = 400
        return self
    
    
    