# a customer in the cafe
class Customer:
    def __init__(self, name, email=None):
        # check if name exists
        if not name or not isinstance(name, str):
            raise ValueError("Customer name must be a non-empty string")
        # check if email is valid
        if email and not isinstance(email, str):
            raise ValueError("Customer email must be a string") 
        # assign attributes
        self.name = name
        self.email = email
        self.id = id(self) 
        
    def get_details(self):
        # for its email, return name and email
        if self.email:
            return f"{self.name} ({self.email})"
        # otherwise, return name
        return self.name
