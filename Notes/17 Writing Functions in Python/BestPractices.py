#Docstrings - best way to explain/show the functionality of a function and its parameters passed and their purpose.

#Example:
def function(arg_1, arg_2=42):
  """Description of what the function does.  
  
  Args:    
    arg_1 (str): Description of arg_1 that can break onto the next line      
    if needed.    
    arg_2 (int, optional): Write optional when an argument has a default      
    value.  
  
  Returns:    
    bool: Optional description of the return value    
    Extra lines are not indented.  
  
  Raises:    
    ValueError: Include any error types that the function intentionally      
    raises.  
  
  Notes:    
    See https://www.datacamp.com/community/tutorials/docstrings-python    
    for more info.    
  """