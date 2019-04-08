class Credential :
  '''
  Class that has the user's credentials
  '''
  @classmethod
  def find_by_username(cls,username):
    '''
    methos that takes in anumber and returns a contact 
    that matches that number 

    Args:
      username:username to search for
    Returns :
      Credentials of that matches the username.
    '''
    for credential in cls.credential_list:
      if credential.username == username:
        return credential

  credential_list =[] 

  def save_credential(self):
      '''
      save_credential method saves contact objects into credential_list
      '''
      Credential.credential_list.append(self)

  def __init__(self,username,number,password,confirmation_password):
    
    self.username =username
    self.phone_number = number
    self.password = password
    self.confirmation_password =confirmation_password

  
  