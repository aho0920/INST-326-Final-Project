import random
import string
import requests

class PasswordGenerator:
  def generate_password(self):
    #Andrew
    """
    Generates a secure password
    Args: 
      None
    Returns:
      secure password (string)
    """
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) #k = length
    return password
  def check_password_strength(self, password):
    #Emani
    """
    Ensures that the password is strong
    Args: 
        password (string) - the user's password
    Returns:
        True/False (boolean) - returns True if the password is strong or False if it is not 
    """
    pass

  def get_word_list(self):
    #Makachi  
    """
    get list of words from online 
    Args:
      none
    Returns:
      list of words or empty list if failed
    """
    pass
    
  def generate_passphrase(self, number):
    #Makachi 
    """
    Creates a passphrase (string of words) with the number of words inputed by user
    Args:
      num_words (int) - the user's inputed number of words to be used
    Returns:
      passphrase (string)
    """
    pass
  

  def character_substitution(self, password):
    #Emani
    """
    Substitute characters in the given password
    Args:
      password (string) - the user's given password
    Returns:
      character substituted password (string)
    """
    pass