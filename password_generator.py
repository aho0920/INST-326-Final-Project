import random
import string
import requests

class PasswordGenerator:
  def generate_password(self):
    # Driver: Makachi
    # Navigator: Andrew
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
    # Driver: Diana
    # Navigator: Emani
    """
    Ensures that the password is strong
    Args: 
        password (string) - the user's password
    Returns:
        True/False (boolean) - returns True if the password is strong or False if it is not 
    """
    # Convert the given password to string
    passwordStr = str(password)
    if len(passwordStr) < 8:
        return False

    # Check for at least one uppercase letter, one lowercase letter, one digit, and one special character
    has_upper = any(char.isupper() for char in passwordStr)
    has_lower = any(char.islower() for char in passwordStr)
    has_digit = any(char.isdigit() for char in passwordStr)
    has_special = any(char in string.punctuation for char in passwordStr)

    return has_upper and has_lower and has_digit and has_special

  def get_word_list(self):
    # Driver: Andrew  
    # Navigator: Makachi
    """
    get list of words from online 
    Args:
      none
    Returns:
      list of words or empty list if failed
    """
    # Fetch a list of common English words from an randomlists.com
    response = requests.get("https://www.randomlists.com/data/words.json")
    if response.status_code == 200:
        word_list = response.json()["data"]
        return word_list
    else:
        print("Failed to fetch word list.")
        return []


    
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
    # Define a dictionary for character substitution
    substitution_map = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '$',
        't': '7',
        'A': '4',
        'E': '3',
        'I': '1',
        'O': '0',
        'S': '$',
        'T': '7',
        ' ': '_'
    }
       
    # Iterate over each character in the password and substitute if it matches
    substituted_password = ''
    for char in password:
        substituted_password += substitution_map.get(char, char)  
    # If char not in map, keep it unchanged
   
    return substituted_password


