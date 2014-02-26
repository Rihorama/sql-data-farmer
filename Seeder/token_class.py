"""TOKEN CLASSES"""

  
class Token:
  token_type = None
  token_value = None
  token_line = None
  
  def set_type(self, new_type):
    self.token_type = new_type
    
  def set_value(self, new_value):
    self.token_value = new_value
    
  def set_line(self, line):
    self.token_line = line